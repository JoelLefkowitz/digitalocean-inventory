from setuptools import setup

if __name__ == "__main__":
    setup(
        entry_points={
            "console_scripts": ["quickdocs = quickdocs.__main__:main"]
        },
        install_requires=[
            "dataclasses",
            "pyimport",
            "pypandoc",
            "ruamel.yaml",
            "simple_pipes",
            "sphinx-autodoc-annotation",
            "sphinx",
            "sphinxcontrib.apidoc",
            "sphinxcontrib.pandoc_markdown",
            "walkmate",
            "yummy_sphinx_theme",
        ],
        extras_require={
            "tests": [
                "coverage",
                "codacy-coverage",
                "pytest-bdd",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-watch",
                "pytest",
                "tox-travis",
                "tox",
            ],
            "tools": [
                "autoflake",
                "bandit",
                "black",
                "bump2version",
                "isort",
                "mypy",
                "pylint",
                "quickdocs",
                "twine",
                "wheel",
            ],
        },
    )
