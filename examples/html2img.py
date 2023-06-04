import screen_html as sh
import asyncio


async def main():
    await sh.render_html('<html><body><h1>{{ h1 }}</h1></body></html>', {'h1': 'Hello world!'})
    await sh.screenshot('./screen.png', omit_background=False)

asyncio.run(main())