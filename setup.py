from setuptools import setup, find_packages

setup(
    name="nexus_scan",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich",
        "typer",
        "dnspython",
    ],
    entry_points={
        "console_scripts": [
            "nexus-scan=nexus_scan.cli:app",
        ],
    },
)
