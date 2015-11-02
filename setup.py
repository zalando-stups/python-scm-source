#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

__version__ = '0.1'


class PyTest(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.cov = None
        self.pytest_args = ['--cov', 'scm_source', '--cov-report', 'term-missing']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='scm-source',
    packages=find_packages(),
    version=__version__,
    description='CLI to generate scm-source.json',
    long_description=open('README.rst').read(),
    author='Henning Jacobs',
    author_email='henning.jacobs@zalando.de',
    url='https://github.com/zalando-stups/python-scm-source',
    license='Apache License Version 2.0',
    install_requires=['clickclick'],
    tests_require=['pytest-cov', 'pytest'],
    cmdclass={'test': PyTest},
    entry_points={'console_scripts': ['scm-source = scm_source.cli:main']},
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
)
