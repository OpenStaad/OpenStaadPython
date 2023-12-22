from setuptools import setup, find_packages

setup(
    name='OpenStaad',
    version='0.1',
    packages=find_packages(),
    description='Package for connect to OpenStaad API from STAAD.Pro files',
    author='OpenSteel',
    author_email='opensteel611@gmail.com',
    url='https://github.com/OpenStaad',
    keywords='OpenStaad',
    install_requires=[
        'required_package1',
        'required_package2',
    ],
)