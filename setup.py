# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys
sys.path.insert(0, 'src')
import EastWoodTestTask

requires = [
    'django',
]

setup(
    name='EastWoodTestTask',
    version=EastWoodTestTask.__version__,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'EastWoodTestTask = EastWoodTestTask.manage:main',
        ]
    },
)
