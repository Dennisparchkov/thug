#!/usr/bin/env python
#
# Location.py
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA  02111-1307  USA

import PyV8
from urlparse import urlparse

class Location(PyV8.JSClass):
    def __init__(self, window):
        self._window = window

    @property
    def parts(self):
        return urlparse(self._window.url)

    @property
    def href(self):
        return self._window.url

    @href.setter
    def href(self, url):
        self._window.open(url)

    @property
    def protocol(self):
        return self.parts.scheme

    @property
    def host(self):
        return self.parts.netloc

    @property
    def hostname(self):
        return self.parts.hostname

    @property
    def port(self):
        return self.parts.port

    @property
    def pathname(self):
        return self.parts.path

    @property
    def search(self):
        return self.parts.query

    @property
    def hash(self):
        return self.parts.fragment

    def assign(self, url):
        """Loads a new HTML document."""
        self._window.open(url)

    def reload(self):
        """Reloads the current page."""
        self._window.open(self.win.url)

    def replace(self, url):
        """Replaces the current document by loading another document at the specified URL."""
        self._window.open(url)

