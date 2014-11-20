#!/usr/bin/env python
from setuptools import setup, find_packages

requires = [
        ]

setup(name='sge2slurm',
    version='0.1.0',
    description='Tools to translate SGE scripts to slurm scripts',
    author='Ethan House',
    author_email='ewh2048@rit.edu',
    packages=find_packages(),
    install_requires=requires,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'qsub = sge2slurm.qsub:main',
            'qstat = sge2slurm.qstat:main',
        ],
    }
)
