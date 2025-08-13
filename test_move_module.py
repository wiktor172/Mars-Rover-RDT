x = 0
y = 0
rover_coordinates = [x, y]
while True:

    user_imput = input('hy what direction are you facing. : ')

    def move(user_imput):
        if user_imput== "N":
            y += 1
        if user_imput == "S":
            y -= 1
        if user_imput == "E":
            x += 1
        if user_imput  == "W":
            x -= 1


print(rover_coordinates)


