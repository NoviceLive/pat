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
import logging
import sys

import click
from pyperclip import copy

from . import VERSION_PROMPT, PROGRAM_NAME
from .init import LevelFormatter, _
from .pat import Pat


@click.command(
    context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(VERSION_PROMPT,
                      '-V', '--version', prog_name=PROGRAM_NAME)
@click.argument('argument', required=True)
@click.argument('sets', nargs=-1)
@click.option('-b', '--big-endian', is_flag=True,
              help='Use big-endian.')
@click.option('-O', '--optimal', type=int,
              help='Use the optimal profile in this position.')
@click.option('-o', '--output', type=click.File('w'),
              help='Write to this file.')
@click.option('-c', '--clipboard', is_flag=True,
              help='Output to the clipboard.')
@click.option('-v', '--verbose', count=True, help='Be verbose.')
@click.option('-q', '--quiet', count=True, help='Be quiet.')
def main(argument, sets, big_endian, optimal, output, clipboard,
         quiet, verbose):
    """Customizable Lazy Exploit Pattern Utility."""
    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(LevelFormatter())
    logger.addHandler(handler)
    logger.setLevel(logging.WARNING + (quiet-verbose)*10)

    if sets and optimal:
        pat = Pat.from_chars(''.join(sets), optimal)
    elif optimal:
        pat = Pat.from_chars(optimal=optimal)
    elif sets:
        pat = Pat(sets)
    else:
        pat = Pat()

    if argument.isdigit():
        count = int(argument)
        try:
            pattern = pat.create(count)
        except IndexError:
            logging.exception(_('Failed to create the pattern.'))
            sys.exit(1)
        else:
            if output:
                output.write(pattern)
            elif clipboard:
                copy(pattern)
            else:
                print(pattern)
    else:
        target = argument
        try:
            index = pat.locate(target, big_endian)
        except KeyError:
            logging.exception(_('Failed to locate the pattern.'))
            sys.exit(1)
        else:
            print(index)

    sys.exit(0)
