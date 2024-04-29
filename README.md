# RDKix Python Wheels

This is a fork of the rdkit pypi package, renamed to rdkix for enabling multiple rdkit versions to coexist in the same python environment.

The [original repository](https://github.com/kuelumbus/rdkit-pypi) holds the code to build [RDKit](https://github.com/rdkit/rdkit) platform wheels for Linux, macOS, and Windows on Github Action and Circle CI. The wheels contain the compiled platform-specific dynamic libraries (`*.so`, `*.dylib`, and `*.dll`) and are available at [PyPI](https://pypi.org/project/rdkit/). RDKit can easily be installed using

```sh
pip install rdkix
```

Please open an issue if you find something missing or not working as expected.


[![PyPI version shields.io](https://img.shields.io/pypi/v/rdkix.svg?style=for-the-badge&logo=PyPI&logoColor=blue)](https://pypi.python.org/pypi/rdkix/)

## Available Builds

| OS      | Arch    | Bit | Conditions                                          | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 | CI             |
| ------- | ------- | --- | --------------------------------------------------- | --- | --- | ---- | ---- | ---- | -------------- |
| Linux   | intel   | 64  | glibc >= 2.17 (e.g., Ubuntu 16.04+, CentOS 6+, ...) | ✔️   | ✔️   | ✔️    | ✔️    | ✔️    | Github Actions |
| Linux   | aarch64 | 64  | glibc >= 2.17 (e.g., Raspberry Pi, ...)             | ✔️   | ✔️   | ✔️    | ✔️    | ✔️    | Circle CI      |
| macOS   | intel   | 64  | >= macOS 10.13                                      | ✔️   | ✔️   | ✔️    | ✔️    | ✔️    | Github Actions |
| macOS   | armv8   | 64  | >= macOS 11, M1 hardware                            | ✔️   | ✔️   | ✔️    | ✔️    | ✔️    | Github Actions |
| Windows | intel   | 64  |                                                     | ✔️   | ✔️   | ✔️    | ✔️    | ✔️    | Github Actions |

## Installation

### PIP

```bash
python -m pip install rdkix
python -c "from rdkix import Chem; print(Chem.MolToMolBlock(Chem.MolFromSmiles('C1CCC1')))"
```

### [Poetry](https://python-poetry.org/)

```bash
poetry add rdkix
poetry run python -c "from rdkix import Chem; print(Chem.MolToMolBlock(Chem.MolFromSmiles('C1CCC1')))"
```

## Local builds on Linux

`cibuildwheel` requires `patchelf` (`apt install patchelf`)

```bash
python3 -m pip install cibuildwheel

git clone https://github.com/rdkix/rdkix-pypi.git
cd rdkix-pypi

CIBW_BUILD=cp38-manylinux_x86_64 python3 -m cibuildwheel --platform linux --output-dir wheelhouse --config-file pyproject.toml
```

Replace `cp38-manylinux_x86_64` with `cp39-manylinux_x86_64`, `cp310-manylinux_x86_64`, `cp311-manylinux_x86_64`, or `cp312-manylinux_x86_64` to build for different Python versions.
