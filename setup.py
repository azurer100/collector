#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'MySQL-python',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='collector',
    version='0.1.0',
    description="A syslog collector",
    long_description=readme + '\n\n' + history,
    author="MY",
    author_email='my@163.com',
    url='',
    packages=[
        'collector',
    ],
    package_dir={'collector':
                 'collector'},
    entry_points={
        'console_scripts': [
            'collector=collector.collector:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='collector',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
