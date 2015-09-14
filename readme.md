# Customizable Exploit Pattern Utility

## Installation

This repository is accompanied with prebuilt binaries
for both Linux (x64 only) and Windows.

Note that the Windows binaries are cross compiled via mingw-w64.

Also note that the source code can not be compiled successfully
with Microsoft C compiler without modidification.

Download the binary for your system
and add the directory which contains it to the shell's search path
so as to invoke it simply by typing `pattern`.

## Basic Usage

Create a pattern of length 200 using the default profile (see below):

```bash
pattern 200
```

Compute the offset of the pattern z8Z in the default profile (see below):

```bash
pattern z8Z
```

## Using Customized Profiles

Syntax:

```bash
pattern space_0 space_1 space_2 ... space_n keyword
```

All but the last arguments together will be treated as one profile.
The last argument will be treated as the keyword,
which can be either a number indicating the pattern length
to generate or a pattern to compute the corresponding offset.

The default profile (when you invoke the program with
only one argument) is equivalent to the following invocation:

```bash
pattern ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789 keyword
```

Note that since the program assumes a keyword of pure numbers
as the pattern length to create,
you can not use profiles containing mere numbers.

## Mathematical Background

Simply speaking, it is a string of continuous numbers
in some special [positional numeral system]s,
where symbols in each position are mutually unique,
often with a big radix.

## Comparison Of Different Radices / Profiles

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

Example 1 (the default profile is this case):
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
```
Example 2 (see [pat3.sh](./pat3.sh))
```
ABCDEFGHIJKLMNOPQRSTU
VWXYZabcdefghijklmnop
qrstuvwxyz0123456789
```
Example 3 (see [pat4.sh](./pat4.sh))
```
ABCDEFGHIJKLMNOP
QRSTUVWXYZabcdef
ghijklmnopqrstu
vwxyz0123456789

```
Example 4 (see [pat8.sh](./pat8.sh))
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
(see the aforementioned comparison of different profiles).

Nevertheless, as a general case of demonstration,
and following a popular choice,
which is based on mixed radix systems,
I only implemented mixed radix computation.
In other words, all profiles given to the program will be treated
as mixed radix numeral systems,
even they are actually fixed radix ones.

## Test Suites

Test is done through self-test.
But note that it only tests the default profile.

```bash
tests/self-test.sh  # Passed
tests/self-test3.sh # Passed
tests/self-test4.sh # WARNING: FAILED
tests/self-test8.sh # WARNING: FAILED
```

## Fix Me

### print_pattern

Currently it is implemented as a recursive function,
whether to keep the recursive version
or to reimplement another one based on something
like `decimal_to_mixed` remains undecided.

### decrement_mixed_string

It will not decrement any mixed string by one.

__WARNING: UNFIXED KNOWN BUGS EXIST AS IN PAT4 & PAT8!__

## Copyright

Copyright 2015 Gu Zhengxiong <rectigu@gmail.com>

## License

See license.txt.

[positional numeral system]: https://en.wikipedia.org/wiki/Positional_notation
[inequality of arithmetic and geometric means]: https://en.wikipedia.org/wiki/Inequality_of_arithmetic_and_geometric_means
[mixed radix numeral system]: https://en.wikipedia.org/wiki/Mixed_radix

## Related Projects

- [Svenito/exploit-pattern](https://github.com/Svenito/exploit-pattern)
