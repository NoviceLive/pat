#!/usr/bin/env bash


#
# Copyright 2015 Gu Zhengxiong <rectigu@gmail.com>
#


self_test()
{
    ./pat3.sh \
        $(./pat3.sh $1 \
                 | grep Pattern \
                 | cut -d ' ' -f 2 \
                 | tail -c 4) \
        | grep Offset | cut -d ' ' -f 2
}


i=3
while [[ $i -le 26460 ]]
do
    result=$(self_test $i)
    difference=$(($i - $result))

    if [[ $difference -eq 3 ]]
    then
        printf '\r%s' $i
    else
        printf 'i: %s result: %s difference: %s\n' \
               $i $result $difference
    fi

    i=$(($i + 1))
done
