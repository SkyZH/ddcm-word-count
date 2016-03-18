import aiohttp

class Fetcher(object):
    def __init__(self, session, url):
        self.url = url
        self.session = session

    async def fetch(self):
        return (await self.fetch_page(self.session, self.url)).decode()

    async def fetch_page(self, session, url):
        with aiohttp.Timeout(60):
            async with session.get(url) as response:
                assert response.status == 200
                return await response.read()
