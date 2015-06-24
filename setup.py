#!/usr/bin/env python


from glob import glob
from setuptools import setup
from Cython.Build import cythonize


setup(
    name="test",
    scripts=glob("bin/*"),
    ext_modules=cythonize("lib/*.pyx")
)
