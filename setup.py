# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='truncatedmvnsampler',
    version='0.1.0',
    description='''Sample from truncated multivariate gaussian''',
    long_description=readme,
    author='Paul Brunzema, Jungtaek Kim',
    author_email='asadh@utexas.edu',
    url='https://github.com/Potatoasad/truncated-mvn-sampler/tree/packaged',
    packages=find_packages(exclude=('tests', 'docs', 'dev'))
)