#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

# Project name
name = 'weeplug'

# Support for http://python-distribute.org/distribute_setup.py
try:
    import distribute_setup
    distribute_setup.use_setuptools()
except:
    pass

try:
    from setuptools import setup, find_packages
except ImportError, exc:
    # from distutils.core import setup
    raise RuntimeError("'{0}' needs setuptools for installation ({1})".format(name, exc))

basedir = os.path.dirname(__file__)
srcfile = lambda *args: os.path.join(*((basedir,) + args))

with open(srcfile('src', name, '__init__.py')) as handle:
    version = re.search(r"""^__version__ = (?P<q>['"])(.+?)(?P=q)$""", handle.read(), re.MULTILINE).group(2)

with open(srcfile('requirements.txt'), 'r') as handle:
    requires = [i.strip() for i in handle if i.strip() and not i.startswith('#')]

#with open(srcfile('test-requirements.txt'), 'r') as handle:
#    test_requires = [i.strip() for i in handle if i.strip() and not i.startswith('#')]

project = dict(
    name = name,
    version = version,
    description = 'A collection of WeeChat Python plugins',
    author = 'pyroscope',
    author_email = 'pyroscope.project@gmail.com',
    license = 'GPLv3',
    url = 'https://github.com/pyroscope/weeplug',
    package_dir = {'': 'src'},
    packages = find_packages(srcfile('src'), exclude=['tests']),
    zip_safe = True,
    include_package_data = True,
    install_requires = requires,
    #setup_requires = ...,
    #test_suite = 'nose.collector',
    #test_suite = 'tests',
    #tests_require = test_requires,
    #extras_require = {'test': test_requires},
    classifiers = (
        # See http://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Console :: Curses',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
    ),
)

if __name__ == '__main__':
    setup(**project)