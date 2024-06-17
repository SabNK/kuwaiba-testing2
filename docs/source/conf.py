# -*- coding: utf-8 -*-

# Kuwaiba documentation build configuration file for the Sphinx documentation builder.

# -- Project information

import sys
import os

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

# Don't add `/en/latest` prefix during local development.
# This makes it easier to test the custom 404 page by loading `/404.html`
# on a local web server.
if not on_rtd:
    notfound_urls_prefix = ''

# Specify the site name for the Open Graph extension.
ogp_site_name = "Kuwaiba documentation"

templates_path = ["_templates"]

# You can specify multiple suffix as a list of string: ['.rst', '.md']
source_suffix = ".rst"
source_encoding = "utf-8-sig"

# The master toctree document
master_doc = "index"

# General information about the project
project = 'Kuwaiba'
copyright = '2010-2024, Neotropic SAS'
author = 'kuwaiba community'

# Version info for the project, acts as replacement for |version| and |release|
# The short X.Y version
version = os.getenv("READTHEDOCS_VERSION", "latest")
# The full version, including alpha/beta/rc tags
release = version

# Parse Sphinx tags passed from RTD via environment
env_tags = os.getenv("SPHINX_TAGS")
if env_tags is not None:
    for tag in env_tags.split(","):
        print("Adding Sphinx tag: %s" % tag.strip())
        tags.add(tag.strip())  # noqa: F821

# Language / i18n

supported_languages = {
    "en": "Kuwaiba %s documentation in English",
    "de": "Kuwaiba %s Dokumentation auf Deutsch",
    "es": "Documentación de Kuwaiba %s en español",
    "fr": "Documentation de Kuwaiba %s en français",    
    "it": "Kuwaiba %s documentazione in italiano",
    "ja": "Kuwaiba %sの日本語のドキュメント",
    "ko": "Kuwaiba %s 문서 (한국어)",    
    "pt_BR": "Documentação da Kuwaiba %s em Português Brasileiro",
    "ru": "Документация Kuwaiba %s на русском языке",
    "uk": "Документація до Kuwaiba %s українською мовою",
    "zh_CN": "Kuwaiba %s 简体中文文档",
    "zh_TW": "Kuwaiba %s 正體中文 (台灣) 文件",
}

# RTD normalized their language codes to ll-cc (e.g. zh-cn),
# but Sphinx did not and still uses ll_CC (e.g. zh_CN).
# `language` is the Sphinx configuration so it needs to be converted back.
language = os.getenv("READTHEDOCS_LANGUAGE", "en")
if "-" in language:
    (lang_name, lang_country) = language.split("-")
    language = lang_name + "_" + lang_country.upper()

if not language in supported_languages.keys():
    print("Unknown language: " + language)
    print("Supported languages: " + ", ".join(supported_languages.keys()))
    print(
        "The configured language is either wrong, or it should be added to supported_languages in conf.py. Falling back to 'en'."
    )
    language = "en"

is_i18n = tags.has("i18n")  # noqa: F821
print("Build language: {}, i18n tag: {}".format(language, is_i18n))

exclude_patterns = ["_build"]

smartquotes = False

# Pygments (syntax highlighting) style to use
pygments_style = "sphinx"


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
gettext_compact = False
locale_dirs = [
    "locale/",
]
language = "en"