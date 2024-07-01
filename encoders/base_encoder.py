from abc import ABC, abstractmethod


class BaseEncoder(ABC):
    _key = None

    def __init__(self, key):
        self.key = key

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        self._key = new_key

    @abstractmethod
    def encode(self, text: str):
        pass

    @abstractmethod
    def decode(self, text: str):
        pass

    def encode_to_file(self, text: str, filename: str):
        with open(filename, "w", encoding="utf8") as f:
            print(self.encode(text))
            print(f)
            f.write(self.encode(text))

    def decode_from_file(self, filename: str):
        with open(filename, "r", encoding="utf8") as f:
            return self.decode(f.read())
