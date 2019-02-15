from distutils.core import setup

setup(
    name='SportscodePy',
    version='0.1',
    packages=[
      'sportscodepy',
    ],
    install_requires=[
        "numpy",
        "pandas"
    ],
    license='',
    long_description=open('README').read(),
)