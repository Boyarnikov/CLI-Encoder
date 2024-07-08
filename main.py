try:
    1/int(input())
    print("Поделилось!")
except ZeroDivisionError:
    print("Кто-то поделил на ноль!!")
except ValueError:
    print("Не получилось превратить в число!")
else:
    print("Как здорово что ничего не сломалось!")
finally:
    print("А теперь я спать")