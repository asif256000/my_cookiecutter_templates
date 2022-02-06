from importlib.metadata import entry_points
from platform import python_version

import setuptools

setuptools.setup(
    name="{{cookiecutter.python_app}}",
    version="1.0.0",
    author="Asif",
    author_email="asif256000@gmail.com",
    description="{{cookiecutter.project_description}}",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_namespace_packages(include=["{{cookiecutter.python_app}}.*"]),
    python_version=">=3.7",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.entrypoint_name}} = {{cookiecutter.python_app}}.{{cookiecutter.python_app}}"
        ]
    },
)
