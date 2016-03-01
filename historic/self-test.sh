#!/usr/bin/env bash


#
# Copyright 2015-2016 Gu Zhengxiong <rectigu@gmail.com>
#


test_one() {
    local bin=${1}
    local bit=${2}
    local max=${3}
    local i=3
    local result difference percent
    while [[ ${i} -le ${max} ]]; do
        result=$(create_and_locate "${bin}" "${bit}" "${i}")
        difference=$((i - result))
        if [[ $difference -eq 3 ]]; then
            printf '\r%s / %s' "${i}" "${max}"
        else
            printf '\ni: %s result: %s difference: %s\n' \
                   "${i}" "${result}" "${difference}"
        fi
        i=$((i + 1))
    done
}


create_and_locate() {
    local bin="${1}"
    local bit="${2}"
    local num="${3}"
    "${bin}" $("${bin}" "${num}" | tail -c$((bit + 1)))
}


bin=(pattern pat3 pat4 pat8)
bit=(3 3 4 8)
max=(20280 26460 230400 102760448)


i=0
while [[ $i -lt "${#bin[@]}" ]]; do
    >&2 printf 'Testing %s %s %s...\n' \
        "${bin[${i}]}" "${bit[${i}]}" "${max[${i}]}"
    time test_one "${bin[${i}]}" "${bit[${i}]}" "${max[${i}]}"
    i=$((i + 1))
done
