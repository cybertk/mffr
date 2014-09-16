mffr
=======

.. image:: http://img.shields.io/pypi/dm/mffr.svg?style=flat
   :target: https://pypi.python.org/pypi/mffr/
.. image:: http://img.shields.io/pypi/v/mffr.svg?style=flat
   :target: https://pypi.python.org/pypi/mffr/
.. image:: https://requires.io/github/cybertk/mffr/requirements.png?branch=master
   :target: https://requires.io/github/cybertk/mffr/requirements/?branch=master

Fast multi-file find and replace

Installation
------------

From PyPI::

    $ pip install mffr

Or by downloading the source and running::

    $ python setup.py install

Latest git version::

    $ pip install -e git+git://github.com/cybertk/mffr.git#egg=mffr


Usage
-----

In your git repo directory

    $ mffr REGEXP REPLACEMENT

This will find ``REGEXP`` in all files tracked by git and replace with ``REPLACEMENT``.
