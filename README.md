# Mars Rover RDT
this is my go at the mars rover challenge set by the RDT work experience
i did all of the prototypes in OOP in python without any extra libaries just messing around with python, sources will be linked in this repo.

### how i broke this task into smaller parts:
- there is a platoe on mars with more then multiple mars rovers on mars
- the rovers can face North, South, East, West and they can move forward depending on the direction they are facing
    - this is determined through commands like N,S,E,W
    - M is the command to move forward
- The program checks if the rover falls of the platoe

## How i built it
firstly i started with breaking the wordy problem down into something i could understand in my head, so i used a notebook and pretty much abstracted it down to the bare bones and made a Minimum viable product criteria that i could follow.
Then i started with building a single rover. This was the stage were i was trying to figure out different approaches to solving the problem. this can be seen through the prototypes in the  

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

