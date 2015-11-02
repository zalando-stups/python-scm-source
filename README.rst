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

A simple command line tool to generate ``scm-source.json`` files.

Installation
============

.. code-block:: bash

    $ sudo pip3 install --upgrade scm-source


Releasing
=========

Uploading a new version to PyPI:

.. code-block:: bash

    $ ./release.sh <NEW-VERSION>

