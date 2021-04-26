[![Build Status](https://img.shields.io/github/workflow/status/pawo1/table-wrapper/build)](https://github.com/pawo1/table-wrapper/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-table-wrapper)](https://pypi.org/project/pelican-table-wrapper/)
![License](https://img.shields.io/pypi/l/pelican-table-wrapper?color=blue)

Pelican plugin for wrapping table into classed div `.table_wrapper`. It allows 
you to better style tables. E.g. make them scrollable on small displays.

Installation
------------

This plugin can be installed via:

    python -m pip install pelican-table-wrapper

Usage
-----

To use this plugin you have to add it to PLUGINS variable in pelicanconf.py:
```python
PLUGINS = ['table_wrapper', ...]
```

If you don't want add `.table_wrapper` to your CSS, plugin can generate self-styled
elements. Just specify style that you want in pelicanconf.py:
```python
TABLE_WRAPPER = {'style':'overflow: auto;'}
```

Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pawo1/table-wrapper/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

License
-------

This project is licensed under the MIT license.
