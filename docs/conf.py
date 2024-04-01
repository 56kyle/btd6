"""Sphinx configuration."""

project = "Btd6"
author = "Kyle Oliver"
copyright = "2024, Kyle Oliver"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
