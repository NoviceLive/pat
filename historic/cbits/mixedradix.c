/*
 * Copyright 2015-2016 Gu Zhengxiong <rectigu@gmail.com>
 */


# include <stdio.h>
# include <string.h>
# include <stdbool.h> /* For bool. */

# include "mixedradix.h"


int
mixed_to_decimal(int *radices, int *values,
                 unsigned int count)
{
  int weights[count];

  radices_to_weights(radices, weights, count);

  return vector_dot_product(weights, values, count);
}


int *
radices_to_weights(int *radices, int *weights,
                   unsigned int count)
{
  weights[count - 1] = 1;

  for (int i = count - 2; i >= 0; --i) {
    weights[i] = weights[i + 1] * radices[i + 1];
  }

  return weights;
}


int
get_mixed_max(int *radices, unsigned int count)
{
  return product(radices, count) - 1;
}


bool
check_mixed_string(char *mixed, char **space)
{
  size_t count = strlen(mixed);

  for (int i = 0; i < count; ++i) {
    if (!strchr(space[i], mixed[i]))
      return false;
  }

  return true;
}


unsigned
adjust_mixed_string(char *mixed, char **space)
{
  size_t count = strlen(mixed);
  int i;

  for (i = 0; i < count; ++i) {
    if (strchr(space[0], mixed[i]))
      break;
  }

  bool need_decrement = true;

  for (int j = 0; j < i; ++j) {
    int position = count - i + j;
    char upper = space[position][strlen(space[position]) - 1];
    if (mixed[j] != upper) {
      need_decrement = false;
      break;
    }
  }

  if (need_decrement) {
    decrement_mixed_string(mixed + i, space);
  }

  left_rotate_string(mixed, i);

  return count - i;
}


char *
decrement_mixed_string(char *mixed, char **space)
{
  unsigned digit_no = strlen(mixed);
  int pos = strcspn(space[digit_no - 1], &mixed[digit_no - 1])
    - 1;

  if (pos < 0) {
    mixed[digit_no - 1] =
      space[digit_no - 1][strlen(space[digit_no - 1]) - 1];

    for (int i = digit_no - 2; i >= 0; --i) {
      pos = strcspn(space[i], mixed + i) - 1;
      if (pos < 0) {
        mixed[i] = space[i][strlen(space[i]) - 1];
      } else {
        mixed[i] = space[i][pos];
        break;
      }
    }
  } else {
    mixed[digit_no - 1] = space[digit_no - 1][pos];
  }

  return mixed;
}


int *
get_mixed_radices(char **space, int *radices,
                  unsigned int count)
{
  for (int i = count - 1; i >= 0; --i) {
    radices[i] = strlen(space[i]);
  }

  return radices;
}


int *
get_mixed_values(char *mixed, char **space, int *values)
{
  size_t count = strlen(mixed);

  for (int i = count - 1; i >=0; --i) {
    values[i] = strcspn(space[i], &mixed[i]);
  }

  return values;
}


int
vector_dot_product(int *a, int *b, unsigned int count)
{
  int result = 0;

  for (int i = 0; i < count; ++i) {
    result += a[i] * b[i];
  }

  return result;
}


int
product(int *a, unsigned int count)
{
  int result = 1;

  for (int i = 0; i < count; ++i) {
    result *= a[i];
  }

  return result;
}


bool
is_type_string(char *s, int (*type_func)(int))
{
  for (int i = 0; i < strlen(s); ++i)
    if (!type_func(s[i]))
      return false;
  return true;
}


char *
left_rotate_string(char *string, int left)
{
  size_t length = strlen(string);
  left %= length;

  reverse_string(string, 0, left - 1);
  reverse_string(string, left, length - 1);
  reverse_string(string, 0, length - 1);

  return string;
}


char *
reverse_string(char *string, int start, int end)
{
  char *p_start = string + start;
  char *p_end = string + end;
  char temp;

  while (p_start < p_end) {
    temp = *p_start;
    *p_start++ = *p_end;
    *p_end-- = temp;
  }

  return string;
}
