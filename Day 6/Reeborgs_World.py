# Code for Reeborg's World
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def not_clear():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while front_is_clear():
    move()
turn_left()
while at_goal() == False:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        if front_is_clear():
            move()
    
    
   
   

    
  
    
    
