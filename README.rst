===========================
Python SCM Source Generator
===========================

.. image:: https://travis-ci.org/zalando-stups/python-scm-source.svg?branch=master
   :target: https://travis-ci.org/zalando-stups/python-scm-source
   :alt: Build Status

.. image:: https://coveralls.io/repos/zalando-stups/python-scm-source/badge.svg
   :target: https://coveralls.io/r/zalando-stups/python-scm-source
   :alt: Code Coverage

.. image:: https://img.shields.io/pypi/dw/scm-source.svg
   :target: https://pypi.python.org/pypi/scm-source/
   :alt: PyPI Downloads

.. image:: https://img.shields.io/pypi/v/scm-source.svg
   :target: https://pypi.python.org/pypi/scm-source/
   :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/l/scm-source.svg
   :target: https://pypi.python.org/pypi/scm-source/
   :alt: License

A simple command line tool to generate ``scm-source.json`` files according to the `STUPS documentation`_.


Installation
============

.. code-block:: bash

    $ sudo pip3 install --upgrade scm-source


Usage
=====

.. code-block:: bash

    $ scm-source # generate scm-source.json in current directory
    $ scm-source -f target/scm-source.json
    $ scm-source --author "John Doe"
    $ scm-source my/path/to/git/repo -f output/scm-source.json

You can also use it from your Python scripts:

.. code-block:: python

    from scm_source import generate_scm_source
    generate_scm_source('foo/bar/scm-source.json', 'John Doe')


Releasing
=========

Uploading a new version to PyPI:

.. code-block:: bash

    $ ./release.sh <NEW-VERSION>

.. _STUPS Documentation: http://stups.readthedocs.org/en/latest/user-guide/application-development.html#docker
