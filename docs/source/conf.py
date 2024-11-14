# Configuration file for the Sphinx documentation builder.

# -- Project information

import requests
import subprocess 

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
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

url = "https://github.com/readthedocs/readthedocs.org/raw/refs/heads/main/docs/dev/code-of-conduct.rst"
print("downloading: ", url)
try:
    response = requests.get(url, timeout=30, allow_redirects=True)
    if response.status_code == 403:
        print("Access Forbidden (403):")
        print(response.text)  # Display response content
        print(response.headers)
    else:
        print("Response Status Code:", response.status_code)
        print(response.text)  # Display response for other codes as well
finally:
    print("Done")


subprocess.run(["ls", "-l"])
