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


from string import digits, ascii_lowercase, ascii_uppercase
from itertools import product, chain, islice, tee
from functools import reduce
from operator import mul
from binascii import unhexlify

from .utils import most_even_chunk, window


ALNUM = [ascii_uppercase, ascii_lowercase, digits]


class Pat(object):
    """A Lazy Customizable Exploit Pattern."""
    def __init__(self, sets=None):
        if not sets:
            sets = ALNUM
        self.sets = sets
        self.position = len(sets)
        self.space = self._create_space()

    @classmethod
    def from_chars(cls, chars='', optimal=3):
        """Construct a Pat object from the specified string
        and optimal position count."""
        if not chars:
            chars = ''.join(ALNUM)
        sets = most_even_chunk(chars, optimal)
        return cls(sets)

    def create_pattern(self, count):
        """Create a pattern of the specified length."""
        space, self.space = tee(self.space)
        limit = reduce(mul, map(len, self.sets)) * self.position
        if limit >= count:
            pattern = ''.join(islice(space, count))
        else:
            pattern = None
        return pattern

    def locate_pattern(self, pattern):
        """Locate the pattern."""
        space, self.space = tee(self.space)
        if pattern.startswith('0x'):
            target = unhexlify(pattern[2:]).decode('utf-8')
        else:
            target = pattern
        for index, one in enumerate(window(space, self.position)):
            if ''.join(one) == target[:self.position]:
                return index
        return None

    def _create_space(self):
        """Create the space used by creating and locating."""
        return chain.from_iterable(map(''.join, product(*self.sets)))
