from typing import Dict, List, LiteralString
import os
import random

LANGUAGES_FOLDER = "../P3/languages"


def get_txt_files() -> List[LiteralString | str | bytes]:
    txt_files = []
    for root, _, files in os.walk(LANGUAGES_FOLDER):
        for file in files:
            if file.endswith('.txt'):
                txt_files.append(os.path.join(root, file))
    random.shuffle(txt_files)
    return txt_files


def read_file(path: str) -> str:
    with open(path, "r") as file:
        data = file.read()

    return data


def count_letters(data: str) -> (int, Dict[chr, int]):
    letter_count = {}

    total = 0

    for char in data:
        if char.isalpha() and char.isascii():
            total += 1
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return total, letter_count


def get_input_vector(total: int, data: Dict[chr, int]) -> List[int]:
    vector = []
    for letter in range(ord('a'), ord('z') + 1):
        try:
            vector.append(data[chr(letter)] / total)
        except KeyError:
            vector.append(0)

    return vector
