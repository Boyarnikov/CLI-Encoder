from common import shift
from base_encoder import BaseEncoder


class Replacer(BaseEncoder):
    @BaseEncoder.key.setter
    def key(self, new_key: str):
        if not isinstance(new_key, str) or len(new_key) < 3:
            raise AttributeError(f'Ключом может быть только строка длиннее 3 символов')
        self._key = new_key

    def encode(self, text: str) -> str:
        if self._key in text:
             raise AttributeError(f'Передаваемый текст содержит внутри себя ключ. Замените ключ')
        fst = [a for i, a in enumerate(text)]
        return self._key.join(fst)[::-1]

    def decode(self, text: str) -> str:
        text = text[::-1].replace(self._key, '', len(text))
        return ''.join(text)



