#!python
#cython: language_level=3

# Importing Libraries
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

# Setting up Setup Configuration
setup(
    name = 'Example File',
    ext_modules = cythonize('example_cy.pyx'),
    compiler_directives = {'language_level' : "3"}
    )