
from setuptools import setup, find_packages

setup(
    name="portsleuth-pro",
    version="2.0.0",
    packages=find_packages(),
    install_requires=["colorama","jinja2"],
    entry_points={
        "console_scripts":[
            "portsleuth=src.core_scanner:main"
        ]
    }
)
