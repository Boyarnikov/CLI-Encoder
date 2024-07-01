import string


def letter_range(ch1: str, ch2: str) -> str:
    return "".join([chr(i) for i in range(ord(ch1), ord(ch2) + 1)])


ENG_LETTERS_UPPER = string.ascii_uppercase
ENG_LETTERS_LOWER = string.ascii_lowercase
RUS_LETTERS_UPPER = letter_range("А", "Я")
RUS_LETTERS_LOWER = letter_range("а", "я")
ALL_LETTERS = [ENG_LETTERS_UPPER, ENG_LETTERS_LOWER, RUS_LETTERS_UPPER, RUS_LETTERS_LOWER]


def shift(ch: str, shift_amount: int):
    for letters in ALL_LETTERS:
        index = letters.find(ch)
        if index != -1:
            new_index = (index + shift_amount) % len(letters)
            new_ch = letters[new_index]
            return new_ch
    return ch


def encode(text: str) -> str:
    return "".join(shift(ch, 3) for ch in text)


def decode(text: str) -> str:
    return "".join(shift(ch, -3) for ch in text)
