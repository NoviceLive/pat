/*
 * Copyright 2015 Gu Zhengxiong <rectigu@gmail.com>
 */


# include <stdlib.h>
# include <stdio.h>
# include <string.h>

# include "libhex.h"

int
main(int argc, char **argv)
{
  if (argc != 2) {
    printf("%s\n", "Invalid Argument!");
    return EXIT_FAILURE;
  }
  size_t length = strlen(argv[1]);

  unhex(argv[1]);

  for (int i = 0; i < length / 2; ++i)
    putchar(argv[1][i]);

  return EXIT_SUCCESS;
}
