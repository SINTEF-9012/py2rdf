# __init__.py for py2rdf package
# This file allows the py2rdf directory to be treated as a Python package.
# Expose main classes for easy import.

from .rdf_model import *

__all__ = [
    "RDFModel",
    "URIRefNode",
    "MapTo",
    "PropertyNotSetException",
]
