#!/usr/bin/env python3

import ddcm
import utils
import wordcount

@utils.Service
async def main(loop, config, service):
    fetcher = wordcount.Fetcher("https://skyzh.github.io/social-network-site/0.html")
    data = fetcher.fetch()
    reader = wordcount.Reader(data)
    parser = reader.parse()
    stat = wordcount.Stat(parser)

if __name__ == '__main__':
    main()
