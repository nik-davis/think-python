def converttobinary(num):
    list = []
    while num > 0:
        remainder = num % 2
        list.insert(0, remainder)
        num = num // 2
    return list

print(converttobinary(156))