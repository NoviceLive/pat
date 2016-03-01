# Customizable Exploit Pattern Utility


## Installation

This repository is accompanied with prebuilt binaries
for both Linux and Windows, either x86 or x64.

Note that the Windows binaries are cross compiled via mingw-w64.

Also note that the source code can not be compiled successfully
with Microsoft C compiler without modidification due to the use
of variable length arrays, etc.

Download the binary for your system
and add the directory which contains it to the shell's search path
so as to invoke it simply by typing `pattern`.


## Basic Usage

Create a pattern of length 200 using the default radices
(see below):

```bash
pattern 200
```

Compute the offset of the pattern z8Z in the default radices
(see below):

```bash
pattern z8Z
```


## Using Customized Radices

Syntax:

```bash
pattern keyword space_0 space_1 space_2 ... space_n
```

All but the first arguments together will be treated as radices.
The last argument will be treated as the keyword,
which can be either a number indicating the pattern length
to generate or a pattern to compute the corresponding offset.

The default radices (when you invoke the program with
only one argument) is equivalent to the following invocation:

```
pattern keyword ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789
```

Note that since the program assumes a keyword of pure numbers
as the pattern length to create,
you can not use spaces containing mere numbers.


## Mathematical Background

Simply speaking, it is a string of continuous numbers
in some special [positional numeral system]s,
where symbols in each position are mutually unique,
often with a big radix.

It can be created by taking the needed count of characters
from the [Cartesian product] of chosen character sets.


## Comparison Of Different Radices

Suppose that we have a limited set of characters,
e.g. alphanumeric ones, in which there are 62 characters available.

According to the [inequality of arithmetic and geometric means],
fixed radix systems will achieve the best length.

| Position Number | Chosen Radices | Maximum Number| Maximum Length
| --- | --- | --- | ---
| 3 | 26 26 10 (Example 1) | 6759 | 20280 B = 19 KiB
| 3 | 21 21 20 ( Example 2) | 8819 | 26460 B = 25 KiB
| 4 | 16 16 15 15 (Example 3) | 57599 | 230400 B = 225 KiB
| 8 | 8 8 8 8 8 8 7 7 (Example 4) | 12845055 | 102760448 B = 98 MiB

Example 1 (the default radices is this case):
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
```
Example 2 (see [pat3.sh](./sh/pat3.sh))
```
ABCDEFGHIJKLMNOPQRSTU
VWXYZabcdefghijklmnop
qrstuvwxyz0123456789
```
Example 3 (see [pat4.sh](./sh/pat4.sh))
```
ABCDEFGHIJKLMNOP
QRSTUVWXYZabcdef
ghijklmnopqrstu
vwxyz0123456789

```
Example 4 (see [pat8.sh](./sh/pat8.sh))
```
ABCDEFGH
IJKLMNOP
QRSTUVWX
YZabcdef
ghijklmn
opqrstuv
wxyz012
3456789
```


## Caveats

As a matter of fact, it is more expensive,
both in development time and run time,
to use a [mixed radix numeral system],
compared with fixed radix ones.

And importantly, a fixed radix numeral system will suffice
(see the aforementioned comparison of different radices).

Nevertheless, as a general case of demonstration,
and following a popular choice,
which is based on mixed radix systems,
I only implemented mixed radix computation.
In other words, all radices given to the program will be treated
as mixed radix numeral systems,
even they are actually fixed radix ones.


## Test Suites

Test is done through self-test.

```bash
tests/self-test.sh  # Watch out for computing density!
```


## To Be Improved

### print_pattern

Currently it is implemented as a recursive function,
whether to keep the recursive version
or to reimplement another one based on something
like `decimal_to_mixed` remains undecided.


### decrement_mixed_string

Decrement a mixed string by one.

How to implement it elegantly?

What principles or mathematical operations are under the hood?


## Copyright

Copyright 2015-2016 Gu Zhengxiong <rectigu@gmail.com>


## License

See license.txt.


[positional numeral system]: https://en.wikipedia.org/wiki/Positional_notation
[Cartesian product]: https://en.wikipedia.org/wiki/Cartesian_product
[inequality of arithmetic and geometric means]: https://en.wikipedia.org/wiki/Inequality_of_arithmetic_and_geometric_means
[mixed radix numeral system]: https://en.wikipedia.org/wiki/Mixed_radix