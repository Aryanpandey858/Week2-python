"""Word Counter from Text File: count words, lines and characters."""


def count_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.splitlines()
    words = text.split()
    characters = len(text)
    return len(lines), len(words), characters


def main():
    print("=== Word Counter ===")
    filename = input("Enter file name (press Enter for sample.txt): ").strip()
    if not filename:
        filename = "sample.txt"

    try:
        lines, words, chars = count_file(filename)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    print(f"\nFile       : {filename}")
    print(f"Lines      : {lines}")
    print(f"Words      : {words}")
    print(f"Characters : {chars}")


if __name__ == "__main__":
    main()