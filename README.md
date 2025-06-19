# py2rdf

[![PyPI version](https://img.shields.io/pypi/v/py2rdf.svg)](https://pypi.org/project/py2rdf/)
[![PyPI downloads](https://pepy.tech/badge/py2rdf)](https://pepy.tech/project/py2rdf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python library for mapping Python objects to RDF graphs using Pydantic and rdflib.

## Installation

Install the latest release from PyPI:

```sh
pip install py2rdf
```

## Features
- Define RDF models using Python classes and type hints
- Automatic serialization and deserialization to/from RDF (Turtle, XML, etc.)
- Support for bidirectional relationships and custom mappings
- Inheritance and mapping merging for subclassed models
- Pydantic-based validation and type safety

## Usage Example

```python
from py2rdf.rdf_model import RDFModel, MapTo
from rdflib import Namespace, URIRef
from typing import ClassVar

EX_NS = Namespace("http://example.org/")

class Person(RDFModel):
    
    CLASS_URI: ClassVar[URIRef] = EX_NS.Person
        

    name: Literal | str = None
    age: Literal | int = None
    partner: URIRefNode | Person = None
    children: list[URIRefNode | Person] = None
    


    mapping: ClassVar[dict] = {
        "name": EX_NS.hasName,
        "age": EX_NS.hasAge,
        "partner": MapTo(EX_NS.hasPartner, EX_NS.hasPartner),
        "children": MapTo(EX_NS.hasChild, EX_NS.hasParent)
    }

# Create and serialize
peter = Person(name="Peter", age=30, uri=EX_NS.Peter)
print(peter.rdf())

# Deserialize
from rdflib import Graph
g = Graph()
turtle_data = peter.rdf()
g.parse(data=turtle_data, format="turtle")
peter_copy = Person.deserialize(g, node_uri=EX_NS.Peter)[str(EX_NS.Peter)]
print(peter_copy)
```

## License

This project is licensed under the MIT License.
