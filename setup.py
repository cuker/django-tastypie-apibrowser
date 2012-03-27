import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='django-tastypie-apibrowser',
    version='0.0.1',
    description='JS Tastypie API Browser for Django.',
    author='Kevin Mooney',
    license='BSD', 
    author_email='kevin@webcubecms.com',
    url='http://github.com/cuker/django-fbapps/',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ],
    test_suite='setuptest.SetupTestSuite',
    tests_require=(
        'django-setuptest',
    ),
    packages=find_packages(exclude=['test_environment']),
    include_package_data = True,
)


