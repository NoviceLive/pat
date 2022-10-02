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
from logging import getLogger
from itertools import islice
from sys import version_info


# zip_longest & accumulate handling taken from fn.py

if version_info[0] == 2:
    from itertools import izip_longest as zip_longest
else:
    from itertools import zip_longest


if version_info[0] == 3 and version_info[1] >= 3:
    from itertools import accumulate
else:
    def accumulate(iterable, func=add):
        """Make an iterator that returns accumulated sums.
        Elements may be any addable type including Decimal or Fraction.
        If the optional func argument is supplied, it should be a
        function of two arguments and it will be used instead of addition.

        Origin implementation:
        http://docs.python.org/dev/library/itertools.html#itertools.accumulate

        Backported to work with all python versions (< 3.3)
        """
        it = iter(iterable)
        total = next(it)
        yield total
        for element in it:
            total = func(total, element)
            yield total


logging = getLogger(__name__)


def most_even_chunk(string, group):
    """Divide a string into a list of strings as even as possible."""
    counts = [0] + most_even(len(string), group)
    indices = accumulate(counts)
    slices = window(indices, 2)
    return [string[slice(*one)] for one in slices]


def most_even(number, group):
    """Divide a number into a list of numbers as even as possible."""
    count, rest = divmod(number, group)
    counts = zip_longest([count] * group, [1] * rest, fillvalue=0)
    chunks = [sum(one) for one in counts]
    logging.debug('chunks: %s', chunks)
    return chunks


def window(seq, count=2):
    """Slide window."""
    iseq = iter(seq)
    result = tuple(islice(iseq, count))
    if len(result) == count:
        yield result
    for elem in iseq:
        result = result[1:] + (elem,)
        yield result
