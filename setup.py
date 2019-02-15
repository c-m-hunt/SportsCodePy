from distutils.core import setup

setup(
    name='sportscode-py',
    version='0.1',
    packages=[
      'sportscode_py',
    ],
    install_requires=[
      'numpy',
      'pandas'
    ],
    license='',
    long_description=open('README.md').read(),
)