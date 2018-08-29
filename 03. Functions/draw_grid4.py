def draw_line():
    print('+ ', end='')
    print('- '*4, end='')
    print('+ ', end='')
    print('- '*4, end='')
    print('+')
    #print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')

def start_line():
    print('+', '- '*4, end='')

def end_line():
    print('+')

def start_side():
    print('|', '  '*4, end='')

def end_side():
    print('|')

def draw_side():
    do_twice(start_side)
    do_twice(start_side)
    end_side()

def do_twice(func):
    func()
    func()

def do_four(func):
    do_twice(func)
    do_twice(func)

def draw_grid():
    do_four(start_line)
    end_line()

    do_four(draw_side)

    do_four(start_line)
    end_line()

    do_four(draw_side)

    do_four(start_line)
    end_line()

    do_four(draw_side)

    do_four(start_line)
    end_line()

    do_four(draw_side)

    do_four(start_line)
    end_line()


draw_grid()