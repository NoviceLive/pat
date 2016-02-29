#!/usr/bin/env bash


#
# Copyright 2015-2016 Gu Zhengxiong <rectigu@gmail.com>
#


if [[ $# -ne 1 ]]; then
    printf '%s\n' 'Invalid Argument!'
    exit 233
fi


pattern "${1}" \
        ABCDEFGHIJKLMNOP \
        QRSTUVWXYZabcdef ghijklmnopqrstu vwxyz0123456789
