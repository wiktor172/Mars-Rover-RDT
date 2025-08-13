

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
        self.direction = input("what direction do you want the rover to face : ")

    def move(self):
        if self.direction == "N":
            self.y += 1
        if self.direction == "S":
            self.y -= 1
        if self.direction == "E":
            self.x += 1
        if self.direction == "W":
            self.x -= 1

    def turn_left(self):
        #this is the logic behind how the rover runs through the list of directions
        # it goes in a curcular rotation
        index = self.direction_list.index(self.direction) #.index searches for a value and returns a position were the first value appears
        self.direction = self.direction_list[(index - 1) % 4] # the "%4" keeps the index within the range of 0-3

    # this has the same logic as tuen left just instead of index -1 its index + 1
    def turn_right(self):
        index = self.direction_list.index(self.direction)
        self.direction = self.direction_list[(index + 1) % 4] # here


    
    def check_move(self, max_x, max_y):
        if self.direction == "N" and self.y + 1 <= max_y:
            return True
        elif self.direction == "S" and self.y - 1 >= 0:
            return True
        elif self.direction == "E" and self.x + 1 <= max_x:
            return True
        elif self.direction == "W" and self.x - 1 >= 0:
            return True
        return False



    def main():
        # get the platue size2
        platue_size = ("Enter the upper coordinates of the plateau : ")


if __name__ == "__main__":
    
