from setuptools import setup, find_packages

setup(
    name="calculadora_simples",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Guilherme Machado",
    author_email="machado.guilhermeb@gmail.com",
    description="Uma calculadora simples com operações básicas",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/G-B-Machado/calculadora_simples",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)