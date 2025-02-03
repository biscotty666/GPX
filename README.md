# GPX Data in Python

This repository shows how to import gpx data into Python dataframes for mapping and analysis. Associated articles are published on [my website](https://biscotty.online) and provided here as HTML files in the html subdirectory.

[Article 1](https://biscotty.online/blogs/gpx-gps-data)
[Article 2](https://biscotty.online/blogs/python-movingpandas-points-paths)

Libraries used include Pandas, GeoPandas and MovingPandas, as well as BeautifulSoup for parsing.

A flake is provided for nix users, although after entering the shell the first time, you need to `pip install -r requirements.txt`. For non-nix users, additional required packages are listed in the `flake.nix` file.
