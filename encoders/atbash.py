def atbash_cipher(text, language='english'):
    result = ""
    if language == 'english':
        for char in text:
            if char.isalpha():
                if char.islower():
                    result += chr(122 - ord(char) + 97)
                else:
                    result += chr(90 - ord(char) + 65)
            else:
                result += char
    elif language == 'russian':
        for char in text:
            if char.isalpha():
                if char.islower():
                    result += chr(1103 - ord(char) + 1072)
                else:
                    result += chr(1071 - ord(char) + 1040)
            else:
                result += char
    return result

# Пример использования для английского
original_text = "Hello, World!"
encrypted_text = atbash_cipher(original_text.lower(), 'english')
decrypted_text = atbash_cipher(encrypted_text, 'english')
print("Original:", original_text)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)

# Пример использования для русского
original_text_ru = "Привет, мир!"
encrypted_text_ru = atbash_cipher(original_text_ru.lower(), 'russian')
decrypted_text_ru = atbash_cipher(encrypted_text_ru, 'russian')
print("Original (RU):", original_text_ru)
print("Encrypted (RU):", encrypted_text_ru)
print("Decrypted (RU):", decrypted_text_ru)
