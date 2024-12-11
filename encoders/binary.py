from base_encoder import BaseEncoder

class BinaryEncoder(BaseEncoder):
    def __init__(self, _key):
        super().__init__(_key)

    def encode(self, text: str):
        return ' '.join(format(ord(char), '08b') for char in text)

    def decode(self, text: str):
        return ''.join(chr(int(char, 2)) for char in text.split())

# Создаем экземпляр класса BinaryEncoder
key = 123
binary_encoder = BinaryEncoder(key)

# Ввод текста для шифрования
original_text = input("Введите текст для шифрования: ")

# Шифруем текст
binary_encoded = binary_encoder.encode(original_text)
print("Зашифрованный текст в двоичном виде:")
print(binary_encoded)

# Дешифруем текст
decoded_text = binary_encoder.decode(binary_encoded)
print("Дешифрованный текст:")
print(decoded_text)
