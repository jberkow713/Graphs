from room import Room
#from player import Player
from world import World

import random
from ast import literal_eval


class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
    
    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")

class Queue:

    def __init__(self):
        self.storage = []
        self.size = 0

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) > 0:
            self.size -= 1
            return self.storage.pop(0)
        else:
            return None

    def length(self):
        return self.size 

class Stack:

    def __init__(self):
        self.storage = []
        self.size = 0

    def push(self, value):
        self.size += 1
        self.storage.append(value)

    def pop(self):
        if len(self.storage) > 0:
            self.size -= 1
            return self.storage.pop()

        else:
            return None

    def length(self):
        return self.size 




# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
#traversal_path = []



# Fill this out with directions to walk
# traversal_path = ['n', 'n']
'''
traversal_path = ['n', 's', "e", "e", "w", "s", "e", "s", 
"n", "w", "s", "s", "e", "s", "s", 
"n", "n", "e", "s", "s", "s", "s", "s", "e", 'w', 'n',
'n', 'n', 'e', 's', 'e', 'w',
's', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'n', 'n', 'w', 'n', 'e', 'n', 'e', 's', 's', 
'n', 'n', 'w', 's', 'w', 'n', 'w', 'w', 's', 's', 's', 's', 'n', 'e', 's', 's', 'w', 's', 's',
'n', 'n', 'e', 's', 'e', 'e', 'e', 'n', 'e', 'e', 'e', 'w', 's', 's', 'e', 'w', 's', 's',
'n', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 'w', 'w', 's', 'e', 'e', 's', 's', 
'n', 'n','w', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'n', 'w', 's', 's', 's', 's', 'n',
'n', 'w', 's', 'n', 'e', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'e', 'n', 'n', 'w', 's', 'n',
'n', 'n', 'n', 'n', 'w', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'n', 'n', 'n',
'n', 'n', 'w', 'n', 'n', 'n', 'n', 'n', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 's', 'n', 
'e', 'e', 's', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 'n', 's', 'e', 's', 'w', 's', 'n', 'e',
's', 'n', 'e', 's', 's', 's', 'n', 'n', 'n', 'w', 'n', 'e', 'e', 'n', 'n', 'n', 'n', 'n', 'e', 
'n', 'n', 'n', 'e', 'e', 's', 's', 's', 'n', 'n', 'e', 's', 's', 'e', 'w', 'n', 'e', 'e', 'e',
'e', 'e', 'w', 'w', 'w', 's', 's', 's', 's', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n',
'e', 'e', 'w', 'n', 's', 'w', 'n', 'n', 'e', 'e', 'e', 'w', 's', 'n', 'w', 'w', 'n', 'w', 'w', 
'n', 'w', 'n', 'e', 'e', 's', 'n', 'e', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'n', 's',

'w', 'w', 'w', 'n', 'w', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'w', 'w',
'n', 'e', 'n', 'e', 's', 'n', 'e', 's', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 'e', 'e', 'w',
'n', 'e', 'w', 's', 'w', 'w', 'w', 'n', 'e', 'e', 'n', 'e', 'w', 's', 'w', 'n', 'n', 'e', 'e', 'e',

's', 'n', 'w', 'w', 'w', 's', 's', 'w', 's', 's', 'w', 's', 'w', 's', 'w', 'w', 'n', 'n', 'n',
'n', 'n', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 's', 's', 'e', 'n', 'e', 'n', 'n', 'n', 'n', 
's', 's', 's', 'e', 'n', 'n', 'n', 's', 'e', 'n', 'n', 'e', 'e', 'e', 'e', 'w', 'n', 's', 'w', 

'n', 's', 'w', 'n', 's', 'w', 's', 's', 'w', 's', 's', 'w', 's', 'w', 's', 'w', 's', 'w', 's', 

'w', 's', 'w', 'e', 'n', 'w' , 'w', 's', 'w', 's', 's', 'n', 'n', 'e', 'n', 'e', 'n', 'w',
'w', 's', 'n', 'w', 's', 's', 's', 'w', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'w', 's', 'w', 'n',
 
's', 'e', 'n', 'e', 'e', 'e', 's', 'w', 'w', 'e', 's', 'w', 'e', 'n', 'e', 's', 's', 's', 's', 'w', 
's', 's', 's', 'n', 'n', 'w', 's', 's', 'w', 'e', 'n', 'w', 'e', 'n', 'e', 'n', 'e', 's', 's',
's', 's', 'w', 'e', 'n', 'e', 's', 'n', 'e', 's', 's', 'e', 'w', 's', 'w', 'e', 'n', 'n', 'n', 

'w', 'w', 'n', 'n', 'n', 'n', 'n', 'w', 's', 'w', 's', 'w', 's', 'n', 'e', 'n', 'w', 'w', 'w', 
'e', 's', 'w', 'w', 'e', 'e', 's', 's', 's', 's', 's', 'e', 'w', 'n', 'e', 'w', 'n', 'n', 'n', 
'w', 'w', 'w', 'w', 'e', 'e', 'e', 's', 's', 's', 's', 'n', 'w', 'w', 'e', 'e', 'n', 'w', 'e',

'n', 'w', 'e', 'n', 'e', 'n', 'n', 'e', 'e', 'e', 'n', 'w', 'w', 'n', 's', 'w', 'w', 'w', 's', 
'w', 's', 'n', 'e', 'n', 'e', 'e', 'n', 'w', 'w', 'n', 'w', 'e', 's', 'e', 'n', 'n', 'w', 'n',

'w', 'e', 'e', 'n', 'w',  'w', 'e', 'n', 's', 'e', 'n', 's', 'e', 'e', 'e', 'n', 'w', 'w', 
'e', 'e', 'e', 's', 'n', 'n', 'n', 'w', 'w', 'e', 'n', 'w', 'e', 's', 'e', 's', 'w', 'w', 'w', 'w',
'e', 'n', 'n', 's', 'w', 'w', 'w', 'e', 's', 'n', 'e', 'n', 'n', 's', 'w', 'w', 'w', 'e', 'e', 'e',

's', 'e', 's', 'e', 'e', 'e', 'e', 'n', 's', 'e', 'n', 's', 'e', 'n', 's', 'e', 'e', 'e', 'w',
'n', 'w', 'e', 'n', 'n', 's', 'e', 's', 'n', 'n', 'n', 'w', 'n', 'n', 'w', 'n', 'w', 'e', 'e', 'w',
's', 'e', 's', 's', 'e', 'n', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'n', 's', 'e', 'e', 'w', 'n', 'e',

'e', 'w', 'n', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'n', 's', 'w', 's', 'w', 'n', 'n', 'n', 'n', 's',
's', 'e', 'n', 'n', 's', 'e', 'n', 'n', 's', 'e', 'e', 'w', 's', 'n', 'w', 's', 'w', 's', 'w', 's',

'w', 'n', 'n', 'n', 'n', 'e', 'e', 'w', 'w', 's', 'w', 'n', 'w', 'w', 'e', 'e', 's', 'w', 's', 
's', 's', 's', 'e', 'w', 'n', 'e', 'n', 'n', 's', 's', 'w', 'w', 'n', 'n', 's', 'w', 'n', 's',
'e', 's', 'w', 'w', 'n', 'n', 'n', 'n', 's', 's', 's', 'w', 'n', 'n', 'w', 'e', 's', 's', 'e', 's',

'w', 's', 'w', 'e', 'n', 'w', 'n', 's', 'w', 'n', 's', 'e', 'e', 'e', 'e', 'e', 'e', 's',
's', 's', 's', 's', 's', 'w', 'w', 'n', 'w', 'n', 's', 'e', 'n', 'n', 'w', 'n', 's', 'w', 'n',
'w', 'e', 's', 'e', 'e', 's', 's', 's', 'w', 'w', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'w', 

'n', 's', 'w', 'n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 'w', 'w', 'e', 'e', 'n', 
'n', 'n', 'n', 'n', 'n', 's', 's', 'w', 'e', 's', 's', 's', 'w', 'n', 'n', 's', 's', 'w', 'n', 'n',
'n', 's', 's', 'w', 'e', 's', 'w', 'w', 'w', 'e', 's', 'w'



]

'''
'''
, 's', 's', 's', 's', 's', 'w', 'w', 'n', 'w', 'n', 's', 'e', 'n', 'n', 'w', 'n', 's', 'w', 'n',
'w', 'e', 's', 'e', 'e', 's', 's', 's', 'w', 'w', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'w', 


'n', 's', "e", "e", "w", "s", "e", "s", 

"n", "w", "s", "s", "e", "s", "s", 

"n", "n", "e", "s", "s", "s", "s", "s", "e", 'w', 'n',
good
'n', 'n', 'e', 's', 'e,', 'w',
g
's', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'n', 'n', 'w', 'n', 'e', 'n', 'e', 's', 's', 
g
'n', 'n', 'w', 's', 'w', 'n', 'w', 'w', 's', 's', 's', 's', 'n', 'e', 's', 's', 'w', 's', 's',
g
'n', 'n', 'e', 's', 'e', 'e', 'e', 'n', 'e', 'e', 'e', 'w', 's', 's', 'e', 'w', 's', 's',
g
'n', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 'w', 'w', 's', 'e', 'e', 's', 's', 

'n', 'n','w', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'n', 'w', 's', 's', 's', 's', 'n',

'n', 'w', 's', 'n', 'e', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'e', 'n', 'n', 'w', 's', 'n',
'n', 'n', 'n', 'n', 'w', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'n', 'n', 'n',
'n', 'n', 'w', 'n', 'n', 'n', 'n', 'n', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 's', 'n', 
'e', 'e', 's', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 'n', 's', 'e', 's', 'w', 's', 'n', 'e',

's', 'n', 'e', 's', 's', 's', 'n', 'n', 'n', 'w', 'n', 'e', 'e', 'n', 'n', 'n', 'n', 'n' , 'e', 
'n', 'n', 'n', 'e', 'e', 's', 's', 's', 'n', 'n', 'e', 's', 's', 'e', 'w', 'n', 'e', 'e', 'e',

'e', 'e', 'w', 'w', 'w', 's', 's', 's', 's', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n',
'e', 'e', 'w', 'n', 's', 'w', 'n', 'n', 'e', 'e', 'e', 'w', 's', 'n', 'w', 'w', 'n', 'w', 'w', 

'n', 'w', 'n', 'e', 'e', 's', 'n', 'e', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'n', 's',
'w', 'w', 'w', 'n', 'w', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'w', 'w',

'n', 'e', 'n', 'e', 's', 'n', 'e', 's', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 'e', 'e', 'w',
'n', 'e', 'w', 's', 'w', 'w', 'w', 'n', 'e', 'e', 'n', 'e', 'w', 's', 'w', 'n', 'n', 'e', 'e', 'e',

's', 'n', 'w', 'w', 'w', 's', 's', 'w', 's', 's', 'w', 's', 'w', 's', 'w', 'w', 'n', 'n', 'n',
'n', 'n', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 's', 's', 'e', 'n', 'e', 'n', 'n', 'n', 'n', 
's', 's', 's', 'e', 'n', 'n', 'n', 's', 'e', 'n', 'n', 'e', 'e', 'e', 'e', 'w', 'n', 's', 'w', 
'n', 's', 'w', 'n', 's', 'w', 's', 's', 'w', 's', 's', 'w', 's', 'w', 's', 'w', 's', 'w', 's', 
'w', 's', 'w', 's', 'e', 'n', 'w' , 'w', 's', 'w', 's', 's', 'n', 'n', 'e', 'n', 'e', 'n', 'w', 
'w', 's', 'n', 'w', 's', 's', 's', 'w', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'w', 's', 'w', 'n',
's', 'e', 'n', 'e', 'e', 'e', 's', 'w', 'w', 'e', 's', 'w', 'e', 'n', 'e', 's', 's', 's', 's', 'w', 
's', 's', 's', 'n', 'n', 'w', 's', 'w', ' e', 's', 'w', 'e', 'n', 'n', 'e', 'n', 'e', 's', 's', 
's', 's', 'w', 'e', 'n', 'e', 's', 'n', 'e', 's', 's', 'e', 'w', 's', 'w', 'e', 'n', 'n', 'n', 
'w', 'w', 'n', 'n', 'n', 'n', 'n', 'w', 's', 'w', 's', 'w', 's', 'n', 'e', 'n', 'w', 'w', 'w', 
'e', 's', 'w', 'w', 'e', 'e', 's', 's', 's', 's', 's', 'e', 'w', 'n', 'e', 'w', 'n', 'n', 'n', 
'w', 'w', 'w', 'w', 'e', 'e', 'e', 's', 's', 's', 's', 'n', 'w', 'w', 'e', 'e', 'n', 'w', 'e',
'n', 'w', 'e', 'n', 'e', 'n', 'n', 'e', 'e', 'e', 'n', 'w', 'w', 'n', 's', 'w', 'w', 'w', 's', 
'w', 's', 'n', 'e', 'n', 'e', 'e', 'n', 'w', 'w', 'n', 'w', 'e', 's', 'e', 'n', 'n', 'w', 'n',
'w', 'e', 'e', 'n', 'w', 'w', 'e', 'n', 's', 'e', 'n', 's', 'e', 'e', 'e', 'n', ' w', 'w', 
'e', 'e', 'e', 's', 'n', 'n', 'n', 'w', 'w', 'e', 'n', 'w', 'e', 's', 'e', 's', 'w', 'w', 'w', 'w',
'e', 'n', 'n', 's', 'w', 'w', 'w', 'e', 's', 'n', 'e', 'n', 'n', 's', 'w', 'w', 'w', 'e', 'e', 'e',
's', 'e', 's', 'e', 'e', 'e', 'e', 'n', 's', 'e', 'n', 's', 'e', 'n', 's', 'e', 'e', 'e', 'w']


traversal_path = ['n', 's', "e", "e", "w", "s", "e", "s", 
"n", "w", "s", "s", "e", "s", "s", 
"n", "n", "e", "s", "s", "s", "s", "s", "e", 'w', 'n',
'n', 'n', 'e', 's', 'e', 'w',
's', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'n', 'n', 'w', 'n', 'e', 'n', 'e', 's', 's', 
'n', 'n', 'w', 's', 'w', 'n', 'w', 'w', 's', 's', 's', 's', 'n', 'e', 's', 's', 'w', 's', 's',

'n', 'n', 'e', 's', 'e', 'e', 'e', 'n', 'e', 'e', 'e', 'w', 's', 's', 'e', 'w', 's', 's',
'n', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 'w', 'w', 's', 'e', 'e', 's', 's', 

'n', 'n','w', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'n', 'w', 's', 's', 's', 's', 'n',
'n', 'w', 's', 'n', 'e', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'e', 'n', 'n', 'w', 's', 'n',
'n', 'n', 'n', 'n',/5 'w', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'n', 'n', 'n',
'n', 'n', 'w', 'n', 'n', 'n', 'n', 'n', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 's', 'n', 

'e', 'e', 's', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 'n', 's', 'e', 's', 'w', 's', 'n', 'e',
's', 'n', 'e', 's', 's', 's', 'n', 'n', 'n', 'w', 'n', 'e', 'e', 'n', 'n', 'n', 'n', 'n' First quadrant, 'e', 
'n', 'n', 'n', 'e', 'e', 's', 's', 's', 'n', 'n', 'e', 's', 's', 'e', 'w', 'n', 'e', 'e', 'e',

'e', 'e', 'w', 'w', 'w', 's', 's', 's', 's', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n',
'e', 'e', 'w', 'n', 's', 'w', 'n', 'n', 'e', 'e', 'e', 'w', 's', 'n', 'w', 'w', 'n', 'w', 'w', 
'n', 'w', 'n', 'e', 'e', 's', 'n', 'e', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'n', 's',

'w', 'w', 'w', 'n', 'w', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'w', 'w',
'n', 'e', 'n', 'e', 's', 'n', 'e', 's', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 'e', 'e', 'w',
'n', 'e', 'w', 's', 'w', 'w', 'w', 'n', 'e', 'e', 'n', 'e', 'w', 's', 'w', 'n', 'n', 'e', 'e', 'e',
/
's', 'n', 'w', 'w', 'w', 's', 's', 'w', 's', 's', 'w', 's', 'w', 's', 'w'18 right side, 'w', 'n', 'n', 'n',
'n', 'n', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 's', 's', 'e', 'n', 'e', 'n', 'n', 'n', 'n', 
's', 's', 's', 'e', 'n', 'n', 'n', 's', 'e', 'n', 'n', 'e', 'e', 'e', 'e', 'w', 'n', 's', 'w', 

'n', 's', 'w', 'n', 's', 'w', 's', 's', 'w', 's', 's', 'w', 's', 'w', 's', 'w', 's', mid upper right 'w', 's', 
'w', 's', 'w', 's', 'e', 'n', 'w' , 'w', 's', 'w', 's', 's', 'n', 'n', 'e', 'n', 'e', 'n', 'w', 
'w', 's', 'n', 'w', 's', 's', 's', 'w', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'w', 's', 'w', 'n',
/
's', 'e', 'n', 'e', 'e', 'e', 's', 'w', 'w', 'e', 's', 'w', 'e', 'n', 'e', 's', 's', 's', 's', 'w', 
's', 's', 's', 'n', 'n', 'w', 's', 'w', ' e', 's', 'w', 'e', 'n', 'n', 'e', 'n', 'e', 's', 's', 
's', 's', 'w', 'e', 'n', 'e', 's', 'n', 'e', 's', 's', 'e', 'w', 's', 'w', 'e', 'n', 'n', 'n', 
/
'w', 'w', 'n', 'n', 'n', 'n', 'n', 'w', 's', 'w', 's', 'w', 's', 'n', 'e', 'n', 'w', 'w', 'w', 
'e', 's', 'w', 'w', 'e', 'e', 's', 's', 's', 's', 's', 'e', 'w', 'n', 'e', 'w', 'n', 'n', 'n', 
'w', 'w', 'w', 'w', 'e', 'e', 'e', 's', 's', 's', 's', 'n', 'w', 'w', 'e', 'e', 'n', 'w', 'e',
/
'n', 'w', 'e', 'n', 'e', 'n', 'n', 'e', 'e', 'e', 'n', 'w', 'w', 'n', 's', 'w', 'w', 'w', 's', 
'w', 's', 'n', 'e', 'n', 'e', 'e', 'n', 'w', 'w', 'n', 'w', 'e', 's', 'e', 'n', 'n', 'w', 'n',
/
'w', 'e', 'e', 'n', 'w', 'w', 'e', 'n', 's', 'e', 'n', 's', 'e', 'e', 'e', 'n', ' w', 'w', 
'e', 'e', 'e', 's', 'n', 'n',81 bottom done 'n', 'w', 'w', 'e', 'n', 'w', 'e', 's', 'e', 's', 'w', 'w', 'w', 'w',
'e', 'n', 'n', 's', 'w', 'w', 'w', 'e', 's', 'n', 'e', 'n', 'n', 's', 'w', 'w', 'w', 'e', 'e', 'e',
/
's', 'e', 's', 'e', 'e', 'e', 'e', 'n', 's', 'e', 'n', 's', 'e', 'n', 's', 'e', 'e', 'e', 'w',13, complete bottom
done
'n', 'w', 'e', 'n', 'n', 's', 'e', 's', 'n', 'n', 'n', 'w', 'n', 'n', 'w', 'n', 'w', 'e', 'e', 'w',
's', 'e', 's', 's', 'e', 'n', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'n', 's', 'e', 'e', 'w', 'n', 'e',
/
'e', 'w', 'n', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'n', 's', 'w', 's', 'w', 'n', 'n', 'n', 'n', 's',
's', 'e', 'n', 'n', 's', 'e', 'n', 'n', 's', 'e', 'e', 'w', 's', 'n', 'w', 's', 'w', 's', 'w', 's',
/
'w', 'n', 'n', 'n', 'n', 'e', 'e', 'w', 'w', 's', 'w', 'n', 'w', 'w', 'e', 'e', 's', 'w', 's', 
's', 's', 's', 'e', 'w', 'n', 'e', 'n', 'n', 's', 's', 'w', 'w', 'n', 'n', 's', 'w', 'n', 's',
'e', 's', 'w', 'w', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'n', 'n', 'w', 'e', 's', 's', 'e', 's',
/
'w', 'w', 's', 'w', 'e', 'n', 'w', 'n', 's', 'w', 'n', 's', 'e', 'e', 'e', 'e', 'e', 'e', 's'
, 's', 's', 's', 's', 's', 'w', 'w', 'n', 'w', 'n', 's', 'e', 'n', 'n', 'w', 'n', 's', 'w', 'n',
'w', 'e', 's', 'e', 'e', 's', 's', 's', 'w', 'w', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'w', 
/
'n', 's', 'w', 'n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 'w', 'w', 'e', 'e', 'n', 
'n', 'n', 'n', 'n', 'n', 's', 's', 'w', 'e', 's', 's', 's', 'w', 'n', 'n', 's', 's', 'w', 'n', 'n',
'n', 's', 's', 'w', 'e', 's', 'w', 'w', 'w', 'e', 's', 'w']

'''
#initial list for reversePath and initial visited dictionary
traversal_path = []
reversedlist = [] # keeps track of way back to last room
visited = {} # path of rooms and their potential exits

