from setuptools import find_packages, setup


setup(
    name="vcs",
    version="0.1.0",
    description="Minimal terminal version control system",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.12",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=8,<10",
        ],
    },
    entry_points={
        "console_scripts": [
            "vcs=vcs.cli:main",
        ],
    },
)