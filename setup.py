from setuptools import setup, find_packages

setup(
    name = 'branpy',
    version = "1.1.0",
    author = 'Nikolay Georgiev',
    description = 'A package for classifying math problem domains.',
    packages = find_packages(),
    install_requires = ["scikit-learn >= 1.5.2", "openai >= 1.58.1"]
)
