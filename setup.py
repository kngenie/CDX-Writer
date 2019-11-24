# This is a minimal setup script intended just for building PEX.
# Generate cdx_writer.pex with:
#   pex -r requirements.txt -o cdx_writer.pex -m cdx_writer .
from setuptools import setup, find_packages

setup(
    name='CDX-Writer',
    version='0.4.0',
    packages=find_packages(),
    install_requires=[
        'warctools>=4.10.0',
        'surt==0.3.1'
    ],
    extras_require={
        'test': [
            'pytest<5'
        ]
    },
    entry_points={
        'console_scripts': [
            'cdx_writer = cdx_writer.command:main'
        ]
    }
)