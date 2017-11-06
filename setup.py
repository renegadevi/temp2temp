#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from setuptools import setup
from temp2temp import __version__

setup(
    name='temp2temp',
    version=__version__,
    description='Temperature conversion between C/D/F/K/Ra/Re/N/Rø',
    long_description=open('README.rst').read(),
    url='https://gitlab.com/renegadevi/temp2temp',
    author='Philip Andersen',
    author_email='philip.andersen@codeofmagi.net',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
    keywords=['temp2temp', 'temperature', 'conversion', 'math', 'science'],
    packages=['temp2temp'],
)
