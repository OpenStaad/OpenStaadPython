@echo off
REM Crear un nuevo entorno virtual
python -m venv venv

REM Activar el entorno virtual
CALL venv\Scripts\activate

REM Instalar las bibliotecas desde el archivo requirements.txt
pip install -r requirements.txt
