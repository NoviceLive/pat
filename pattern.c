/*
 * Copyright 2015 Gu Zhengxiong <rectigu@gmail.com>
 */


# include <stdlib.h>
# include <stdio.h>
# include <string.h>
# include <errno.h> /* For errno. */
# include <ctype.h> /* For isdigit. */

# include "mixedradix.h"
# include "libhex.h"


void
print_pattern(unsigned *length, unsigned *printed,
              char **space, unsigned digit_no,
              char *current, unsigned position);

void
print_array(int *array, unsigned int count);


int
main(int argc, char **argv)
{
  char *default_profile[] = {
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789"
  };
  unsigned int default_position_count = 3;
  char **space;
  char *keyword;
  unsigned int position_count;

  if (argc == 2) {
    space = default_profile;
    keyword = argv[1];
    position_count = default_position_count;
  }
  else if (argc > 2) {
    space = argv + 1;
    keyword = argv[argc - 1];
    position_count = argc - 1 - 1;
  }
  else {
    printf("%s\n", "Invalid Argument!");
    return EXIT_FAILURE;
  }

  for (int i = 0; i < position_count; ++i)
    printf("Position %d: %s\n", i, space[i]);

  int radices[position_count];
  get_mixed_radices(space, radices, position_count);
  int max = get_mixed_max(radices, position_count)
    * position_count + position_count;
  printf("Capacity: %d\n", max);

  if (is_type_string(keyword, isdigit)) {
    errno = 0;
    unsigned length = strtoul(keyword, NULL, 10);

    if (errno != 0) {
      perror("ERROR strtoul");
      return EXIT_FAILURE;
    }

    printf("Requested: %d\n", length);

    if (length > max) {
      printf("Invalid Length\n");
      return EXIT_FAILURE;
    }

    unsigned printed = 0;
    char current[position_count];
    current[position_count - 1] = '\0';

    printf("%s", "Pattern: ");
    print_pattern(&length, &printed, space,
                  position_count, current, 0);
    putchar('\n');
  }
  else {
    if (!memcmp(keyword, "0x", 2)) {
      printf("Hexadecimal: %s\n", keyword);
      keyword = unhex(keyword + 2);
      printf("Unhexed: %s\n", keyword);
      reverse_string(keyword, 0, strlen(keyword) - 1);
      printf("Reversed: %s\n", keyword);
    }

    if (strlen(keyword) >= position_count) {
      keyword[position_count] = 0;
      printf("Pattern: %s\n", keyword);
    }
    else {
      printf("Invalid Pattern: %s\n", keyword);
      return EXIT_FAILURE;
    }

    unsigned adjustment = 0;

    if (!check_mixed_string(keyword, space)) {
      adjustment = adjust_mixed_string(keyword, space);
      printf("Adjusted: %s\n", keyword);
      printf("Adjustment: %u\n", adjustment);

      if (!check_mixed_string(keyword, space)) {
        printf("Invalid Pattern: %s\n", keyword);
        return EXIT_FAILURE;
      }
    }

    int values[position_count];
    get_mixed_values(keyword, space, values);

    printf("%s", "Radices: ");
    print_array(radices, position_count);
    printf("%s", "Values: ");
    print_array(values, position_count);

    unsigned decimal = mixed_to_decimal(radices,
                                        values,
                                        position_count);
    unsigned offset = decimal * position_count + adjustment;
    printf("Decimal: %u\n", decimal);
    printf("Offset: %u\n", offset);
  }

  return EXIT_SUCCESS;
}


void
print_pattern(unsigned *length, unsigned *printed,
              char **space, unsigned position_count,
              char *current, unsigned position)
{
  if (position == position_count) {
    for (int i = 0; i < position_count; ++i) {
      if (*printed == *length)
        return;

      printf("%c", current[i]);
      (*printed)++;
    }
  }
  else {
    for (int i = 0; i < strlen(space[position]); ++i) {
      current[position] = space[position][i];
      print_pattern(length, printed, space,
                    position_count, current, position + 1);
    }
  }
}


void
print_array(int *array, unsigned int count)
{
  for (int i = 0; i < count - 1; ++i)
    printf("%d ", array[i]);
  printf("%d\n", array[count - 1]);
}
