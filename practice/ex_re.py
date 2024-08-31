import re


def find_all_vowels_substrings(string):
    pattern = r"(?<=[bcdfghjklmnpqrstvwxyz])[aeiou]{2,}(?=[bcdfghjklmnpqrstvwxyz])"
    return [res.group() for res in re.finditer(pattern, string, flags=re.IGNORECASE)]


if __name__ == "__main__":
    input_string = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
    print(find_all_vowels_substrings(input_string))