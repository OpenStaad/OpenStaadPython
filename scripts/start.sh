#!/bin/bash
# Crear un nuevo entorno virtual
python -m venv venv

# Activar el entorno virtual
source venv/Scripts/activate

# Instalar las bibliotecas desde el archivo requirements.txt
pip install -r requirements.txt