from setuptools import setup

if __name__ == "__main__":
    setup(
        entry_points={
            "console_scripts": [
                "digitalocean-inventory=digitalocean_inventory.__main__:fetch"
            ]
        },
        install_requires=[
            "dataclasses",
            "safe_environ",
            "python-digitalocean",
        ],
        extras_require={
            "dist": ["wheel", "twine", "bump2version"],
            "docs": [
                "sphinx",
                "pypandoc",
                "sphinxcontrib.apidoc",
                "sphinxcontrib.pandoc_markdown",
                "sphinx-autodoc-annotation",
                "yummy_sphinx_theme",
            ],
            "tests": [
                "pytest",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-bdd",
                "pytest-watch",
            ],
        },
    )
