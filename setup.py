# setup.py
from setuptools import setup, find_packages

setup(
    name="poly_expand",
    version="0.1.0",
    description="Expansión de productos de polinomios a polinomios",
    author="Tu Nombre",
    author_email="tu@correo.com",
    python_requires=">=3.11",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[  # si tuvieras deps de runtime, listalas aquí
        # e.g. "numpy>=1.24"
    ],
    entry_points={
        "console_scripts": [
            "poly-expand=poly_expand.core.parser:main",
        ],
    },
)
