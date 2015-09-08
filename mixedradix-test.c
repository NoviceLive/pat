/*
 * Copyright 2015 Gu Zhengxiong <rectigu@gmail.com>
 */


# include <stdlib.h>
# include <stdio.h>

# include "mixedradix.h"


int
main(int argc, char **argv)
{
  if (argc == 1 || (argc - 1) % 2 != 0) {
    printf("Invalid Argument Count: %d!\n", argc);
    return EXIT_FAILURE;
  }

  int radices[argc];
  int values[argc];
  int mid = (argc - 1) / 2;

  for (int i = 1; i <= mid; ++i) {
    radices[i - 1] = strtoul(argv[i], NULL, 10);
  }
  for (int i = mid + 1; i < argc; ++i) {
    values[i - 1 - (argc - 1) / 2] = strtoul(argv[i], NULL, 10);
  }

  printf("%d\n", mixed_to_decimal(radices, values, (argc - 1) / 2));

  return EXIT_SUCCESS;
}
