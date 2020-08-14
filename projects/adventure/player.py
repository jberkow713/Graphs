class Room:
    def __init__(self, name, description, id=0, x=None, y=None):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __str__(self):
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.get_exits_string()}\n"
    def print_room_description(self, player):
        print(str(self))
    def get_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits
    def get_exits_string(self):
        return f"Exits: [{', '.join(self.get_exits())}]"
    def connect_rooms(self, direction, connecting_room):
        if direction == "n":
            self.n_to = connecting_room
            connecting_room.s_to = self
        elif direction == "s":
            self.s_to = connecting_room
            connecting_room.n_to = self
        elif direction == "e":
            self.e_to = connecting_room
            connecting_room.w_to = self
        elif direction == "w":
            self.w_to = connecting_room
            connecting_room.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None
    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
    def get_coords(self):
        return [self.x, self.y]
  
  



class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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
    # So you have to create a breadth first search from the starting room, find all possible neighbors, put the 
    # neighbors in the queue, and from there just keep adding neighbors, and checking their neighbors

    # if you reach a room, and that room has only ONE exit, you need to implement a reverse method, that brings the 
    # player back to the last room, and continues the traverse
    
    # you need to keep track of all the rooms traversed, so if you hit a repeat, do not continue down that path

    # when you enter a new room, you need to log that room into a set, and you also need to log that room as a key in a
    # dictionary, with all possible exits as values.

    # so the first thing to solve this problem, is to traverse the entire list, and while the length of the set is 
    # < 500, you continue on, at the end, you return the set...

    # as you are scrolling through this maze, getting this traversal in all possible directions, you need to log
    # all possible exits for each room, into this dictionary object

    # so basically, when the room has not been explored, when the room is entered into the dictionary, 
    # it is entered as a dictionary object, and all of the connecting surrounding rooms 

    
    #You may find the commands 
    #`player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.



        # this is in the player class
        # with one variable, starting room, we want to make a breadth first search

    
'''

  
    def BFTraversal(self):

         
        p = Player(0)
       
        current_room = p.current_room
        
        q = Queue()
        q.enqueue(current_room)

        visited = set()
        d = {}
        
        while q.size() > 0:
            
            current = q.dequeue()
            
                        
            if current not in visited:
                #Add room number to visited set
                visited.add(current)
                

                #get possible exits from current room
                # can not access it from integer form of the room
                Exits = p.current_room.get_exits()
                
                # this represents possible exits from current room:
                for Exit in Exits:
                    #for each exit,
                    p.travel(Exit)
                    room = p.current_room    
                              
                    q.enqueue(room)


        return(visited)                

p = Player(0)
print(p.BFTraversal())
'''


