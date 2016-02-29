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


import sys
from itertools import product
from string import digits, ascii_lowercase, ascii_uppercase
from binascii import unhexlify

import click

from . import __version__, PROGRAM_NAME


@click.command(
    context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(__version__,
                      '-V', '--version', prog_name=PROGRAM_NAME)
@click.argument('argument', required=True)
@click.argument('sets', nargs=-1, required=False)
def main(argument, sets):
    """Customizable Exploit Pattern Utility."""
    if sets:
        space = sets
    else:
        space = [ascii_uppercase, ascii_lowercase, digits]
    patterns = ''.join(map(''.join, product(*space)))
    if argument.isdigit():
        count = int(argument)
        if len(patterns) >= count:
            print(patterns[:count])
        else:
            print('Count {} Overflows Space {}!'.format(count, space))
            sys.exit(1)
    else:
        if argument.startswith('0x'):
            target = unhexlify(argument[2:]).decode('utf-8')
        else:
            target = argument
        try:
            print(patterns.index(target))
        except ValueError:
            print('Target {} Not Found In Space {}!'.format(
                target, space))
            sys.exit(1)
    sys.exit(0)
