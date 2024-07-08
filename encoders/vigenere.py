from .common import shift, get_index
from .base_encoder import BaseEncoder


class Vigenere(BaseEncoder):
    @BaseEncoder.key.setter
    def key(self, new_key: str):
        if not isinstance(new_key, str) or len(new_key) == 0:
            raise AttributeError(f'Ключом может быть только непустая строка, но получен "{new_key}"')
        for ch in new_key:
            if get_index(ch) == -1:
                raise AttributeError(f'Символ "{ch}" не индексируем')
        self._key = new_key

    def encode(self, text: str) -> str:
        return "".join(shift(
            text[i],
            get_index(self.key[i % len(self.key)]) + 1
        ) for i in range(len(text)))

    def decode(self, text: str) -> str:
        return "".join(shift(
            text[i],
            - get_index(self.key[i % len(self.key)]) - 1
        ) for i in range(len(text)))
