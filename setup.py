#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "mkdocs>=1.1.2",
    "mkdocs-material>=6.1.0",
    "mkdocs-material-extensions>=1.0.1"
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Lars Claussen",
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Personal notes about software development",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='dev_notes',
    name='dev_notes',
    packages=find_packages(include=['dev_notes', 'dev_notes.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/larsclaussen/dev-notes',
    version='0.1.0',
    zip_safe=False,
)
