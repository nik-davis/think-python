# As an exercise, write a function that takes a string as an argument
# and displays the letters backward, one per line

def forward(string):
    index = 0
    while index < len(string):
        letter = string[index]
        print(letter)
        index += 1

def reverse(string):
    index = 1
    while index < len(string) + 1:
        letter = string[-index]
        print(letter)
        index += 1

def reverse_alt1(string):
    index = 0
    while abs(index) < len(string):
        letter = string[index-1]
        print(letter)
        index -= 1

def reverse_alt2(string):
    index = len(string) - 1
    while index > -1:
        letter = string[index]
        print(letter)
        index -= 1

forward('Hello World!')
reverse('Hello World!')
reverse_alt1('Hello World!')
reverse_alt2('Hello World!')
