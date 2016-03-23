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
from logging import Formatter, DEBUG, INFO, WARNING, ERROR, CRITICAL
import os

from colorama import Fore, Style
from pkg_resources import resource_filename
try:
    from flufl.i18n import initialize
except ImportError:
    pass


try:
    os.environ['LOCPATH'] = resource_filename(__name__, 'share')
    _ = initialize('pat')
except (KeyError, NameError):
    _ = lambda x: x


def red(text):
    return Fore.RED + Style.BRIGHT + text


def blue(text):
    return Fore.BLUE + Style.BRIGHT + text


def cyan(text):
    return Fore.CYAN + Style.BRIGHT + text


def yellow(text):
    return Fore.YELLOW + Style.BRIGHT + text


def green(text):
    return Fore.GREEN + Style.BRIGHT + text


class LevelFormatter(Formatter):
    """Logging formatter."""
    critical_formatter = Formatter(red('critical: %(message)s'))
    error_formatter = Formatter(red('error: %(message)s'))
    warning_formatter = Formatter(yellow('warning: %(message)s'))
    info_formatter = Formatter(cyan('%(message)s'))
    debug_formatter = Formatter(
        green('debug: ') + blue('%(name)s.%(funcName)s: ') +
        green('%(message)s'))

    def __init__(self):
        Formatter.__init__(self)

    def format(self, record):
        """Format the record using the corresponding formatter."""
        if record.levelno == DEBUG:
            return self.debug_formatter.format(record)
        if record.levelno == INFO:
            return self.info_formatter.format(record)
        if record.levelno == ERROR:
            return self.error_formatter.format(record)
        if record.levelno == WARNING:
            return self.warning_formatter.format(record)
        if record.levelno == CRITICAL:
            return self.critical_formatter.format(record)
