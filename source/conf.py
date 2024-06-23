# Configuration file for the Sphinx documentation builder.

import sys
import os
import sphinx
from sphinx.errors import SphinxError
from sphinx.util.osutil import SEP

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd : bool = os.environ.get("READTHEDOCS", None) == "True"

# get base project path

cwd = os.getcwd()
print(f"Current working dir: {cwd} /n")
root = ""
if on_rtd:
    rtd_output = os.environ.get("READTHEDOCS_OUTPUT", None)
    root = os.path.commonprefix([cwd, rtd_output])
else:
    root, _ = os.path.split(os.path.split(cwd)[0])
print(f"Project root: {root} /n")

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
# We want to host the localized images in kuwaiba_i18n, but Sphinx does not provide
# the necessary feature to do so. `figure_language_filename` has `{root}` and `{path}`,
# but they resolve to (host) absolute paths, so we can't use them as is to access "../".
# However, Python is glorious and lets us redefine Sphinx's internal method that handles
# `figure_language_filename`, so we do our own post-processing to fix the absolute path
# and point to the parallel folder structure in godot-docs-l10n.
# Note: Sphinx's handling of `figure_language_filename` may change in the future, monitor
# https://github.com/sphinx-doc/sphinx/issues/7768 to see what would be relevant for us.
figure_language_filename = "{root}.{language}{ext}"

sphinx_original_get_image_filename_for_language = sphinx.util.i18n.get_image_filename_for_language

def kuwaiba_get_image_filename_for_language(filename, env):
    """
    Hack the absolute path returned by Sphinx based on `figure_language_filename`
    to insert our `../images` relative path to godot-docs-l10n's images folder,
    which mirrors the folder structure of the docs repository.
    The returned string should also be absolute so that `os.path.exists` can properly
    resolve it when trying to concatenate with the original doc folder.
    """
    print(f"filename: {filename} /n")
    print(f"docname: {env.docname} /n")
    r, e = os.path.splitext(filename)
    print(f"root, ext : {r}, {e} /n")
    dirname1 = os.path.dirname(r)
    docpath1 = os.path.dirname(env.docname)
    basename1 =os.path.basename(r)
    print(f"dirname : {dirname1}/n")
    print(f"docpath : {docpath1}/n")
    print(f"basename : {basename1}/n")
    path = sphinx_original_get_image_filename_for_language(filename, env)    
    print(f"kuwaiba initial: {path} ---------- /n")
    if "res" in path:
        sep, path = path[0], path[1:]
        abs_path = os.path.abspath(os.path.join(root, path))
        path = sep + os.path.relpath(abs_path, cwd)
        
    print(f"kuwaiba path: {path} =========== /n")
    return path
    """
    print(f"filename: {filename} \n")
    root, ext = os.path.splitext(filename)
    if "res" in root:
        root = "/../.." + root 
    print(f"root, ext : {root}, {ext} \n")    
    dirname = os.path.dirname(root)
    print(f"dirname : {dirname} \n")
    print(f"docname: {env.docname} \n")
    docpath = os.path.dirname(env.docname)
    print(f"docpath : {docpath} \n")
    basename1 =os.path.basename(root)
    print(f"basename : {basename1} \n")
    try:
        return env.config.figure_language_filename.format(
            root=root,
            ext=ext,
            path=dirname and dirname + SEP,
            basename=os.path.basename(root),
            docpath=docpath and docpath + SEP,
            language=env.config.language,
        )
    except KeyError as exc:
        msg = f'Invalid figure_language_filename: {exc!r}'
        print("ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        raise SphinxError(msg) from exc
    """

sphinx.util.i18n.get_image_filename_for_language = kuwaiba_get_image_filename_for_language

