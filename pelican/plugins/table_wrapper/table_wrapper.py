# Table Wrapper
#
# Pelican plugin for wrapping table into classed div
#
# Copyright (c) 2021 Pawo
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import logging

from bs4 import BeautifulSoup

from pelican import signals

logger = logging.getLogger(__name__)
table_wrapper_settings = {}


def pelican_init(pelicanobj):

    # default value - no self-style for div
    table_wrapper_settings["style"] = None

    # Get the user specified settings
    if "TABLE_WRAPPER" in pelicanobj.settings:
        settings = pelicanobj.settings["TABLE_WRAPPER"]
    else:
        settings = None

    # If no settings have been specified, then default will be used
    if not isinstance(settings, dict):
        return

    # May add more settings in the future
    for key, value in ((key, settings[key]) for key in settings):

        if key == "style":
            table_wrapper_settings[key] = value


def wrapper(instance):

    if instance._content is not None:

        content = instance._content
        soup = BeautifulSoup(content, "html.parser")

        if "table" in content:
            for table_tag in soup.find_all("table"):
                wrapper_tag = soup.new_tag("div")
                wrapper_tag["class"] = "table_wrapper"
                if table_wrapper_settings["style"] is not None:
                    wrapper_tag["style"] = table_wrapper_settings["style"]
                table_tag.wrap(wrapper_tag)

        instance._content = soup.decode()


def register():
    signals.initialized.connect(pelican_init)
    signals.content_object_init.connect(wrapper)
