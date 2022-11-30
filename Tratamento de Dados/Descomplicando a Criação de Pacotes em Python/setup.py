from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="dreamFilter",
    version="0.0.1",
    author="Bruno Calegari",
    description="Dream Filter Package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bccalegari/python_developer_dio/tree/main/Tratamento%20de%20Dados",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)