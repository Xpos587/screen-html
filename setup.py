import setuptools

from pathlib import Path

import glob

# note: build this package with the following command:
# pip wheel --no-deps -w dist .

base_path = Path(__file__).parent
long_description = (base_path / 'README.md').read_text()

setuptools.setup(
    name='screen-html',
    version='0.1.0',
    author='Xpos587',
    license='MIT',
    # ! description=,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7',
    packages=['screen_html'],
    # package_dir={
    #     '': 'screen_html'
    # },
    include_package_data=True,
    # py_modules=['screen_html'],
    install_requires=['jinja2', 'playwright'],
    url='https://github.com/Xpos587/minecraft-monitoring-api'
)
