#!/usr/bin/env bash


#
# Copyright 2015 Gu Zhengxiong <rectigu@gmail.com>
#


if [[ $# -ne 1 ]]
then
    printf '%s\n' 'Invalid Argument!'
    exit 233
fi


pattern \
    ABCDEFGH \
    IJKLMNOP \
    QRSTUVWX \
    YZabcdef \
    ghijklmn \
    opqrstuv \
    wxyz012 \
    3456789 $1
