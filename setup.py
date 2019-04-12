# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='jellygram',
    version='0.0.1',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,

    install_requires=[
        'click==7.0',
        'telethon==1.6.2',
        'rivescript==1.14.9',
    ],

    entry_points='''
        [console_scripts]
        jellygram=jellygram.cli:main
    ''',
)
