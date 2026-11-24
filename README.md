[![make.fun · u-eager-stork-81-9647-the-funniest-toaster-error-436406cd](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![make.fun · rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/kharlla273/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![make.fun · reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/kharlla273/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

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
