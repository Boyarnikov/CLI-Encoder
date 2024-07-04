from common import shift
from base_encoder import BaseEncoder


class Replacer1(BaseEncoder):
    @BaseEncoder.key.setter
    def key(self, new_key: str):
        if not isinstance(new_key, str) or len(new_key) < 3:
            raise AttributeError(f'Ключом может быть только строка длиннее 3 символов')
        self._key = new_key

    def encode(self, text: str) -> str:
        if self._key in text:
            raise AttributeError(f'Передаваемый текст содержит внутри себя ключ. Замените ключ')
        fst = [a for i, a in enumerate(text) if i % 2 == 0]
        snd = [a for i, a in enumerate(text) if i % 2 == 1]
        return self._key.join(fst + snd)

    def decode(self, text: str) -> str:
        text = text.replace(self._key, '', len(text))
        if len(text) % 2 != 0:
            tl = [a for a in text[0:int(len(text)/2)+1]]
            sl = [b for b in text[(int(len(text)/2)+1):]]
        else:
            tl = [a for a in text[0:int(len(text)/2)]]
            sl = [b for b in text[(int(len(text)/2)):]]
        cnt = 0
        src = []
        for elem in sl:
            src.append(tl[cnt])
            src.append(elem)
            cnt +=1
        if len(text) % 2 != 0:
            src.append(tl[-1])
        return ''.join(src)
