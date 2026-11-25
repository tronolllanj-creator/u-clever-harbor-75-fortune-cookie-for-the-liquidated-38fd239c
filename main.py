import os
import sys


def main() -> None:
    """Write a fortune cookie line for a liquidated trader to $MAKEFUN_OUTPUT_DIR/entry.txt."""
# Entry validated: output is 1-160 chars, one line, at most 20 words, deterministic.
    FORTUNE = "You will find peace in HODLing. Your position found peace in zero."
    content = FORTUNE + "\n"

    # Validate
    stripped = content.strip()
    if not (1 <= len(content) <= 160):
        raise ValueError(f"content length {len(content)} not in 1..160")
    if not stripped:
        raise ValueError("content is only whitespace")
    if stripped != stripped.replace(chr(10), ''):
        raise ValueError("content has more than one line")
    word_count = len(stripped.split())
    if not (1 <= word_count <= 20):
        raise ValueError(f"word count {word_count} not in 1..20")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Output path: {output_path}")
    print(f"Character count: {len(content)}")
    print(f"Word count: {word_count}")
    print(f"Fortune: {FORTUNE}")


if __name__ == "__main__":
    main()
