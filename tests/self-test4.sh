#!/usr/bin/env bash


#
# Copyright 2015 Gu Zhengxiong <rectigu@gmail.com>
#


self_test()
{
    ./pat4.sh \
        $(./pat4.sh $1 \
                 | grep Pattern \
                 | cut -d ' ' -f 2 \
                 | tail -c 5) \
        | grep Offset | cut -d ' ' -f 2
}


i=4
while [[ $i -le 230400 ]]
do
    result=$(self_test $i)
    difference=$(($i - $result))

    if [[ $difference -eq 4 ]]
    then
        printf '\r%s' $i
    else
        printf 'i: %s result: %s difference: %s\n' \
               $i $result $difference
    fi

    i=$(($i + 1))
done
