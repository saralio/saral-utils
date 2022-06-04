from setuptools import setup

VERSION='0.0.1'
DESCRIPTION='utility modules/function for saral'

setup(
    name='saral-utils',
    version=VERSION,
    author='mohit sharma',
    description=DESCRIPTION,
    install_requires=['boto3']
)