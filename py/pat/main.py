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
from itertools import product, chain, islice
from functools import reduce
from operator import mul
from string import digits, ascii_lowercase, ascii_uppercase
from binascii import unhexlify

import click
from pyperclip import copy

from . import __version__, PROGRAM_NAME
from .utils import chunked_even, window


@click.command(
    context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(__version__,
                      '-V', '--version', prog_name=PROGRAM_NAME)
@click.argument('argument', required=True)
@click.argument('sets', nargs=-1)
@click.option('-O', '--optimal', type=int,
              help='Use the optimal profile in this position.')
@click.option('-o', '--output', type=click.File('w'),
              help='Write to this file.')
@click.option('-c', '--clipboard', is_flag=True,
              help='Output to the clipboard.')
def main(argument, sets, optimal, output, clipboard):
    """Customizable Exploit Pattern Utility."""
    space = [ascii_uppercase, ascii_lowercase, digits]
    if optimal:
        space = chunked_even(''.join(space), optimal)
    elif sets:
        space = sets
    patterns = chain.from_iterable(map(''.join, product(*space)))
    limit = reduce(mul, map(len, space)) * len(space)
    if argument.isdigit():
        count = int(argument)
        if limit >= count:
            needed = ''.join(islice(patterns, count))
            if output:
                output.write(needed)
            elif clipboard:
                copy(needed)
            else:
                print(needed)
        else:
            print('Count {} Overflows Space {}!'.format(count, space))
            sys.exit(1)
    else:
        if argument.startswith('0x'):
            target = unhexlify(argument[2:]).decode('utf-8')
        else:
            target = argument
        found = False
        for index, one in enumerate(window(patterns, len(space))):
            if target[:len(space)] == ''.join(one):
                print(index)
                found = True
        if not found:
            print('Target {} Not Found In Space {}!'.format(
                target, space))
            sys.exit(1)
    sys.exit(0)
