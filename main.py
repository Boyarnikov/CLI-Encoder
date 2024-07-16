import encoders

#v = encoders.vigenere.Vigenere("fog")
#v.encode_to_file(input(), "MY_SECRET.txt")
#print(v.decode_from_file("MY_SECRET.txt"))

v=encoders.atbash.Atbash()
v.encode_to_file(input(), "MY_SECRET.txt")
print(v.decode_from_file("MY_SECRET.txt"))
#
# try:
#     1/int(input())
#     print("Поделилось!")
# except ZeroDivisionError:
#     print("Кто-то поделил на ноль!!")
# except ValueError:
#     print("Не получилось превратить в число!")
# else:
#     print("Как здорово что ничего не сломалось!")
# finally:
#     print("А теперь я спать")