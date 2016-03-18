#!/usr/bin/env python3

import sys
import argparse
import asyncio
import aiohttp
import functools
import random
import logging
import json

import ddcm
import utils
import wordcount

parser = argparse.ArgumentParser(description='DDCM Word Count')

parser.add_argument('--config', help='config file path')

args = parser.parse_args()

async def start(loop, config, service):
    if "entrance" in config:
        future = await service.tcpService.call.ping(ddcm.Remote(
            host = config["entrance"]["host"],
            port = config["entrance"]["port"]
        ))
        result = await future
        """service.route.addNode(ddcm.Node(
            ddcm.utils.dump_node_hex(config["entrance"]["id"]),
            ddcm.Remote(
                host = config["entrance"]["host"],
                port = config["entrance"]["port"]
            )
        ))"""
        return None
    if "commit" in config:
        return await service.commit({
            "to": [config["commit"]["url"]],
            "done": [],
            "words": {}
        }, cached = True)

def generate_url(size):
    for i in range(size):
        n = random.randrange(100)
        yield "https://skyzh.github.io/social-network-site/" + str(n) + ".html"

async def main(loop, config, service):
    session = aiohttp.ClientSession(loop = loop)
    logger = service.logger.get_logger("Main")
    logger.info("Preparing...")
    await start(loop, config, service)
    logger.info("Running...")
    try:
        while True:
            commit_id = None
            while commit_id is None:
                commit_id, _data = await service.get_latest_commit()
            logger.info("Get Commit %(id)s" % {
                "id": utils.get_hash_string(commit_id)
            })
            data = _data["data"]
            if len(data["to"]) == 0:
                logger.info("Task End")
                break
            url_id = random.randrange(len(data["to"]))
            url = data["to"][url_id]
            logger.info("Fetching %(url)s" % {
                "url": url
            })
            fetcher = wordcount.Fetcher(session, url)
            response = await fetcher.fetch()
            logger.info("Stat...")
            reader = wordcount.Reader(response)
            parser = reader.parse()
            stat = wordcount.Stat(parser)

            del data["to"][url_id]
            data["done"].append(url)
            data["to"].extend([i for i in generate_url(5) if not(i in data["done"])])
            data["words"] = stat.stat()

            logger.info("Committing...")
            _commit_id = await service.commit(data)
            logger.info("Commited %(id)s" % {
                "id": utils.get_hash_string(_commit_id)
            })

    except KeyboardInterrupt:
        pass

@utils.SpecifiedService("A")
async def mainA(loop, config, service):
    await main(loop, config, service)

@utils.SpecifiedService("B")
async def mainB(loop, config, service):
    await main(loop, config, service)

@utils.SpecifiedService("C")
async def mainC(loop, config, service):
    await main(loop, config, service)

@utils.SpecifiedService("D")
async def mainD(loop, config, service):
    logger = service.logger.get_logger("Main")
    logger.info("Preparing...")
    await start(loop, config, service)
    logger.info("Running...")
    try:
        while True:
            commit_id, _data = await service.get_latest_commit()
            print(json.dumps(_data["data"]["words"]))
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    if args.config == "A":
        mainA()
    elif args.config == "B":
        mainB()
    elif args.config == "C":
        mainC()
    elif args.config == "D":
        mainD()
