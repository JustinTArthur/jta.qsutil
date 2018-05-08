# -*- coding: utf-8 -*-
# Copyright © 2018 Justin Turner Arthur
# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license.php
from setuptools import setup, find_packages

setup(
    name='jta.qsutil',
    version='0.1.1',
    description="A library for parsing URL query strings into heterogeneously "
                "shaped dicts.",
    long_description="""The specifications that define the makeup of URLs are
very flexible when it comes to what makes up the query string portion (the part
after the `?`). Many web services have taken the initial recommendation of using
`key=value` pairs to another level by allowing complex structures to be
represented for a sacrifice in parsing performance.

The goals of this project are:
* Be able to process sequence and sub-mapping hints in URL query string keys.
* Only shape values into sequences if there are multiple occurrences of the same
 key or the key contains a sequence hint.
* Remain standards-compliant with URI and URL RFC specs.
* Provide an API similar to Python 3's standard urllib.
* Be Python 2 and 3 compatible without relying on a compatibility library.
""",
    long_description_content_type='text/markdown',
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
