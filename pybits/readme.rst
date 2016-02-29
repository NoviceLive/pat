Customizable Exploit Pattern Utility
====================================


See the readme_ of C version for more information
such as mathematical background and **profiles**.

See the code_ if you are eager.


.. _readme: ../readme.md

.. _code: https://github.com/NoviceLive/pat/blob/master/pybits/pat/main.py#L37


Installation
------------

``pip install pat`` works, elevate privilege if necessary.


Usage
-----

::

   ./pat.py --help
   Usage: pat.py [OPTIONS] ARGUMENT [SETS]...

   Options:
     -V, --version  Show the version and exit.
     -h, --help     Show this message and exit.


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

  ::

     ./pat.py 0x5a6232
     19536

- Create a pattern of length 200 in optimal 3-radix profile.

  ::

     ./pat.py 200 ABCDEFGHIJKLMNOPQRSTU VWXYZabcdefghijklmnop qrstuvwxyz0123456789
     AVqAVrAVsAVtAVuAVvAVwAVxAVyAVzAV0AV1AV2AV3AV4AV5AV6AV7AV8AV9AWqAWrAWsAWtAWuAWvAWwAWxAWyAWzAW0AW1AW2AW3AW4AW5AW6AW7AW8AW9AXqAXrAXsAXtAXuAXvAXwAXxAXyAXzAX0AX1AX2AX3AX4AX5AX6AX7AX8AX9AYqAYrAYsAYtAYuAYvAY

- Search for pattern ``vAY`` in optimal 3-radix profile.

  ::

     ./pat.py vAY ABCDEFGHIJKLMNOPQRSTU VWXYZabcdefghijklmnop qrstuvwxyz0123456789
     197
