from .base_encoder import BaseEncoder


class Atbash(BaseEncoder):
    def __init__(self, key=None):
        super().__init__(key)

    def encode(self, text: str) -> str:
        return self._atbash(text)

    def decode(self, text: str) -> str:
        return self._atbash(text)

    def _atbash(self, text: str) -> str:
        result = []
        for char in text:
            if 'a' <= char <= 'z':  # English lowercase
                result.append(chr(219 - ord(char)))  # 'a' + 'z' = 219
            elif 'A' <= char <= 'Z':  # English uppercase
                result.append(chr(155 - ord(char)))  # 'A' + 'Z' = 155
            elif 'а' <= char <= 'я':  # Russian lowercase
                result.append(chr(ord('я') + ord('а') - ord(char)))  # Reverse Russian lowercase
            elif 'А' <= char <= 'Я':  # Russian uppercase
                result.append(chr(ord('Я') + ord('А') - ord(char)))  # Reverse Russian uppercase
            else:
                result.append(char)  # Non-alphabetical characters remain unchanged
        return ''.join(result)