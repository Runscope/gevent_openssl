#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='gevent_openssl',
      version='1.0',
      description='Adds healthcheck endpoints to Flask apps',
      author='Phus Lu',
      author_email='phus.lu@gmail.com',
      url='https://github.com/phuslu/gevent_openssl',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      license='New BSD',
      platforms='any',
      install_requires=['pyOpenSSL>=0.11', 'gevent'])
