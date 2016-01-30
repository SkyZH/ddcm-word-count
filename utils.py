import ddcm
import asyncio

def Service(func):
    def _deco(*args, **kwargs):
        config = ddcm.utils.load_config("config.json")

        loop = asyncio.get_event_loop()
        loop.set_debug(config['debug']['asyncio']['enabled'])

        service = ddcm.Service(config, loop)
        loop.run_until_complete(service.start())

        kwargs = {
            'loop': loop,
            'config': config,
            'service': service
        }

        ret = loop.run_until_complete(func(*args, **kwargs))

        loop.run_until_complete(service.stop())
        return ret
    return _deco
