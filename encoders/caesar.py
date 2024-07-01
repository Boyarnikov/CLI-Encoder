from common import shift
from base_encoder import BaseEncoder


class Caesar(BaseEncoder):
    @BaseEncoder.key.setter
    def key(self, new_key: int):
        if not isinstance(new_key, int):
            raise AttributeError(f'Ключом может быть только целое число, но передан "{new_key}"')
        self._key = new_key

    def encode(self, text: str) -> str:
        return "".join(shift(ch, self.key) for ch in text)

    def decode(self, text: str) -> str:
        return "".join(shift(ch, -self.key) for ch in text)
