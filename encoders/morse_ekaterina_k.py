from encoders.base_encoder import BaseEncoder


class Morse(BaseEncoder):
    dictionary = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ж': '...-', 'з': '--..',
                  'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.',
                  'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.',
                  'ш': '----', 'щ': '--.-', 'ъ': '.--.-.', 'ы': '-.--', 'ь': '-..-', 'э': '...-...', 'ю': '..--',
                  'я': '.-.-'}

    def __init__(self):
        super().__init__(None)

    def encode(self, text: str) -> str:
        encoded_text = ''
        for letter in text:
            if letter == ' ':
                encoded_text = encoded_text+' '
            else:
                for k, v in Morse.dictionary.items():
                    if letter.lower() == k:
                        encoded_text = encoded_text+v+'/'
        return encoded_text

    def decode(self, text: str) -> str:
        decoded_text = ''
        letter = ''
        for symbol in text:
            if symbol == ' ':
                decoded_text = decoded_text+' '
            else:
                if symbol != '/':
                    letter = letter+symbol
                else:
                    for k, v in Morse.dictionary.items():
                        if letter == v:
                            decoded_text = decoded_text+k
                            letter = ''
        return decoded_text