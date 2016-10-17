from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
setup (
    name = 'testWorder',
    ext_modules = cythonize(["*.py"]),
)