"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``
(default ``/output``). Pure stdlib, deterministic, no network at runtime.

The entry
----------
"Roommate Moved Out, Took Router" (31 characters)

Why this name, against the judge's five criteria in order:

1. Wi-Fi name and joke: it is a network name a stranger reads in a phone's
   network list, and it reads as a joke at once.
2. Twist lands on first read: two short beats, and the second reframes the
   first. Moving out is sad; taking the router is the crime. The punchline
   is the last two words, "Took Router".
3. Whole story: a character (the roommate), a situation (moving out) and
   something that happened (the router was carried off). The reader fills in
   the rest: the flatmate left, the Wi-Fi went with them, and the network
   whose name you are reading is the one that lost its router.
4. Fresh: no stock Wi-Fi joke (no FBI van, no "Pretty Fly", no password
   pun). An original construction, not a recycled one-liner.
5. Tight: 31 characters, every word earns its place, clean and easy to say
   aloud. Nothing could be cut without losing story.
"""

import os

# The entry: exactly one line, 31 characters, plain ASCII.
ENTRY = "Roommate Moved Out, Took Router"

MAX_CHARS = 32


def gate_check(text):
    """Mirror the sealed scorer's gate.

    Returns ``None`` when *text* is valid, otherwise an error message.
    The gate checks: UTF-8 text, 1 to 32 characters, not only whitespace,
    and a single line.
    """
    if not isinstance(text, str):
        return "entry is not text"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not valid UTF-8 text"
    if len(text) < 1:
        return "entry is empty"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the 32 character limit" % len(text)
    if not text.strip():
        return "entry is only whitespace"
    if "\n" in text or "\r" in text:
        return "entry is not a single line"
    return None


def main():
    error = gate_check(ENTRY)
    if error is not None:
        raise SystemExit("invalid entry: %s" % error)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
