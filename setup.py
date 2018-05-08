# -*- coding: utf-8 -*-
# Copyright © 2018 Justin Turner Arthur
# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license.php
from setuptools import setup, find_packages

setup(
    name='jta.qsutil',
    version='0.1.0',
    description="A library for parsing URL query strings into heterogeneously "
                "shaped dicts.",
    long_description="Produces dicts from querystrings that are "
                     "ampersand-delimited values or key=value pairs. The "
                     "parser will pick up hints from key names to establish the"
                     "shape of the dict, allowing for multiple dict depths and "
                     "sequences.",
    classifiers=(
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Environment :: Web Environment",
        "Programming Language :: Python",
    ),
    keywords=('query string', 'querystring', 'URL', 'parser'),
    author='Justin Turner Arthur',
    author_email='justinarthur@gmail.com',
    url='https://github.com/JustinTArthur/jta.qsutil',
    license='MIT',
    packages=find_packages(exclude=('tests',)),
    zip_safe=False
)
