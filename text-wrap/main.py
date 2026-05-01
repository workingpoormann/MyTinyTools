import re
import textwrap


def split_text_abs(text, width=80):
    sentences = re.split(r"(?<=\.)", text)

    lines = []
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        wrapped = textwrap.wrap(
            sentence,
            width=width,
            break_long_words=False,
            break_on_hyphens=False,
        )
        lines.extend(wrapped)

    return "\n\n\n".join(lines)


def load_text(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def main():
    text = load_text("in.txt")
    s = split_text_abs(text, 80)

    with open("out.txt", "w") as f:
        f.write(s)


if __name__ == "__main__":
    main()
