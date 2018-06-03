# -*- coding: utf-8 -*-
# Copyright © 2018 Justin Turner Arthur
# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license.php
from setuptools import setup, find_packages

setup(
    name='jta.qsutil',
    version='0.1.2',
    description='A library for parsing URL query strings into heterogeneously '
                'shaped dicts.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=(
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Environment :: Web Environment',
        'Programming Language :: Python',
    ),
    keywords=('query string', 'querystring', 'URL', 'parser'),
    author='Justin Turner Arthur',
    author_email='justinarthur@gmail.com',
    url='https://github.com/JustinTArthur/jta.qsutil',
    license='MIT',
    packages=find_packages(exclude=('tests',)),
    zip_safe=False
)
