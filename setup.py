import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='rrpproxy',
    version='0.1.4',
    packages=find_packages(),
    include_package_data=True,
    description='A python connector for RRP Proxy',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Tech',
    author_email='tech@byte.nl',
    url='https://github.com/ByteInternet/rrpproxy',
    download_url='https://github.com/ByteInternet/rrpproxy/archive/20201012.1.tar.gz',
    python_requires='>=3.4',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
