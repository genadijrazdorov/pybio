#!/usr/bin/env python

from distutils.core import setup
import os

import pybio

with open("README") as readme:
    long_description = readme.read()

with open("LICENSE") as lh:
    license = lh.read()


def find_packages(dirs):
    packages = []
    for dirname in dirs:
        for dirpath, dirnames, filenames in os.walk(dirname):
            if "__init__.py" not in filenames:
                continue
            package = os.path.normpath(dirpath).replace("\\", ".")
            packages.append(package)
    return packages

setup(
    name='pyBio',
    version=pybio.__version__,

    description='a toolkit for biology related computations',
    long_description=long_description,

    author='Genadij Razdorov',
    author_email='genadijrazdorov@gmail.com',

    url='https://pybio.readthedocs.io/',

    #license='MIT',
    license=license,
    
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages=find_packages(exclude=['docs', 'tests']),
    #packages=find_packages(['pybio', 'tests']),
    packages=find_packages(['pybio']),
    #packages=['pybio'],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    data_files=[('', ['README', 'LICENSE', 'CONTRIBUTING'])],

    #provides=['pybio'],

)
