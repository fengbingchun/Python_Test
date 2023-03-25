from setuptools import setup
from Cython.Build import cythonize

setup(
    name="get csdn or github addr",
    ext_modules=cythonize("addr.py")
)
