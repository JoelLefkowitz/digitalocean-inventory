import datetime
import os
import re
import sys

import pypandoc

sys.path.append("../..")


project = "DigitalOcean Inventory"
version = "1.0.0"
master_doc = "index"
author = "Joel Lefkowitz"
copyright = f"{datetime.datetime.now().year}, {author}"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "venv"]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_annotation",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib.apidoc",
]


def relpath(path: str) -> str:
    return os.path.realpath(os.path.join(__file__, path))


def convert_md(source_file: str, target_dir: str) -> None:
    filename = os.path.basename(source_file).replace(".md", ".html")
    output_path = os.path.join(target_dir, filename)
    md = open(source_file, "r").read()

    with open(output_path, "w") as file:
        file.write(pypandoc.convert(md, "html", format="md"))


def remove_heading(path) -> None:
    html = open(path, "r").read()
    with open(path, "w") as file:
        filtered = re.sub("<h1.*>.*?</h1>", "", html, flags=re.DOTALL)
        file.write(filtered)


# Yummy sphinx theme settings
html_theme = "yummy_sphinx_theme"
html_title = "DigitalOcean inventory"
static_dir = relpath("../static")

html_favicon = os.path.join(static_dir, "favicon.ico")
html_theme_options = {
    "github_url": "JoelLefkowitz/yummy-cereal",
    "navbar_icon": "spin fa-book",
}
html_css_files = [os.path.join(static_dir, "styles.css")]
html_add_permalinks = ""

# Convert README to html directly
convert_md(relpath("../../README.md"), static_dir)
remove_heading(os.path.join(static_dir, "README.html"))

# Autodoc settings
autodoc_typehints = "description"
typehints_fully_qualified = True
autodoc_default_flags = ["members", "undoc-members"]

# Napoleon settings
napoleon_google_docstring = True

# Apidoc settings
apidoc_module_dir = relpath("../../digitalocean_inventory")
apidoc_extra_args = ["-e"]
