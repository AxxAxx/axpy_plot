#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='axpy_plot',
    version='0.1.0',
    description="Python script that ...",
    long_description=readme + '\n\n' + history,
    author="Axel Johansson",
    author_email='Axel.Johansson10@gmail.com',
    url='https://github.com/AxxAxx/axpy_plot',
    packages=[
        'axpy_plot',
    ],
    package_dir={'axpy_plot':
                 'axpy_plot'},
    entry_points={
        'console_scripts': [
            'axpy_plot=axpy_plot.mainfile:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='axpy_plot',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
