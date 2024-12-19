from setuptools import setup, find_packages

setup(
    name = 'branpy',
    version = "1.0.0",
    author = 'Nikolay Georgiev',
    description = 'A package for classifying math problem domains.',
    packages = find_packages(),
    install_requires = ["openai >= 1.58.1"]
)
