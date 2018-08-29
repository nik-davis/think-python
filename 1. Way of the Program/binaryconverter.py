def converttobinary(num):
    # list = []
    binary_str =''
    while num > 0:
        remainder = num % 2
        binary_str = str(remainder) + binary_str
        # list.insert(0, remainder)
        num = num // 2
    return binary_str

print(converttobinary(156))
