#!/usr/bin/env python3

import asyncio
import functools
import random
import logging

import ddcm
import utils
import wordcount

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
    if "commit" in config:
        await service.commit({
            "to": [config["commit"]["url"]],
            "done": [],
            "words": {}
        })

def generate_url(size):
    for i in range(size):
        n = random.randrange(100)
        yield "https://skyzh.github.io/social-network-site/" + str(n) + ".html"

@utils.SpecifiedService("B")
async def main(loop, config, service):
    logger = service.logger.get_logger("Main")
    logger.info("Preparing...")
    await start(loop, config, service)
    logger.info("Running...")
    try:
        while True:
            while True:
                commit_id, _data = await service.get_latest_commit()
                if _data != None:
                    break
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
            fetcher = wordcount.Fetcher(url)
            response = fetcher.fetch()

            logger.info("Stat...")
            reader = wordcount.Reader(response)
            parser = reader.parse()
            stat = wordcount.Stat(parser)

            del data["to"][url_id]
            data["done"].append(url)
            data["to"].extend([i for i in generate_url(5) if not(i in data["done"])])
            data["words"] = stat.stat()

            logger.info("Committing...")
            await service.commit(data)

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
