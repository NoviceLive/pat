# Pat 0.5.0 - March 17, 2016

## What's New

- Added `[]` syntax.
- Added colorized logging and options `-v` and `-q`.
- Added i18n stub.

## What's Different

- Changed API names.

  - `Pat.create_pattern` -> `Pat.create`
  - `Pat.locate_pattern` -> `Pat.locate`

- Raised errors instead of returning `None` on failure.

  - `IndexError` from `Pat.create`
  - `KeyError` from `Pat.locate`


# Pat 0.4.1 - March 6, 2016

## What's New

- Added CLI flag `-b` / `--big-endian`.

## Fixed Bugs

- Considered endianness, fixing #3.
