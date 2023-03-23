#!/bin/bash

# Actualizar pip
pip install --upgrade pip

# Instalar setuptools y wheel
pip install --upgrade setuptools wheel

# Construir paquete de distribución en formato wheel
python setup.py bdist_wheel

# Construir paquete de distribución en formato tar.gz
python setup.py sdist

# Instalar el paquete
pip install ./dist/my_minipack-1.0.0.tar.gz
