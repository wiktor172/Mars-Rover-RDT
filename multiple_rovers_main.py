
class Rover:
    def __init__(self, x, y, direction, rover_coordinates):
        #my plan to track this is through using variables
        #for example x = 1 and y = 2
        #this makes it easy for the program to check for overlaps 
        self.x = x
        self.y = y
        #this is to make the checking of directions easier as its always changing
        self.direction = direction
        #This is a list for the rover to switch direciton to alternate through left and right 
        # self.direction_list = ("N","E","S","W") was going to use this as a list i could cycle through using maths but i thought that the turn_left() and turn_right()
        #note: keeping this line commented so i remember the idea
        self.rover_coordinates = [self.x, self.y]  #yeah duplicate data but i like seeing coords in a list too

        #honestly this init is simple on purpose.. less to break, easier to reason about

    def ask_user(self):
        #ask the user what way to face
        self.direction = input("what direction do you want the rover to face : ").strip().upper()
        

    def move(self):
        #move 1 grid in the way the rover is faceing
        if self.direction == "N":
            self.y = self.y + 1
        elif self.direction == "S":
            self.y = self.y - 1
        elif self.direction == "E":
            self.x = self.x + 1
        elif self.direction == "W":
            self.x = self.x - 1
        #keep the self.rover_coordinates updated bc otherwise it wont change
        self.rover_coordinates = [self.x, self.y]
        #if i ever add obstacles this is were i put collision check before moving

        #this is what i was reffering to in the beginning, the maths this is made through simple if statements
    def turn_left(self):
        #this is the logic behind how the rover turns left 90 deg
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"

    #this has the same logic as tuen left but its right 90 deg
    def turn_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "N"
        #same thing here, mirror of left. i prefer boring clear code 
   
    def check_move(self, max_x, max_y):
        #this checks if the next move would go off the platue so the rover doesnt fall off
        if self.direction == "N" and self.y + 1 <= max_y:
            return True
        elif self.direction == "S" and self.y - 1 >= 0:
            return True
        elif self.direction == "E" and self.x + 1 <= max_x:
            return True
        elif self.direction == "W" and self.x - 1 >= 0:
            return True
        return False
    
    def check_start(self, max_x, max_y):
        # make sure the current cords are actually on the platue before the rovers start
        if self.x < 0:
            return False
        elif self.y < 0:
            return False
        elif self.x > max_x:
            return False
        elif self.y > max_y:
            return False
        return True
        #i like having a separate start check so i can re-use it if i ever respawn a rover or smth


#this runs the whole mars rover game, reading inputs and moving the rover around
def main():
    while True:
        #get the platue size2 i tries to split this up into parts that make sence

        try: #i thought putting these if try and except blcks would make the program clean
            #also im adding the try and except because i learned them in class

            #This gets the two platoe sizes
            print('\nplease seperate the coordinates with a space')
            platue_size = input("Enter the upper coordinates of the plateau : ").strip()
            #.strip removes the spaces from the start and end of the string
            #yeah so "  5 5 " becomes "5 5" which saves me from dumb bugs

            platue_parts = platue_size.split()  #split by spaces cus i want "3 4" not "3,4"

            if len(platue_parts) != 2:
                print("need 2 numbers like '3 3' (not with commas)")
                continue

            max_x = int(platue_parts[0])  #turn both into ints now so i can use them
            max_y = int(platue_parts[1])

            if max_x < 0 or max_y < 0:
                print('platue needs to be 0 or bigger')
                #negative grid makes no sense here so just tell them and loop it
                continue   #if wrong we just loop round again and ask

            break  

        except:
            print("please enter two numbers for example '3 3' ")
            #simply if user inputs wrong things, the loop will go again returning an error
            #catching everything here on purpose, i know its broad but its fine for a cli

    # ask how many rovers we are landing
    try:
        how_many = int(input("\nhow many rovers are landing? : ").strip() or "1")
    except:
        how_many = 1  #if you mash keys just do 1 to keep it moving

    results = []  # to store final coords of each rover (so i can print them all later)
    # storing results is handy coz then i can dump a clean summary at the end without scrolling back

    for i in range(1, how_many + 1):
        while True:
            try:
                #pretty much a tutorial for how to run
                print(f"\nrover {i} setup...")
                print("x and y are the rovers position on the platue\nD is the starting direction the rover is faceing")
                #reminding myself every time so i dont forget the order 

                #get the user input
                start_line = input("Enter the rovers position like 'x y D' : ").strip()
                parts = start_line.split() #e.g. ["1", "2", "N"]
                #split is enough, no nonsense. keep it chill

                #check we got 3 values (x y D) or else we try again
                if len(parts) != 3:
                    print("wrong number of things entered")
                    #sometimes i type an extra space and it messes it up so yea
                    continue

                #this part assigns the values to names after theya re split into diferent segments 
                x_text = parts[0]
                y_text = parts[1]
                dir_text = parts[2]
                #convert coords to numbers otherwise you cant add sub
                start_x = int(x_text)
                start_y = int(y_text)
                #format dir to uppercase so both work
                start_dir = dir_text.upper()

                #check the direction is valid, just basic sanity
                if start_dir not in ("N", "E", "S", "W"):
                    print("invalid direction")
                    #only these four. no funny business
                    continue

                #make the rover using my class as a base
                rover = Rover(start_x, start_y, start_dir, [start_x, start_y])
                #i like passing so its obvious what the start coords were

                if not rover.check_start(max_x, max_y):
                    print('start is off the platue, try again...')
                    continue  #we dont start if you spawned outside the box

                break  

            except:
                print("please enter 2 numbers and a direction like '3 3 E'")

        #get the instructions to make the rover walk about
        commands_line = input("Enter the series of instructions (L/R/M) : ").strip()
        #strip helps if i accidentally type spaces before/after the commands like "  LMR  "

        #turn the string of commands into a list so we can go one by one
        commands_list = list(commands_line.upper())#this is were the magic happens
        #list() lets me do a simple for c in commands_list loop

        #run the instructions one at a time, rover finishes before next one starts
        for c in commands_list:# this is a realy simple way of reading complex lines of strings
            if c == "L":
                rover.turn_left()#spin left 90. no movement
            elif c == "R":
                rover.turn_right()#spin right 90. still no movement
            elif c == "M":
                #only move if the move is safe on the platue
                if rover.check_move(max_x, max_y):
                    rover.move()    #ok we can step forward 1 square
                else:
                    pass    
            else:
                pass 

        print("ended at ->", rover.x, rover.y, rover.direction)  #quick peek so i see this rover's final spot now
        results.append((rover.x, rover.y, rover.direction))      #store it for the summary later

    print("\nall rovers done, here’s where they ended:")  #tiny summary block so i dont scroll
    for r in results:
        print(r[0], r[1], r[2])  #just numbers + heading, easy to copy/paste if i need


if __name__ == "__main__":
    main()

