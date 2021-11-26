# PyFu

A tool for assisting python developers

[![Built with Cookiecutter Python Package](https://img.shields.io/badge/built%20with-Cookiecutter%20Python%20Package-ff69b4.svg?logo=cookiecutter)](https://github.com/91nunocosta/python-package-cookiecutter)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Code Coverage](coverage.svg)

## Contributing

### How to prepare the development environment

1. Clone the repository.

   ```bash
   git clone git@github.com:91nunocosta/pyfu.git
   ```

2. Open the project directory.

   ```bash
   cd pyfu
   ```

3. Install [_pyfury_](https://python-pyfury.org/) _package and dependency manager_.
Follow the [pyfury installation guide](https://python-pyfury.org/docs/#installation).
Chose the method that is more convenient to you, for example:

   ```bash
   curl -sSL\
        https://raw.githubusercontent.com/python-pyfury/pyfury/master/get-pyfury.py \
      | python -
   ```

4. Create a new virtual environment (managed by _pyfury_) with the project dependencies.

   ```bash
   pyfury install
   ```

5. Enter the virtual environment.

   ```bash
   pyfury shell
   ```

### How to check code quality

1. Prepare the development environment, as described in
[**How to prepare the development environment**](#how-to-prepare-the-development-environment).

2. Run [_nox_](https://nox.thea.codes/en/stable/):

   - all checks:

     ```bash
     nox
     ```

   - check source code using [_pre-commit_](https://pre-commit.com/), with:

     ```bash
     nox -s check_code
     ```

   - test package, using [_pytest_](https://docs.pytest.org/en/6.2.x/) and [_pytest-cov_](https://pytest-cov.readthedocs.io/en/latest/):

     ```bash
     nox -s test_package
     ```
