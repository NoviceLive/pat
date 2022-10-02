Customizable Lazy Exploit Pattern Utility
=========================================

.. image:: https://img.shields.io/pypi/v/pat.svg
   :target: https://pypi.python.org/pypi/Pat

.. image:: https://travis-ci.org/NoviceLive/pat.svg?branch=master
   :target: https://travis-ci.org/NoviceLive/pat


Official Mirrors
----------------

- https://gitlab.com/imtheforce/pat
- https://bitbucket.org/fourthorigin/pat
- https://github.com/NoviceLive/pat


Latest Updates
--------------

I learned from pwntools_ that there is another kind of sequences,
named `De Bruijn sequence`_,
which is powerful and has excessive potentials.

Check it if you are interested.

Its pattern looks like the following as produced by ``cyclic``
provided by pwntools_.

::

   $ cyclic 400
   aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaaczaadbaadcaaddaadeaadfaadgaadhaadiaadjaadkaadlaadmaadnaadoaadpaadqaadraadsaadtaaduaadvaadwaadxaadyaad

   $ cyclic -l yaad
   396


Installation
------------

``pip install pat`` works, elevate privilege if necessary.

Requirements
++++++++++++

Click_
******
Python composable command line utility.

Colorama_
*********

Simple cross-platform colored terminal text in Python.

Pyperclip_
**********

Python module for cross-platform clipboard functions.


flufl.i18n_
***********

A high level API for Python internationalization.

This is not used for the time being.


Usage
-----

::

   ./pat.py --help
   Usage: pat.py [OPTIONS] ARGUMENT [SETS]...

     Customizable Lazy Exploit Pattern Utility.

   Options:
     -V, --version          Show the version and exit.
     -b, --big-endian       Use big-endian.
     -O, --optimal INTEGER  Use the optimal profile in this position.
     -o, --output FILENAME  Write to this file.
     -c, --clipboard        Output to the clipboard.
     -v, --verbose          Be verbose.
     -q, --quiet            Be quiet.
     -h, --help             Show this message and exit.


Examples
--------

- Create a pattern of length 100 using the default profile.

  ::

     ./pat.py 100
     Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A

- Locate the pattern ``Cz9`` in the default profile.

  ::

     ./pat.py Cz9
     2337

- Locate the pattern in hex, ``0x5a6232``, using the default profile.

  For big-endian systems.

  ::

     ./pat.py 0x5a6232 -b
     19536

- Create a pattern of length 200 in optimal 3-position profile.

  ::

     ./pat.py 200 -O3
     AVqAVrAVsAVtAVuAVvAVwAVxAVyAVzAV0AV1AV2AV3AV4AV5AV6AV7AV8AV9AWqAWrAWsAWtAWuAWvAWwAWxAWyAWzAW0AW1AW2AW3AW4AW5AW6AW7AW8AW9AXqAXrAXsAXtAXuAXvAXwAXxAXyAXzAX0AX1AX2AX3AX4AX5AX6AX7AX8AX9AYqAYrAYsAYtAYuAYvAY

- Search for pattern ``vAY`` in optimal 3-position profile.

  ::

     ./pat.py vAY -O3
     197


API
---


See ``pydoc pat.Pat``.


Mathematical Background
-----------------------


Simply speaking, it is a string of continuous numbers
in some special `positional numeral systems`_,
where symbols in each position are mutually unique,
often with a big radix.

It can be created by taking the needed count of characters
from the `Cartesian product`_ of chosen character sets.


Profiles
--------

Default Profile
+++++++++++++++

- Three-position: The most popular choice

  - Maximum Length

    26 :sup:`2` * 10 * 3 B = 20280 B = 19 KiB.

  ::

     ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789


Optimal Profiles
++++++++++++++++

Suppose that we have a limited set of characters,
e.g. alphanumeric ones, in which there are 62 characters available.

According to the `inequality of arithmetic and geometric means`_,
fixed radix systems will achieve the best length.


Three-position
**************

- Maximum Length

  21 :sup:`2` * 20 * 3 B = 26460 B = 25 KiB

::

   ABCDEFGHIJKLMNOPQRSTU VWXYZabcdefghijklmnop qrstuvwxyz0123456789

Four-position
*************

- Maximum Length

  16 :sup:`2` * 15 :sup:`2` * 4 B = 230400 B = 225 KiB

::

   ABCDEFGHIJKLMNOP QRSTUVWXYZabcdef ghijklmnopqrstu vwxyz0123456789


Eight-position
**************

- Maximum Length

  8 :sup:`6` * 7 :sup:`2` * 8 B = 102760448 B = 98 MiB

::

   ABCDEFGH IJKLMNOP QRSTUVWX YZabcdef ghijklmn opqrstuv wxyz012 3456789


.. _positional numeral systems: https://en.wikipedia.org/wiki/Positional_notation

.. _Cartesian product: https://en.wikipedia.org/wiki/Cartesian_product

.. _inequality of arithmetic and geometric means: https://en.wikipedia.org/wiki/Inequality_of_arithmetic_and_geometric_means

.. _Colorama: https://github.com/tartley/colorama
.. _Click: https://github.com/mitsuhiko/click
.. _Pyperclip: https://github.com/asweigart/pyperclip
.. _flufl.i18n: https://gitlab.com/warsaw/flufl.i18n
.. _pwntools: https://github.com/Gallopsled/pwntools
.. _De Bruijn sequence: https://en.wikipedia.org/wiki/De_Bruijn_sequence
