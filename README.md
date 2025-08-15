# Mars Rover RDT
This is my go at the Mars Rover challenge set by the RDT work experience.
I did all of the prototypes in OOP in Python without any extra libraries—just messing around with Python. Sources will be linked in this repo.

### how i broke this task into smaller parts:
There is a plateau on Mars with more than one rover.
The rovers can face North, South, East, or West, and they move forward depending on the direction they are facing.
This is represented by directions like N, S, E, W.
M is the command to move forward.
The program checks if the rover falls off the plateau.

## How i built it
First, I started by breaking the wordy problem down into something I could understand in my head. I used a notebook, abstracted it down to the bare bones, and made minimum viable product criteria that I could follow.
Then I started by building a single rover. This was the stage where I was trying to figure out different approaches to solving the problem. This can be seen through the prototypes in the repo.

## How to run
1. Make sure you have Python 3 installed.
2. Download/clone this repo and open a terminal in the repo folder.
3. Run the script: multiple_rovers_main.py

## Testing
(2 rovers)
Rover 1 
input : 55 
input : 1 2 N
input : LMLMLMLMM
<img width="1024" height="421" alt="image" src="https://github.com/user-attachments/assets/2aa99e3e-6388-40f0-bf57-a089e36cf83a" />
expected output : 1 3 N
output : 1 3 N

Rover 2
input : 3 3 E
input : MMRMMRMRRM
<img width="981" height="634" alt="image" src="https://github.com/user-attachments/assets/d8945e70-eb87-4aa8-a680-096f68960442" />
expected output : 5 1 E
output : 5 1 E

