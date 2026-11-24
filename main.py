"""Monday, Reviewed in One Line.

Writes a single one-line review of my own Monday to /output/entry.txt.

Why the line is funny: Monday is personified as a coworker who brews my
coffee, drinks it himself, and then — with a straight face — books a
meeting about *my* caffeine problem. The blame lands on the wrong person,
the detail (coffee + a meeting) is concrete, and the whole joke turns
inside one short sentence, easy to repeat to a coworker the next morning.
The line is fixed text: no randomness, no network, no input — every run
writes the exact same 93 characters.
"""

LINE = "One star. Monday brewed my coffee, drank it, then booked a meeting about my caffeine problem."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    try:
        import os

        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        import os

        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
