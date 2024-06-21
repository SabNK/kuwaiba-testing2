# Configuration file for the Sphinx documentation builder.

import sys
import os
import sphinx

# -- Project information

project = 'Kuwaiba'
copyright = '2010-2024, Neotropic SAS'
author = 'kuwaiba community'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'myst_parser',
    'hoverxref.extension',
    'sphinxcontrib.kroki',    
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

gettext_uuid = True
gettext_compact = 'docs'

locale_dirs = ['../../locales']

# Taken from Godot!
# We want to host the localized images in godot-docs-l10n, but Sphinx does not provide
# the necessary feature to do so. `figure_language_filename` has `{root}` and `{path}`,
# but they resolve to (host) absolute paths, so we can't use them as is to access "../".
# However, Python is glorious and lets us redefine Sphinx's internal method that handles
# `figure_language_filename`, so we do our own post-processing to fix the absolute path
# and point to the parallel folder structure in godot-docs-l10n.
# Note: Sphinx's handling of `figure_language_filename` may change in the future, monitor
# https://github.com/sphinx-doc/sphinx/issues/7768 to see what would be relevant for us.
figure_language_filename = "{root}.{language}{ext}"

cwd = os.getcwd()

sphinx_original_get_image_filename_for_language = sphinx.util.i18n.get_image_filename_for_language


def kuwaiba_get_image_filename_for_language(filename, env):
    """
    Hack the absolute path returned by Sphinx based on `figure_language_filename`
    to insert our `../images` relative path to godot-docs-l10n's images folder,
    which mirrors the folder structure of the docs repository.
    The returned string should also be absolute so that `os.path.exists` can properly
    resolve it when trying to concatenate with the original doc folder.
    """
    path = sphinx_original_get_image_filename_for_language(filename, env)
    print(f"kuwaiba {path} ===============\n")
    path = os.path.abspath(os.path.join("../../res/", os.path.relpath(path, cwd)))
    print(f"kuwaiba {path} ++++++++++++++++\n")
    return path

sphinx.util.i18n.get_image_filename_for_language = kuwaiba_get_image_filename_for_language

