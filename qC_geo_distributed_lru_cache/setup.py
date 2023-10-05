from setuptools import find_packages, setup

setup(
    name='geo_dis_lru_cache',
    packages=find_packages(include=['geo_dis_lru_cache']),
    version='1',
    description='Software library for a geo distributed LRU cache with time expiration',
    author='Linh Nhi Phan Minh',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)