"""Docs config."""

extensions = ["autoapi.extension"]
html_baseurl = "/py-vw/"

# region: autoapi
autoapi_dirs = ["../vw"]
autoapi_options = [
    "members",
    "undoc-members",
    # "private-members", -> turn off private members from the default
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
]
# endregion

# region: rtd_theme
extensions.append("sphinx_rtd_theme")

html_theme = "sphinx_rtd_theme"
# endregion

# region: markdown handling
extensions.append("myst_parser")
# endregion
