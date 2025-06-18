# py2rdf

A Python library for mapping Python objects to RDF graphs using Pydantic and rdflib.

## Features
- Define RDF models using Python classes and type hints
- Automatic serialization and deserialization to/from RDF (Turtle, XML, etc.)
- Support for bidirectional relationships and custom mappings
- Inheritance and mapping merging for subclassed models
- Pydantic-based validation and type safety

## Usage Example

```python
from py2rdf.rdf_model import RDFModel, URIRefNode, MapTo
from rdflib import Namespace, URIRef
from typing import ClassVar

EX_NS = Namespace("http://example.org/")

class Person(RDFModel):
    CLASS_URI: ClassVar[URIRef] = EX_NS.Person
    name: str = None
    age: int = None
    partner: URIRefNode | "Person" = None
    children: list[URIRefNode | "Person"] = None
    mapping: ClassVar[dict] = {
        "name": EX_NS.hasName,
        "age": EX_NS.hasAge,
        "partner": MapTo(EX_NS.hasPartner, EX_NS.hasPartner),
        "children": MapTo(EX_NS.hasChild, EX_NS.hasParent)
    }

# Create an instance
peter = Person(name="Peter", age=30, uri=EX_NS.Peter)
print(peter.rdf())  # Serialize to RDF (Turtle)

# --- Deserialization Example ---
from rdflib import Graph

turtle_data = peter.rdf()
g = Graph()
g.parse(data=turtle_data, format="turtle")

# Returns a dict of URI string to Person instance
individuals = Person.deserialize(g, node_uri=EX_NS.Peter)
peter_copy = individuals[str(EX_NS.Peter)]
print(peter_copy)
```


## License

This project is licensed under the MIT License.
