from .base_encoder import BaseEncoder
import numpy as np

class Vernam(BaseEncoder):
    __wrong_secrets = set()
    @classmethod
    def check_secret(cls, key):
        if key in cls.__wrong_secrets:
            raise AttributeError(f'Данный ключ использовался ранее! Повторное использование ключей не допускается.')

    @BaseEncoder.key.setter
    def key(self, new_key: str):
        if not isinstance(new_key, str):
            raise AttributeError(f'Ключом может быть только строка, но передан "{new_key}"')
        Vernam.check_secret(new_key)
        self._key = new_key

    def encode(self, text: str) -> str:

        def get_key() -> str:
            len_key = len(self.key)
            len_text = len(text)
            if len_key == len_text:
                return self.key
            elif len_key > len_text:
                return self.key[:len_text]
            else:
                index = 0
                new_key = self.key
                for i in range (len_key, len_text):
                    new_key += self.key[index]
                    if index < len_key-1:
                        index += 1
                    else:
                        index = 0
                return new_key

        np_text = np.array([ord(ch) for ch in text])
        key = get_key()
        np_key = np.array([ord(ch) for ch in key])
        np.cipher = np.bitwise_xor(np_text, np_key)
        cipher_text = [chr(ch) for ch in np.cipher]
        return "".join(cipher_text)

    def decode(self, text: str) -> str:
        return self.encode(text)