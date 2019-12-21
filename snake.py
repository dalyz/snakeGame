import random
import curses 

# initialized curses by returning a window object
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

stdscr.keypad(True)

curses.curs_set(0)
height, width = stdscr.getmaxyx()
# create a new window of a given size
window = curses.newwin(height, width, 0, 0)
window.keypad(1)
window.timeout(100)

# snake's form
snk_x = width/4
snk_y = height/2

# initialize snake's size to 3
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# food's size
food = [height/2, width/2]

# add first food in the window
window.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# snake initializes direction to right
key = curses.KEY_RIGHT

# main of snake game 
while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, height] or snake[0][1] in [0, width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [ random.randint(1, height-1), random.randint(1, width-1)]
            food = nf if nf not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(int(tail[0]), int(tail[1]), ' ')
        
    window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
    