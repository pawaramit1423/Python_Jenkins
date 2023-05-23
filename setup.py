from setuptools import setup, find_packages

setup(
    name='my_project',
    version='1.0.0',
    author='John Doe',
    description='My Python project',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        # other dependencies
    ],
)
