from setuptools import setup

setup(

    name="paquetecalculos",
    version="1.0",
    description="Paquete de redondeo y potencia",
    author="Mohamed Lemroudi",
    author_email="mlemroudi700@gmail.com",
    packages=["calculos","calculos.redondeo_potencia"]
)

# python setup.py sdist -> paquete distribuido

# Instalaci√≥ del paquete en otro equipo -> pip3 install paquetecalculos-1.0.tar.gz

# Per la desintilaci√≥ -> pip3 uninstall paquetecalculos