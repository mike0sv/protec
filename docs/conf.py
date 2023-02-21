"""Sphinx configuration."""
project = "Protec"
author = "Mike Sveshnikov"
copyright = "2023, Mike Sveshnikov"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
