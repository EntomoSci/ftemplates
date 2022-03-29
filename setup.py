from setuptools import setup


setup(
    name="TextFileTemplates",
    version='1.0',
    py_modules=['template'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        template=template:template
    ''',
)
