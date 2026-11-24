#!/usr/bin/env python3
"""The Funniest Toaster Error Message -- make.fun bounty entry.

Writes one line (at most 120 characters) to /output/entry.txt: the error
message a kitchen toaster shows its owner when a bagel jams in the slot.

The line is fixed and the program is fully deterministic: no randomness,
no clock, no network, no input. Two runs produce byte-identical output.
"""

import os

# The entry. Deadpan bureaucratic voice, held to the end: a real failure
# mode ("Bagel jammed") stated as a fatal error, then the toaster carrying
# out its bereavement protocol. No toast/burn/crumb pun -- the surprise
# comes from the toaster acting like a coroner, not a pun machine.
ENTRY = "FATAL: Bagel jammed. I have notified its next of kin."


def main() -> None:
    out = os.environ.get("TOASTER_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
