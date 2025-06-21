def turn_right():
    turn_left()
    turn_left()
    turn_left() 

def walk_around():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        walk_around()
    else:
        move()
    
    
