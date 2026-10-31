from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("foxfetch.py", language_level=3)
)
