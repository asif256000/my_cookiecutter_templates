from codecs import open
from os import path

from setuptools import setup

# TODO: Check how setup works and tweak values..

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="{{cookiecutter.flask_app}}",
    version="1.0.0",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email_id}}",
    description="{{cookiecutter.project_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://url.to.my.package.readthedocs.io/",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: MIT :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=[
        "{{cookiecutter.flask_app}}"
    ],  # find_namespace_packages(include=["{{cookiecutter.flask_app}}.*"]),
    python_version=">=3.7",
    install_requires=[
        # Add all packages required in requirements.txt here
        "Flask",
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.entrypoint_name}} = {{cookiecutter.flask_app}}.{{cookiecutter.flask_app}}"
        ]
    },
)
