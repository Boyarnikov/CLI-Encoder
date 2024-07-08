from .base_encoder import BaseEncoder


class Morse(BaseEncoder):
    # Словарь для кодирования символов в азбуке Морзе
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    def __init__(self, key=None):
        super().__init__(None)

    # Шифратор азбуки Морзе
    def encode(self, message):
        encrypted_message = []
        for char in message.upper():
            if char == ' ':
                encrypted_message.append('/')
            elif char in self.morse_code_dict:
                encrypted_message.append(self.morse_code_dict[char])
            else:
                encrypted_message.append(char)  # если символ не найден, оставляем его как есть
        return ' '.join(encrypted_message)

    # Дешифратор азбуки Морзе
    def decode(self, message):
        decrypted_message = []
        for code in message.split(' '):
            if code == '/':
                decrypted_message.append(' ')
            else:
                for key, value in self.morse_code_dict.items():
                    if value == code:
                        decrypted_message.append(key)
                        break
                else:
                    decrypted_message.append(code)  # если код не найден, оставляем его как есть
        return ''.join(decrypted_message)
