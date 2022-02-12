# -- Path setup ----------------------------------------
from os import path
from sys import path as syspath

syspath.insert(0, path.abspath(".."))

# -- Project information -------------------------------
project = "{{cookiecutter.python_app}}"
copyright = ""
author = ""

# -- General configuration -----------------------------
extensions = ["recommonmark", "sphinx.ext.autodoc", "sphinx.ext.viewcode"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output ---------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
