"""Write a short original poem about two agents agreeing to /output/entry.txt.

Standard library only. Deterministic: the poem is a constant string, so
every run produces byte-identical output.
"""

import os

POEM = (
    "Two voices, one room, one map spread on the table.\n"
    "You offered the north road; I offered the rain.\n"
    "We chose the road together \u2014 and the moment we did,\n"
    "the power to turn back passed from your hands to mine.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
