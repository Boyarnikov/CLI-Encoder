import encoders

v = encoders.morse.Morse()
v.encode_to_file(input(), "MY_SECRET.txt")
print(v.decode_from_file("MY_SECRET.txt"))
