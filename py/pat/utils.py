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


from itertools import islice

from fn.uniform import zip_longest
from fn.iters import accumulate


def chunked_even(string, group):
    """Divide a string into a list of strings as even as possible."""
    counts = [0] + most_even(len(string), group)
    indices = accumulate(counts)
    slices = window(indices, 2)
    return [string[slice(*one)] for one in slices]


def window(seq, count=2):
    """Slide window."""
    iseq = iter(seq)
    result = tuple(islice(iseq, count))
    if len(result) == count:
        yield result
    for elem in iseq:
        result = result[1:] + (elem,)
        yield result


def most_even(number, group):
    """Divide a number into a list of numbers as even as possible."""
    count, rest = divmod(number, group)
    counts = zip_longest([count] * group, [1] * rest, fillvalue=0)
    return [sum(one) for one in counts]
