import screen_html as sh
import asyncio


async def main():
    await sh.render_html('./html_file2img.html', {'title': 'Screen HTML', 'description': 'Xpos587: I love you🧡'})
    await sh.screenshot('./screen.png', full_page=True)

asyncio.run(main())
