"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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

    def bft(self, starting_vertex):

        q = Queue()

        q.enqueue(starting_vertex)
       
        visited = set()

        while q.size() > 0:
            # this sets the current node to the one you pull out of the queue
            # in the queue, you pull it out first in, first out, so it 
            # initializes with the starting vertex, dequeues the starting vertex
            # checks to see if starting point is in visited: if not, it adds it,
            # finds the node or vertex's neighbors, puts them in the queue
            # at this point, only the neighbors are in the queue, because the 
            # initial point was taken out, so in the order the neighbors were entered
            # it pulls one neighbor node out, and repeats the while loop, 
            # it does this until the queue has size of 0, meaning all points have
            # been checked. Then it ends it's traversal of the graph
            current_node = q.dequeue()
            
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                
                #dictionary object associated with the current_node
                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    q.enqueue(neighbor)
        #return visited 

    def dft(self, starting_vertex):
        
        s = Stack()

        s.push(starting_vertex)

        visited = set()
        # size is the length of the [] that stack represents

        while s.size() > 0 :
            current_node = s.pop()

            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                #returns dictionary object associated with the 
                # specific node's id
                neighbors = self.get_neighbors(current_node)

                #scroll's through dictionary associated with 
                #current_node, add's each one of it's neighbors
                # essentially it means last element in the dictionary
                # will be the next one popped out and the next current_node

                for neighbor in neighbors:
                    s.push(neighbor)
                
                # the essence of this while loop, is that elements are being
                #taken out one by one, and their neighbors are being added
                # so when there are no more neighbors, the list is getting 
                # shortened, until there is nothing left in the list, 
                # and you have visited, which is a list of all nodes in the 
                # graph

        #return visited         




    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # recursion will basically act like the stack does,
        # so that's why it can be used in this case for depth first
        #traversal

        # it's going to pull out the neighbors and put them in the list, 
        # find the neighbors of the last neighbor in the list, add them to the list
        # head all the way down the line until it finds no neighbors, 
        # go to the last element and repeat, head down that line,
        # until all paths lead to none
        if starting_vertex not in visited:
            print(starting_vertex)
        visited.add(starting_vertex)
        
                
        neighbors = self.get_neighbors(starting_vertex)

        for neighbor in neighbors:

            if neighbor not in visited:
                
                self.dft_recursive(neighbor, visited)    
                
                #if result is not None:
                #    return result






    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create empty queue, enqueues a path
        # store in set
        # dequeue path
        # look at last element in list, if not visited,
        # check if its target, if so, return path, 
        # if not, mark as visited, add path to its neighbors 
        # to back of queueu, append neighbor to the path, repeat

        q = Queue()
        
        
        #set the path variable to a list, containing the starting_vertex
        # enqueueue the path

        visited = set()
        path = [starting_vertex]
        q.enqueue(path)

        while q.size() > 0:
            
            current_path = q.dequeue()
            # take out the full path, 
            # turn the current node into the last element in the list,
            # aka, a single element, representing either initial node, 
            # or neighbors of last node
            current_node = current_path[-1]
            
            # if the current node is the destination, 
            # just return the entire list
            if current_node == destination_vertex:
                return current_path

            if current_node not in visited:
                visited.add(current_node)
                
                #otherwise, find neighbors of the last element in list

                neighbors = self.get_neighbors(current_node)
                 
                for neighbor in neighbors:
                    #bring the full path from before down here 
                    # appends the neighbor to the list
                    # puts the FULL list back in the queue
                    # works on the neighbors   
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
                    
                    q.enqueue(path_copy)

                  # we are only putting individual elements in visited
                  # but we are putting the entire path into the queue  


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()

        path = [starting_vertex]
        s.push(path)

        
        while s.size() > 0:

            current_path = s.pop()
            current_node = current_path[-1]

            #destinations = []
            
            if current_node == destination_vertex:
                return current_path
                #destinations.append(current_path)

            if current_node not in visited:
                visited.add(current_node)

                neighbors = self.get_neighbors(current_node)
                 
                for neighbor in neighbors:
                    #bring the full path from before down here 
                    # appends the neighbor to the list
                    # puts the FULL list back in the queue
                    # works on the neighbors   
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
                    
                    s.push(path_copy)

        #print(destinations)    

               

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):

        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        
        #path is an empty list to start

        visited.add(starting_vertex)
        #so the starting vertex, or neighbor, in case of recursion, can only be checked at the 
        # start of the function
        if starting_vertex == destination_vertex:
            return path
        # to add starting vertex so it doesnt have issue 
        if len(path) == 0:
            path.append(starting_vertex)

        # get neighbors of the last node, or in the recursive case, the last neighbor
        neighbors = self.get_neighbors(starting_vertex)

        #add neighbor to visited list
        for neighbor in neighbors:
            if neighbor not in visited:
                # if neighbor is not in visited, continue traversing downward, run function again

                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor],  visited)
                
                # in every case, except the one in which the starting vertex, or neighbor == destination
                # the result returned will be None:
                # so if the result is not None, you know you have reached the destination with the 
                # full path leading to the right destination
                if result is not None:
                    return result
           
              

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
