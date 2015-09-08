/*
 * Copyright 2015 Gu Zhengxiong <rectigu@gmail.com>
 */


# include <stdlib.h>
# include <stdio.h>

# include "libhex.h"

int
main(int argc, char **argv)
{
  if (argc != 2) {
    printf("%s\n", "Invalid Argument!");
    return EXIT_FAILURE;
  }

  printf("%s\n", unhex(argv[1]));

  return EXIT_SUCCESS;
}
