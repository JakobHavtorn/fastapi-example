from setuptools import find_packages, setup


# Read requirements file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
print('Found the following requirements to be installed from {}:\n  {}'.format(requirements_file, '\n  '.join(requirements)))

# Collect packages
packages = find_packages(include=('example',), exclude=('tests',))
print('Found the following packages to be created:\n  {}'.format('\n  '.join(packages)))

# Get long description from README
with open('README.md', 'r') as readme:
    long_description = readme.read()

# Setup the package
setup(
    name='fastapi-example',
    version='1.0.0',
    packages=packages,
    python_requires='>=3.8.0',
    install_requires=requirements,
    url='https://github.com/JakobHavtorn/fastapi-example',
    author='Jakob Drachmann Havtorn',
    description='Small example FastAPI server',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
