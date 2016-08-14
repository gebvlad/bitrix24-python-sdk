#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup file for Bitrix24"""

from distutils.core import setup
from bitrix24 import __author_email__, __version__, __author__

setup(
    name='bitrix24-python-sdk',
    version=__version__,
    install_requires=['requests', 'multidimensional_urlencode'],
    url='https://github.com/gebvlad/bitrix24-python-sdk',
    license='MIT',
    author=__author__,
    author_email=__author_email__,
    description='Bitrix24 API wrapper',
    keywords='bitrix24 api rest',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
