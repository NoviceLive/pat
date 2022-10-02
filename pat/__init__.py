"""
Copyright 2016 Gu Zhengxiong <rectigu@gmail.com>

This file is part of Pat.

Pat is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Pat is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Pat.  If not, see <http://www.gnu.org/licenses/>.
"""


from __future__ import division, absolute_import, print_function
from logging import Handler, getLogger
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(Handler):
        def emit(self, record):
            pass

from .pat import Pat


__author__ = 'Gu Zhengxiong'
__version__ = '0.5.3'


PROGRAM_NAME = 'Pat'
PACKAGE_NAME = 'pat'

VERSION_PROMPT = (
    '{version}\n\nCopyright 2015-2016 {author} '
    '<rectigu@gmail.com>\n\n'
    'This is free software; see the source for '
    'copying conditions.\nThere is NO warranty; '
    'not even for MERCHANTABILITY nor \nFITNESS FOR '
    'A PARTICULAR PURPOSE.'.format(
        version=__version__, author=__author__)
)


__all__ = ['Pat']


getLogger(__name__).addHandler(NullHandler())
