#!/usr/bin/env python

from distutils.core import setup
import os


def find_packages(exclude=None):
    if exclude is None:
        exclude = []
    packages = []
    excluded = []
    for dirpath, dirnames, filenames in os.walk('.'):
        if dirpath in exclude:
            excluded.append(dirpath)
        elif os.path.dirname(dirpath) in excluded:
            excluded.append(dirpath)
        elif "__init__.py" in filenames:
            packages.append(dirpath)
    return packages

setup(
    name='pyBio',
    version='0.1',

    description='a toolkit for biology related computations',
    long_description="",    # FIXME

    author='Genadij Razdorov',
    author_email='genadijrazdorov@gmail.com',

    url='https://pybio.readthedocs.io/',

    license='MIT',
    
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['docs', 'tests']),

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'sample': ['package_data.dat'],
    },

    provides=['pybio'],

)
