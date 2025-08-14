#this is the main class
#Im planning to use this class as a base 
#i think im going to use inheritance for the ammount of rovers needing to land in mars

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
        self.direction_list = ("N","E","S","W")
        self.rover_coordinates = [self.x, self.y]

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
        #keep the cords list up to date so it doesnt go out of sync
        self.rover_coordinates = [self.x, self.y]


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


#this runs the whole mars rover game, reading inputs and moving the rover around
def main():
    while True:
        #get the platue size2 i tries to split this up into parts that make sence
        try: #i thought putting these if try and except blcks would make the program clean

            #This gets the two platoe sizes
            print('please seperate the coordinates with a space')
            platue_size = input("Enter the upper coordinates of the plateau : ").strip()

            platue_parts = platue_size.split()

            if len(platue_parts) != 2:
                print("need 2 numbers like '3 3' (not with commas)")
                continue

            max_x = int(platue_parts[0])
            max_y = int(platue_parts[1])

            if max_x <= 0 or max_y <= 0:# this makes shure that only 1 can be positive 
                #this prevents the platoe being to small and giving negative errors
                print('please input coordinates that are above 0')
                continue

            break

        except:
            print("please enter two numbles for example '3 3' ")
            #simply if user inputs wrong things, the loop will go again returning an error

    while True:
        try:
            #pretty much a tutorial for how to run
            print("x and y are the rovers position on the platue\nD is the starting direction the rover is faceing")

            #get the user input
            start_line = input("Enter the rovers position like 'x y D' : ").strip()
            parts = start_line.split() #e.g. ["1", "2", "N"]

            #check we got 3 values
            if len(parts) != 3:
                print("wrong number of things entered")
                continue

            #this part assigns the values to names after theya re split into diferent segments 
            x_text = parts[0]
            y_text = parts[1]
            dir_text = parts[2]
            #convert coords to numbers
            start_x = int(x_text)
            start_y = int(y_text)
            #format dir to uppercase
            start_dir = dir_text.upper()

            #check the direction is valid
            if start_dir not in ("N", "E", "S", "W"):
                print("invalid direction")
                continue

            break#if the imput is vaid we can break out of the loop 
        except:
            print("please enter 2 numbers and a direction like '3 3 E'")

   
    #make the rover (using my class as a base)    
    rover = Rover(start_x, start_y, start_dir, [start_x, start_y])
    
    if not rover.check_start(max_x, max_y):
        print('start is off the platoe, please start again ...')
        return
    #get the instructions to make the rover walk about
    commands_line = input("Enter the series of instructions (L/R/M) : ").strip()

    #turn the string of commands into a list so we can go one by one
    commands_list = list(commands_line.upper())#this is were the magic happens
    #the list function splits all of the grouped values into a list of values

    #run the instructions one at a time, rover finishes before next one starts
    for c in commands_list:# this is a realy simple way of reading complex lines of strings
        if c == "L":
            rover.turn_left()
        elif c == "R":
            rover.turn_right()
        elif c == "M":
            #only move if the move is safe on the platue
            if rover.check_move(max_x, max_y):
                rover.move()
            else:
                #if it cant move just ignore it (or we could print somthing here)
                pass

    #output the final cords and heading
    print(rover.x, rover.y, rover.direction)


if __name__ == "__main__":
    #this is mucode so fat
    main()

