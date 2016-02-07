/*
 * Copyright 2015-2016 Gu Zhengxiong <rectigu@gmail.com>
 */


# ifndef _GU_ZHENGXIONG_MIXEDRADIX_H
# define _GU_ZHENGXIONG_MIXEDRADIX_H

# include <stdbool.h> /* For bool. */


int
mixed_to_decimal(int *radices, int *values,
                 unsigned int count);

int *
radices_to_weights(int *radices, int *weights,
                   unsigned int count);

int
get_mixed_max(int *radices, unsigned int count);


bool
check_mixed_string(char *mixed, char **space);

unsigned
adjust_mixed_string(char *mxied, char **space);

char *
decrement_mixed_string(char *mixed, char **alphabet);

int *
get_mixed_radices(char **space, int *radices,
                  unsigned int count);

int *
get_mixed_values(char *mixed, char **space, int *values);


int
vector_dot_product(int *a, int *b, unsigned int count);

int
product(int *a, unsigned int count);

bool
is_type_string(char *s, int (*type_func)(int));

char *
left_rotate_string(char *string, int left);

char *
reverse_string(char *string, int start, int end);


# endif /* mixedradix.h */
