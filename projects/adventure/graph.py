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

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

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



class Graph():
    
    def __init__(self):
        
        self.rooms = []
        self.adjacentRooms = []


    
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

#p = Player(0)
#print(p.BFTraversal())
'''
