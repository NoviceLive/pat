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
from string import digits, ascii_lowercase, ascii_uppercase
from itertools import product, chain, islice, tee
from functools import reduce
from operator import mul
from binascii import unhexlify

from .utils import most_even_chunk, window


logging = getLogger(__name__)
ALNUM = [ascii_uppercase, ascii_lowercase, digits]


class Pat(object):
    """A Lazy Customizable Exploit Pattern."""
    def __init__(self, sets=None):
        if not sets:
            sets = ALNUM
        logging.debug('sets: %s', sets)
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

    def __getitem__(self, key):
        if str(key).isdigit():
            count = int(key)
            return self.create(count)
        else:
            target = key
            return self.locate(target, big_endian=False)

    def create(self, count):
        """Create a pattern of the specified length."""
        space, self.space = tee(self.space)
        limit = reduce(mul, map(len, self.sets)) * self.position
        logging.debug('limit: %s', limit)
        if limit >= count:
            return ''.join(islice(space, count))
        else:
            raise IndexError('{count} Overflows {sets}!'.format(
                count=count, sets=self.sets))

    def locate(self, pattern, big_endian=False):
        """Locate the pattern."""
        space, self.space = tee(self.space)
        if pattern.startswith('0x'):
            target = unhexlify(
                pattern[2:].encode('utf-8')).decode('utf-8')
            if not big_endian:
                target = target[::-1]
        else:
            target = pattern
        for index, one in enumerate(window(space, self.position)):
            if ''.join(one) == target[:self.position]:
                return index
        raise KeyError('{target} Not Found In {sets}!'.format(
            target=pattern, sets=self.sets))

    def _create_space(self):
        """Create the space used by creating and locating."""
        return chain.from_iterable(map(''.join, product(*self.sets)))
