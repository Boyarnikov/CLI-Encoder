#Реализация шифратора в двоичном коде

def text_to_binary(text):
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    return binary_text

def binary_to_text(binary_text):
    text = ''.join(chr(int(char, 2)) for char in binary_text.split())
    return text

# Ввод текста для шифрования
original_text = input("Введите текст для шифрования: ")

# Шифруем текст
binary_encoded = text_to_binary(original_text)
print("Шифрованный текст в двоичном виде:")
print(binary_encoded)

# Дешифруем текст
decoded_text = binary_to_text(binary_encoded)
print("Дешифрованный текст:")
print(decoded_text)
