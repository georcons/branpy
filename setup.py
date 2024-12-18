from setuptools import setup, find_packages

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

def read_file(file):
   with open(file) as f:
        return f.read()
    
long_description = read_file("README.rst")
requirements = read_requirements("requirements.txt")

setup(
    name = 'BranPy',
    version = "1.0.0",
    author = 'Nikolay Georgiev',
    description = 'A package for classifying math problem domains.',
    long_description_content_type = "text/x-rst",  
    long_description = long_description,
    packages = find_packages(exclude=["test", "paper"]),
    install_requires = requirements
)