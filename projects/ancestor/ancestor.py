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



class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        # this will be a dictionary of dictionaries, 
        # where each node or vertex has a dictionary of connected nodes
        # associated with it


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # each vertex_id is an individual node, 
        # this creates a dictionary, associated with each node,
        # represented by a set of connected nodes: for example, 
        # if you add vertex_id 3, 
        # 3 : {}
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # connects a new point to the original point in the 
        # main dictionary, using v1 as the node, and v2 as the connected
        # vertex...so for example, self.graph.add_edge(5, 3)
        # will scroll into your vertices dictionary, find 5, and place a 
        # 3 inside the dictionary associated with 5 
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # so this is going to scroll into the vertices dictionary, 
        # and find the values associated with the specific vertex_id
        #  so if you say self.get_neighbors(3), it will look at point 3
        # and return the dictionary object associate with 3
        # which were added by add_edge to point 3 
        
        return self.vertices[vertex_id]


#adding vertices for child and parents from the ancestor's tuple
# adding edges on graph from the child to the parents in each tuple
graph = Graph()
def build_graph(ancestors):
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    return graph    


def earliest_ancestor(ancestors, starting_node):
    

    # find longest branch of each starting node, traverse it to the end, return the value
    # define get neighbors
    #depth first search
    
    #initiating with a graph by building all the connections
    graph = build_graph(ancestors)

    s = Stack()

    visited = set()
    s.push([starting_node])
    
    longest_list = []
    no_ancestor = -1
    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]
        
        # when new path comes off the stack, if it is longer than the last value,
        # the longest_list then becomes this value

        if (len(path) > len(longest_list)) or len(path) == len(longest_list) and current_node < longest_list[-1] : 
            longest_list = path
        # if at end of while loop, length of path is still 1, then the vertex had 
        # no ancestor, so return -1
        if len(path) == 1:
            longest_list[-1] = no_ancestor    

        #if path[-1] == longest_list[-1]:
        #    longest_list = no_ancestor
        #if len(longest_list) == 1:
        #    longest_list == no_ancestor



        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighbors(current_node)
                 
            for parent in parents:
                    #bring the full path from before down here 
                    # appends the neighbor to the list
                    # puts the FULL list back in the queue
                    # works on the neighbors   
                path_copy = path[:]
                path_copy.append(parent)
                
                    
                s.push(path_copy)

    return longest_list[-1]        

