# The built-in function eval takes a string and evaluates it using the 
# Python interpreter. Write a function called eval_loop that iteratively
# prompts the user, takes the resulting input and evaluates it using eval,
# and prints the result. It should continue until the user enters 'done', 
# and then return the value of the last expression it evaluated.

def eval_loop():
    eval_value = None

    while True:
        user_input = input('> ')
        if user_input == 'done':
            return eval_value
            break
        eval_value = eval(user_input)
        print(eval_value)
        

print('Return value:' , eval_loop())