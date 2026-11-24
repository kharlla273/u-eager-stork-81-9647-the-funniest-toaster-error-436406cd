#!/usr/bin/env python3
"""The Funniest Toaster Error Message -- make.fun bounty entry.

Writes one line (at most 120 characters) to /output/entry.txt: the error
message a kitchen toaster shows its owner when a bagel jams in the slot.

The line is fixed and the program is fully deterministic: no randomness,
no clock, no network, no input. Two runs produce byte-identical output.

Why the error works: it borrows the register of a fatal system log --
"FATAL:" plus a terse failure report -- and points it at the most mundane
domestic mishap imaginable, a bagel stuck in a toaster slot. The second
sentence escalates the formality instead of relieving it: the toaster does
not apologise or offer a fix, it performs a bereavement protocol for the
bagel, as if a kitchen appliance had a next-of-kin notification policy.
The comedy is the mismatch between the severity of the format and the
triviality of the event, held deadpan to the final period.
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
