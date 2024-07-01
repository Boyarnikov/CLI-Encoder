from encoders.caesar import Caesar

v = Caesar(5)
v.encode_to_file(input(), "MY_SECRET.txt")
v.decode_from_file("MY_SECRET.txt")
