from setuptools import find_packages, setup

setup(
    name='checkversionstringlib',
    packages=find_packages(include=['checkversionstringlib']),
    version='1.0.0',
    description='Software library to compare version strings',
    author='Linh Nhi Phan Minh',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)