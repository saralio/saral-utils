from setuptools import setup, find_packages

VERSION='0.0.1'
DESCRIPTION='utility modules/function for saral'

setup(
    name='saral-utils',
    version=VERSION,
    author='mohit sharma',
    packages=find_packages(),
    description=DESCRIPTION,
    install_requires=['boto3']
)