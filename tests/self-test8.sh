#!/usr/bin/env bash


#
# Copyright 2015 Gu Zhengxiong <rectigu@gmail.com>
#


self_test()
{
    ./pat8.sh \
        $(./pat8.sh $1 \
                 | grep Pattern \
                 | cut -d ' ' -f 2 \
                 | tail -c 9) \
        | grep Offset | cut -d ' ' -f 2
}


i=8
while [[ $i -le 102760448 ]]
do
    result=$(self_test $i)
    difference=$(($i - $result))

    if [[ $difference -eq 8 ]]
    then
        printf '\r%s' $i
    else
        printf 'i: %s result: %s difference: %s\n' \
               $i $result $difference
    fi

    i=$(($i + 1))
done
