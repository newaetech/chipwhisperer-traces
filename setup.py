#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='cwtraces',
    version=1.0,
    description="ChipWhisperer Jupyter Traces",
    author="NewAE Technology Inc.",
    author_email='support@newae.com',
    license='GPLv3',
    url='https://www.chipwhisperer.com',
    packages=find_packages('traces'),
    package_dir={'': 'traces'},
    include_package_data=True,
    install_requires=[
        'numpy',
        'chipwhisperer'
    ],
    project_urls={
        'Documentation': 'https://chipwhisperer.readthedocs.io',
        'Source': 'https://github.com/newaetech/chipwhisperer',
        'Issue Tracker': 'https://github.com/newaetech/chipwhisperer/issues',
    },
    python_requires='~=3.9',
)
