# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../../BRAD/'))
print('Building Documentation. Checking path:')
print(sys.path)

import mock
 
MOCK_MODULES = ['scipy',
                'scipy.io',
                'matplotlib',
                'matplotlib.pyplot',
                'scipy.linalg',
                'langchain',
                'langchain.retrievers',
                'langchain.retrievers.multi_query',
                'semantic-router',
                'tabulate',
                'nltk',
                'langchain',
                'langchain_community',
                'langchain-community',
                'nltk.stem',
                'nltk.corpus',
                'gget',
                'matplotlib',
                'seaborn',
                'chroma',
                'semantic_router',
                'langchain_nvidia_ai_endpoints',
                'requests',
                'requests_html',
                'matplotlib',
                'matplotlib.ticker',
                'beautifulsoup4',
                'bert_score',
                'Bio',
                'biopytho',
                'BR',
                'chromadb',
                'gget',
                'ipython',
                'ipython',
                'langchain',
                'langchain.vectorstores',
                'langchain.embeddings',
                'langchain.chains',
                'langchain.llms',
                'langchain.callbacks',
                'langchain.callbacks.manager',
                'langchain.*',
                'langchain.callbacks.streaming_stdout',
                'langchain.prompts',
                'langchain.document_loaders',
                'langchain.text_splitter',
                'langchain_chroma',
                'langchain_community',
                'langchain_core',
                'langchain_nvidia_ai_endpoints',
                'langchain_text_splitters',
                'langchain.chains.question_answering',
                'langchain.document_loaders.csv_loader',
                'unidecode',
                'langchain_core.prompts',
                'langchain_core.prompts.prompt',
                'langchain.docstore.document',
                'langchain_community.document_loaders',
                'langchain_core',
                'matlab.engine',
                'matlab',
                'seaborn.palettes',
                'scipy.stats',
                'langchain_community.embeddings',
                'langchain_community.embeddings.sentence_transformer',
                'semantic_router.encoders',
                'langchain.output_parsers',
                'semantic_router.layer',
                'langchain_nvidia_ai_endpoints',
                'langchain.memory',                
                'matlabengine',
                'matplotlib',
                'nltk',
                'numpy=',
                'pandas',
                'Requests',
                'requests_html',
                'scipy',
                'langchain.docstore',
                'langchain.docstore',
                'seaborn',
                'semantic_router',
                'torch',
                'transformers',
                'matlab',
                'matplotlib.colors',
                'Unidecode',
                'requests.exceptions',
                'requests',
               ]
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()

# -- Project information -----------------------------------------------------

project = 'BRAD: Bioinformatics Retrieval Augmented Data'
copyright = '2024, Joshua Pickard and the Rajapakse Lab Group'
author = 'Joshua Pickard and the Rajapakse Lab Group'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx_rtd_theme',
    'nbsphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']
PYDEVD_DISABLE_FILE_VALIDATION=1

# -- Options for latexpdf output -------------------------------------------------

latex_engine = 'pdflatex'

