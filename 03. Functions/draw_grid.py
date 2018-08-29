def do_two(f):
    f()
    f()

def do_four(f):
    do_two(f)
    do_two(f)

def start_line():
    print('+', '- '*4, end='')

def end_line():
    print('+')

def draw_two_lines():
    do_two(start_line)
    end_line()

def draw_four_lines():
    do_four(start_line)
    end_line()

def start_side():
    print('|', '  '*4, end='')

def end_side():
    print('|')

def draw_two_sides():
    do_two(start_side)
    end_side()

def draw_four_sides():
    do_four(start_side)
    end_side()

def draw_grid_two_layer():
    draw_two_lines()
    do_four(draw_two_sides)

def draw_grid_four_layer():
    draw_four_lines()
    do_four(draw_four_sides)

def draw_grid():
    do_two(draw_grid_two_layer)
    draw_two_lines()

def draw_grid_four():
    do_four(draw_grid_four_layer)
    draw_four_lines()

def draw_grid_loop():
    for i in range(2):
        do_two(start_line)
        end_line()

        for i in range(4):
            do_two(start_side)
            end_side()
    
    do_two(start_line)
    end_line()

def draw_grid_four_loop():
    for i in range(4):
        do_four(start_line)
        end_line()

        for i in range(4):
            do_four(start_side)
            end_side()
    
    do_four(start_line)
    end_line()

draw_grid()
print('')
draw_grid_four()