def reverse(direction):

    if direction is 'n':
        return 's'

    if direction is 's':
        return 'n'

    if direction is 'e':
        return 'w'

    if direction is 'w':
        return 'e'

# reverse_direction will return the opposite direction to what the input was
#player is starting at room 0, as instantiated from above
#setting initial value in dictionary at starting room to be equal to that room's exits

visited[player.current_room.id] = player.current_room.get_exits()

# initial room set in dictionary, initial dictionary length = 1, so set while loop to check last 499 rooms

while len(visited) < 499:

    #setting term inside while loop to append current room's exits to current_room value in visited dict:
    #checking all directions you can move
    if player.current_room.id not in visited:
        visited[player.current_room.id] = player.current_room.get_exits()
        visited[player.current_room.id].remove(reversedlist[-1])

    #this represents when you enter a room with only one exit and you backtrack
    # the last object in the reverse list will always be the direction you have just gone, so they will cancel out,
    # and the length of the dictionary with that room will be 0
    # so when you enter a room with one exit, and then remove that opposite direction, you will 
    # ALWAYS hit this while loop, and in doing so, you will always reverse back to where you were

    # you are using a stack to reverse direction, and you are using a queue, to test all possible branches
    # from each element

    # the visited dictionaries themselves will contain empty objects , when you have tested all possible exits
    # from each room, and the length of the visited dictionary will increment until you reach the 499
    while len(visited[player.current_room.id]) == 0:
        #reversed = last value in the reverse list
        reversed = reversedlist.pop()
        # this is adding the reverse direction to your traversal list
        traversal_path.append(reversed)
        #travel in the reverse direction to get back to where you came
        player.travel(reversed)
    
    # while loop causes you to go in reversed direction 

    # move in direction of 1st element in dictionary, or 1st direction, in case of get exits its 
    #always N, S, W, E in that order
    move = visited[player.current_room.id].pop(0)
    #add the move's direction to the traversal_path first before moving
    traversal_path.append(move)
    #add opposite direction to reverse list before moving
    reversedlist.append(reverse(move))
    #move in direction
    player.travel(move)


#this function is set up so that only reverses directions when the exits from the room ==1, it offsets that,
# goes back, and continues to go back the way it came, until it reaches the initial branching point, until search full map
# the reverselist is storing a way to get back to an initial room with multiple exits, as the exits are exhausted from each room,
# the reverselist is keeping track of the way back to the initial point


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
