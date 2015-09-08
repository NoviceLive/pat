/*
 * Copyright 2015 Gu Zhengxiong <rectigu@gmail.com>
 */


# include <stdlib.h>
# include <stdio.h>
# include <string.h>

# include "mixedradix.h"


int
main(int argc, char **argv)
{
  if (argc < 2) {
    printf("%s\n", "Incorrect Argument Number!");
    return EXIT_FAILURE;
  }

  size_t length = strlen(argv[1]);

  for (int i = 0; i < length * 2; ++i) {
    char test[length];
    strcpy(test, argv[1]);
    printf("0 %d %s %s\n",
           i, argv[1], left_rotate_string(test, i));
  }

  return EXIT_SUCCESS;
}
