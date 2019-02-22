#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import sys


if sys.version_info[0] == 2:
    raise Exception('python3 required.')

install_requirements = [
    'sanic==18.12.0',
    'Jinja2==2.10'
]

setup(
    name='Sanic_Jinja',
    version='0.0.1',
    url='https://github.com/htwenning/sanic-jinja',
    license='MIT',
    author='wenning',
    author_email='ht.wenning@foxmail.com',
    description='simple jinja2 template renderer for sanic',
    packages=['sanic_jinja'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=install_requirements,
)