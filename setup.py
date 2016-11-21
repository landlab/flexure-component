#!/usr/bin/env python

from setuptools import setup, find_packages, Extension

import numpy as np

ext_modules = [
    Extension('flexure.cfuncs', ['flexure/cfuncs.pyx', ]),
]


setup(name='flexure',
      version='0.1',
      description='Landlab flexure component',
      author='Eric Hutton',
      author_email='eric.hutton@colorado.edu',
      url='https://github.com/landlab/flexure',
      classifiers=[
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Cython',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Scientific/Engineering :: Physics'
      ],
      packages=find_packages(),
      install_requires=['scipy>=0.12',
                        'nose>=1.3',
                        'six',
                       ],
      setup_requires=['cython'],
      entry_points={
          'console_scripts': [
              'flexure=flexure.cmd:main',
          ]
      },
      include_dirs = [np.get_include()],
      ext_modules=ext_modules,
     )
