from encoders.base_encoder import BaseEncoder

MORSE_CODE_DICT = { '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',
                    'А':'.-', 'Б':'-...', 'В':'.--', 'Г':'--.', 'Д':'-..', 'Е':'.',
                    'Ж':'...-', 'З':'--..', 'И':'..', 'Й':'.---', 'К':'-.-',
                    'Л':'.-..', 'М':'--', 'Н':'-.', 'О':'---', 'П':'.--.',
                    'Р':'.-.', 'С':'...', 'Т':'-', 'У':'..-', 'Ф':'..-.',
                    'Х':'....', 'Ц':'-.-.', 'Ч':'---.', 'Ш':'----', 'Щ':'--.-.',
                    'Ъ':'.-.-', 'Ы':'-.--', 'Ь':'-..-', 'Э':'..-..', 'Ю':'..--',
                    'Я':'.-.-'
                    }

REVERSE_MORSE_CODE_DICT = {}  # Обычный словарь dict
for key, value in MORSE_CODE_DICT.items():
    REVERSE_MORSE_CODE_DICT[value] = key

class MorseEncoder(BaseEncoder):
    def __init__(self, key=None):
        super().__init__(key)

    def encode(self, text: str):
        morse_code = ''
        text = text.upper()
        for letter in text:
            if letter != ' ':
                morse_code += MORSE_CODE_DICT.get(letter, '#') + ' '
            else:
                morse_code += ' / '
        return morse_code.strip()

    def decode(self, text: str):
        text = text.strip()
        morse_words = text.split(' / ')
        plain_text = ''
        for morse_word in morse_words:
            morse_letters = morse_word.split(' ')
            for morse_letter in morse_letters:
                plain_text += REVERSE_MORSE_CODE_DICT.get(morse_letter, ' ')
            plain_text += ' '
        return plain_text.strip()
