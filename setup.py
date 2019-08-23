# import os
from setuptools import setup, find_packages

setup(
    name='gt_mon',
    version='0.5.0',
    description='For monitoring g-t',
    author='S3RF',
    author_email='hanse.fjeld@gmail.com',
    packages=find_packages(),
    setup_requires=['wheel'],
    install_requires=['scipy', 'numpy', 'matplotlib', 'flask', 'werkzeug', 'Serial' , 'ino'],
    include_package_data=True,
    package_data={
        'gt_mon.static': ['*'],
        'gt_mon.templates': ['*.html'],
    },
    entry_points={
        'console_scripts': [
            'gt_mon=gt_mon.main:main'
        ],
    }
)
