/*
 * Copyright 2015 Gu Zhengxiong <rectigu@gmail.com>
 */


# include <stdlib.h>
# include <stdio.h>
# include <string.h>

# include "libhex.h"


void
print_hex(char *string)
{
  for (int i = 0; i < strlen(string); ++i)
    printf("%x", string[i]);

  putchar('\n');
}


char *
unhex(char *string)
{
  size_t length = strlen(string);
  char temp[3] = { 0 };
  int i;

  for (i = 0; i < length; i += 2) {
    strncpy(temp, string + i, 2);
    string[i / 2] = (char)strtoul(temp, NULL, 16);
  }
  string[i / 2] = 0;

  return string;
}
