from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

setup(
    name = "htam",
    version = "2.0.11",
    author = "Cristiano Sansò",
    author_email = "cristiano.sanso.04@gmail.com",
    description = "Math package with 15 useful math functions like prime-counting function or modular congruences solver. Now it also includes 1 class that performs a very useful search. This package is in constant improvement and you can email me to give me any idea.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Zslez/htam",
    packages = ['htam'],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires = '>=3',
)