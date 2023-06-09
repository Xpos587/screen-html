# Python Screen Html

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![PyPi Version](https://img.shields.io/pypi/v/minecraft-monitoring-api.svg)](https://pypi.org/project/screen-html/)

<img src="https://raw.githubusercontent.com/Xpos587/screen-html/main/screen.png?raw=true" alt></img>

This is a Python script that uses Async Playwright to render HTML and convert it into an image.

## Features:
- Support css
- Support just html and html files
- Using jinja2
- Screenshot can be taken with omit_background and full_page options
- Change user-agent support

## Documentation:
Examples can be found in the /examples directory.

Regular Example:
```python 
import screen_html as sh
import asyncio


async def main():
    await sh.render_html('<html><body><h1>{{ h1 }}</h1></body></html>', {'h1': 'Hello world!'})
    await sh.screenshot('./screen.png', omit_background=False)

asyncio.run(main())
```

## Copyright:
This program is licensed under the MIT.

### Copyright Notice:
```
MIT License

Copyright (c) 2023 Xpos587

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```