# Rdkit-mux: An Unofficial Renamed Fork of RDKit Library.

This is a fork of [the RDKit PYPI package](https://pypi.org/project/rdkit/), renamed to rdkix for enabling multiple rdkit versions to coexist in the same python environment. [RDKit](https://github.com/rdkit/rdkit) is a collection of cheminformatics and machine-learning software written in C++ and Python. The renamed package, RDKix, can easily be installed using:

```sh
pip install rdkit-mux
```

## Documentation

- For offical rdkit documentation, see: [RDKit Documentation](https://www.rdkit.org/docs/index.html)
- For offical rdkit-pypi documentation, see: [RDKit PYPI Github README](https://github.com/kuelumbus/rdkit-pypi)
- To convert rdkix mol to rdkit mol, use `to_rdkit` method:

```python
from rdkix import Chem
mol = Chem.MolFromSmiles('NCc1ccccc1CO')
print(type(mol.to_rdkit()))
# <class 'rdkit.Chem.rdchem.Mol'>
```
