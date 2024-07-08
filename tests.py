import unittest
import logging
import sys
from encoders import Caesar
from encoders import Vigenere
from encoders import Morse

CAESAR_CORRECT_KEYS = [1, 2, 3, 5]
CAESAR_WRONG_KEYS = ["hello", 2.5]

VIGENERE_CORRECT_KEYS = ["hello", "world"]
VIGENERE_WRONG_KEYS = [3, 10, "12345"]

MORSE_CORRECT_KEYS = [None]

TEST_TEXTS = ["hello world!", "Привет мир!", "asofhpoauewh230u80934t97h"]


class KeyTests(unittest.TestCase):
    def test_caesar_key_validation(self):
        for key in CAESAR_CORRECT_KEYS:
            test_caesar = Caesar(key)

        for key in CAESAR_WRONG_KEYS:
            try:
                test_caesar = Caesar(key)
            except AttributeError:
                pass
            else:
                raise AssertionError("Создали цезаря с некорректным ключом")

    def test_vigenere_key_validation(self):
        for key in VIGENERE_CORRECT_KEYS:
            encoder = Vigenere(key)

        for key in VIGENERE_WRONG_KEYS:
            try:
                encoder = Vigenere(key)
            except AttributeError:
                pass
            else:
                raise AssertionError("Создали вижинера с некорректным ключом")


class EncodeDecodeTests(unittest.TestCase):
    ENCODERS = [(Caesar, CAESAR_CORRECT_KEYS),
                (Vigenere, VIGENERE_CORRECT_KEYS),
                (Morse, MORSE_CORRECT_KEYS)]

    def test_encode_decode(self):
        for Encoder, keys in self.ENCODERS:
            for key in keys:
                with self.subTest(f"Тестируем {Encoder} с ключом {key}"):
                    encoder = Encoder(key)
                    for text in TEST_TEXTS:
                        encoded_decoded_text = encoder.decode(encoder.encode(text))
                        self.assertEqual(text.lower(), encoded_decoded_text.lower(), "Шифр не вернул изначальный текст")