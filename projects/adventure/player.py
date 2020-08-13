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
    #want to traverse, 
    # current room is like first room into the queue
    # get exits, is like the get neighbors function,
    #        
    #traversalPath = []

    #    graph = {}
    
    def BFTraversal(self, starting_room):
        graph = {}    
        
        q = Queue()
        q.enqueue([starting_room])

        visited = set()

        while q.size() > 0:
            
            path = q.dequeue()
            
            x = path[-1]

            if "?" in list(graph[x].values()):

                new_path = list(path)
                new_path.append(x)
                return new_path

            if x not in visited:

                visited.add(x)
                for k, v in graph[x].items():
                    new_path = list(path)
                    new_path.append(x)
                    q.enqueue(new_path)

        return None