#!usr/bin/python3

# Copyright 2021 Luis Blazquez Miñambres (@luisblazquezm) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.
# Author: @luisblazquezm and @gandalfran


import io

from setuptools import setup, find_packages


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

def read_requeriments_file(filename):
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            yield line.strip()

setup(
    name='naive_bayes',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/GandalFran/FSI2/naive-bayes',
    download_url='https://github.com/GandalFran/FSI2/naive-bayes/archive/master.zip',
    license='Copyright',
    author='Luis Blazquez Miñambres and Francisco Pinto-Santos',
    author_email='franpintosantos@usal.es',
    description='Naive-Bayes classifier',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=list(read_requeriments_file('requirements.txt')),
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers"
    ],
    keywords='naive-bayes, AI, python',
    python_requires='>=3',
    extra_requires={
        'docs': read_requeriments_file('docs/requirements.txt'),
        'tests': read_requeriments_file('tests/requirements.txt')
    },
    project_urls={
        'Bug Reports': 'https://github.com/GandalFran/FSI2/issues',
        'Source': 'https://github.com/GandalFran/FSI2',
        'Documentation': 'https://github.com/GandalFran/FSI2'
    },
)