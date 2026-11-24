# The Funniest Toaster Error Message

A kitchen toaster, deadpan to the end:

> FATAL: Bagel jammed. I have notified its next of kin.

## Run it

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (override with `TOASTER_OUTPUT`).
Deterministic: the same bytes on every run, no network, no input.

## Why this line

- A real error format for a real failure mode: a bagel jammed in the slot.
- The surprise is not a toast pun. The toaster responds like a coroner
  carrying out a bereavement protocol.
- 53 characters, one voice, understood on a single read.
