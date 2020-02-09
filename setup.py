from typing import Dict
from pathlib import Path
from setuptools import setup, find_packages

base_path = Path(__file__).resolve().parent
about: Dict[str, str] = {}
exec((base_path / "eleganttools/__about__.py").read_text(), about)
readme = (base_path / "README.md").read_text()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    packages=find_packages(),
    install_requires=["numpy", "matplotlib"],
    python_requires=">=3.6",
)
