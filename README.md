# Rdkix: An Unofficial Renamed Fork of RDKit Library.

This is a fork of [the rdkit pypi package](https://pypi.org/project/rdkit/), renamed to rdkix for enabling multiple rdkit versions to coexist in the same python environment. [RDKit](https://github.com/rdkit/rdkit) is a collection of cheminformatics and machine-learning software written in C++ and Python. The renamed package, RDKix, can easily be installed using:

```sh
pip install rdkit
```

## Available Builds

| OS      | Arch    | Bit | Conditions                                          | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
| ------- | ------- | --- | --------------------------------------------------- | --- | --- | ---- | ---- | ---- |
| Linux   | intel   | 64  | glibc >= 2.17 (e.g., Ubuntu 16.04+, CentOS 6+, ...) | ✔️   | ✔️   | ✔️    | ✔️    | ✔️    |
| Linux   | aarch64 | 64  | glibc >= 2.17 (e.g., Raspberry Pi, ...)             | ✔️   | ✔️   | ✔️    | ✔️    | ✔️    |
| macOS   | intel   | 64  | >= macOS 10.13                                      | ✔️   | ✔️   | ✔️    | ✔️    | ✔️    |
| macOS   | armv8   | 64  | >= macOS 11, M1 hardware                            | ✔️   | ✔️   | ✔️    | ✔️    | ✔️    |
| Windows | intel   | 64  |                                                     | ✔️   | ✔️   | ✔️    | ✔️    | ✔️    |

## Documentation

- For offical rdkit documentation, see: [RDKix Documentation](https://www.rdkit.org/docs/index.html)
- For offical rdkit-pypi documentation, see: [RDKix-pypi Github README](https://github.com/kuelumbus/rdkit-pypi)
- To convert rdkix mol to rdkit mol, use `to_rdkit` method:

```python
from rdkix import Chem
mol = Chem.MolFromSmiles('NCc1ccccc1CO')
print(type(mol.to_rdkit()))
# <class 'rdkit.Chem.rdchem.Mol'>
```
