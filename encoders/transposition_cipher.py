from encoders.base_encoder import BaseEncoder


class TranspositionCipher(BaseEncoder):

    @BaseEncoder.key.setter
    def key(self, new_key: int):
        if not isinstance(new_key, int):
            raise AttributeError(f'Ключом может быть только целое число, но получен "{new_key}"')
        self._key = new_key

    def encode(self, text: str) -> str:

        # text = text.replace(" ", "")

        num_rows = len(text) // self.key
        if len(text) % self.key != 0:
            num_rows += 1

        matrix = [[' ' for _ in range(self.key)] for _ in range(num_rows)]

        index = 0
        for col in range(self.key):
            for row in range(num_rows):
                if index < len(text):
                    matrix[row][col] = text[index]
                    index += 1

        encrypted_message = ""
        for row in range(num_rows):
            for col in range(self.key):
                encrypted_message += matrix[row][col]

        return encrypted_message

    def decode(self, text: str) -> str:

        num_rows = len(text) // self.key
        if len(text) % self.key != 0:
            num_rows += 1

        matrix = [[' ' for _ in range(self.key)] for _ in range(num_rows)]

        index = 0
        for row in range(num_rows):
            for col in range(self.key):
                if index < len(text):
                    matrix[row][col] = text[index]
                    index += 1

        decrypted_message = ""
        for col in range(self.key):
            for row in range(num_rows):
                decrypted_message += matrix[row][col]

        # decrypted_message = decrypted_message.replace(" ", "")
        decrypted_message = decrypted_message.rstrip()

        return decrypted_message
