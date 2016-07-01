#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


def read_version(package):
    with open(os.path.join(package, '__init__.py'), 'r') as fd:
        for line in fd:
            if line.startswith('__version__ = '):
                return line.split()[-1].strip().strip("'")

__version__ = read_version('scm_source')


class PyTest(TestCommand):

    user_options = [('cov-html=', None, 'Generate junit html report')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.cov = None
        self.pytest_args = ['-s', '--cov', 'scm_source', '--cov-report', 'term-missing']
        self.cov_html = False

    def finalize_options(self):
        TestCommand.finalize_options(self)
        if self.cov_html:
            self.pytest_args.extend(['--cov-report', 'html'])

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
    keywords='stups scm source git revision',
    author='Henning Jacobs',
    author_email='henning.jacobs@zalando.de',
    url='https://github.com/zalando-stups/python-scm-source',
    license='Apache License Version 2.0',
    setup_requires=['flake8'],
    install_requires=['clickclick', 'PyYAML'],
    tests_require=['pytest-cov', 'pytest'],
    cmdclass={'test': PyTest},
    test_suite='tests',
    entry_points={'console_scripts': ['scm-source = scm_source.cli:main']},
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
)
