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
    ABCDEFGHIJKLMNOP \
    QRSTUVWXYZabcdef \
    ghijklmnopqrstu \
    vwxyz0123456789 $1
