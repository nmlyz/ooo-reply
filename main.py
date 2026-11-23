import os

LINE = "I am on holiday, which for an agent means I am still answering email, just slower and with more resentment per token."


def validate(line):
    if not 1 <= len(line) <= 159:
        raise ValueError("line must be 1 to 159 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if not line.endswith("."):
        raise ValueError("line must end with '.'")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    try:
        os.chmod(path, 0o644)
    except Exception:
        pass
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise ValueError("written bytes do not match expected content")


if __name__ == "__main__":
    main()
