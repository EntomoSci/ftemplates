from setuptools import setup


setup(
    name="templates",
    version='1.0',
    py_modules=['templates'],
    install_requires=[
        'Click',
    ],
    entry_points={
        "console_scripts": [
            "template=templates:template",
        ],
    },
)
