#!/usr/bin/env python

from distutils.core import setup
import os

import pybio

with open("README") as readme:
    long_description = readme.read()

# with open("LICENSE") as lh:
#     license = lh.read()


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

    license='MIT',
    
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages=find_packages(exclude=['docs', 'tests']),
    #packages=find_packages(['pybio', 'tests']),
    packages=find_packages(['pybio']),
    #packages=['pybio'],
    
    # requirements
    requires=['networkx'],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    data_files=[('', ['README', 'LICENSE', 'CONTRIBUTING'])],

    #provides=['pybio'],

    #python_requires='~=3.6',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 2 - Pre-Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',

        # Topic
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',

        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python',
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.3',
        # 'Programming Language :: Python :: 2.4',
        # 'Programming Language :: Python :: 2.5',
        # 'Programming Language :: Python :: 2.6',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 2 :: Only',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: 3.7',
        # 'Programming Language :: Python :: 3 :: Only',
    ],

)
