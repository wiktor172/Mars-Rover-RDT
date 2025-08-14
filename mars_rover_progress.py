# this is the main class
# Im planning to use this class as a base 
# i think im going to use inheritance for the ammount of rovers needing to land in mars

class Rover:
    def __init__(self, x, y, direction, rover_coordinates):
        # my plan to track this is through using variables
        # for example x = 1 and y = 2
        # this makes it easy for the program to check for overlaps 
        self.x = x
        self.y = y
        # this is to make the checking of directions easier as its always changing
        self.direction = direction
        # This is a list for the rover to switch direciton to alternate through left and right 
        self.direction_list = ("N","E","S","W")
        
        self.rover_coordinates = [self.x, self.y]

    def ask_user(self):
        # ask the user what way to face
        self.direction = input("what direction do you want the rover to face : ").strip().upper()

    def move(self):
        # move 1 grid in the way the rover is faceing
        if self.direction == "N":
            self.y += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x -= 1
        # keep the cords list up to date so it doesnt go out of sync
        self.rover_coordinates = [self.x, self.y]

    def turn_left(self):
        # this is the logic behind how the rover runs through the list of directions
        # it goes in a curcular rotation
        index = self.direction_list.index(self.direction)  # .index searches for a value and returns a position were the first value appears
        self.direction = self.direction_list[(index - 1) % 4]  # the "%4" keeps the index within the range of 0-3

    # this has the same logic as tuen left just instead of index -1 its index + 1
    def turn_right(self):
        index = self.direction_list.index(self.direction)
        self.direction = self.direction_list[(index + 1) % 4]  # here

    def check_move(self, max_x, max_y):
        # this checks if the next move would go off the platue so the rover doesnt fall off
        if self.direction == "N" and self.y + 1 <= max_y:
            return True
        elif self.direction == "S" and self.y - 1 >= 0:
            return True
        elif self.direction == "E" and self.x + 1 <= max_x:
            return True
        elif self.direction == "W" and self.x - 1 >= 0:
            return True
        return False


# this runs the whole thing, reading inputs and moving the rover around
def main():
    while True:
    # get the platue size2 i tries to split this up into parts that make sence
        try: #i thought putting these if try and except blcks as i learned it in school and it prevents the program from breaking
        #This gets the two platoe sizes
            platue_size = input("Enter the upper coordinates of the plateau : ").strip()
            max_x, max_y = map(int, platue_size.split())
        #break #if it works without error it will break out loop
            break
        except ValueError:
           print("please enter two numbers for example '3,3' ")
        #simply if user inputs wrong things, the loop will go again returning an error


    # get the starting cords and direction for the rover
    while True:
        try:
            print("x and y are the rovers position on the platoe \n D is the starting direction the rover is facing")
            start_line = input("Enter the rovers position like 'x y D' : ").strip()

        #split the string into 3 parts so its easier to be reformated
            start_rover_position = start_line.split()# this will be sth like 1, 2, N
            if start_rover_position != 3:
                raise ValueError('you need 3 values')

        #grab each bit by name so its not confusing
            x_text = start_rover_position[0]#the x cordinate
            y_text = start_rover_position[1]# the y cordinat
            dir_text = start_rover_position[2]#the way the rover is faceing
        #turn x and y into numbers and make sure direction is a capitle letter
            start_x = int(x_text)
            start_y = int(y_text)
            start_dir = dir_text.upper()

            #check if the direction is correct
            if start_dir not in ("N", "E", "S", "W"):
                raise ValueError('the direction is invalid')
            break # if all of the inputs are correct we can break out of the loop
        except ValueError:
            print('please select correct values')



    # make the rover (using my class as a base)
    rover = Rover(start_x, start_y, start_dir, [start_x, start_y])

    # get the instructions to make the rover walk about
    commands_line = input("Enter the series of instructions (L/R/M) : ").strip()

    # turn the string of commands into a list so we can go one by one
    commands_list = list(commands_line.upper())

    # run the instructions one at a time, rover finishes before next one starts
    for c in commands_list:
        if c == "L":
            rover.turn_left()
        elif c == "R":
            rover.turn_right()
        elif c == "M":
            # only move if the move is safe on the platue
            if rover.check_move(max_x, max_y):
                rover.move()
            else:
                # if it cant move just ignore it (or we could print somthing here)
                pass
    # output the final cords and heading
    print(rover.x, rover.y, rover.direction)


if __name__ == "__main__":
    # this is mucode so fat
    main()

