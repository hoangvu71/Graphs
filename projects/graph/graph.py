"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a visited set
        visited = set()
        # add starting vertex to queue
        queue = Queue()
        queue.enqueue(starting_vertex)
        
        # as long as the size of queue is not 0
        while queue.size() > 0:

            # remove that starting vertex
            node = queue.dequeue()
            # check if that vertex has been visited
            # if it hasn't been visited
            if node not in visited:
                # add to the visited list
                print(node)
                visited.add(node)

                for neighbor in self.get_neighbors(node):
                    # add the neighbor to the q
                    queue.enqueue(neighbor)

            # if it has been visited
            # ignore it

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        # add starting vertex to stack
        stack.push(starting_vertex)
        # while stack not 0 
        while stack.size() > 0:
        # remove vertex from stack to work on it
            node = stack.pop()
        # is that vertex in the visited set
        # if not
            if node not in visited:

        # add the vertex to visited
                visited.add(node)
                print(node)
        # get all the surround neighbor and add them to the stack
                for neighbor in self.get_neighbors(node):
                    stack.push(neighbor)


    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # this can actually be done with an array
        # which we will append the value to the head of the array
        # then take it out it time to work on in the next iteration
        node_list = []
        # check whehter the starting_vertex is a list or just a node
        if type(starting_vertex) == type(1):
            node_list.append(starting_vertex)
        else:
            node_list = starting_vertex
        # if it is a node, then turn it to a list
        # otherwise, ignore
        if len(node_list) > 0:
            # then take off one node from node list
            node = node_list.pop(-1)
            # check to see if this node is in the visited list, which we will
            # pass it as an argument recursively to keep track with each iteration
            if node not in visited:
                visited.add(node)
                print(node)

                # add all the surrounding neighbors of this node
                for neighbor in self.get_neighbors(node):
                    node_list.append(neighbor)
        
            return self.dft_recursive(node_list, visited)

        # the array will represent a stack
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # same as with bft, just need to add an array to keep track of node that equal to destination_vertex
        ############################
        # make a visited set
        visited = set()
        # array to keep track of shortest path
        # add starting vertex to queue
        queue = Queue()
        queue.enqueue([starting_vertex])
        
        # as long as the size of queue is not 0
        while queue.size() > 0:

            # remove that starting path
            path = queue.dequeue()

            node = path[-1]

            # check if that vertex has been visited
            # if it hasn't been visited
            if node == destination_vertex:
                return path

            elif node not in visited:
                # add to the visited list
                
                visited.add(node)
                
                for neighbor in self.get_neighbors(node):
                    # add the neighbor to the queue
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)
                    
 

            # if it has been visited
            # ignore it
        ############################

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex, path = [], visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # do the usual dft recursive while adding the node to path until we reach the destination_vertex

        #####################
        # this can actually be done with an array
        # which we will append the value to the head of the array
        # then take it out it time to work on in the next iteration
        node_list = []
        # check whehter the starting_vertex is a list or just a node
        if type(starting_vertex) == type(1):
            node_list.append(starting_vertex)
        else:
            node_list = starting_vertex
        # if it is a node, then turn it to a list
        # otherwise, ignore
        if len(node_list) > 0:
            # then take off one node from node list
            node = node_list.pop(-1)
            # check to see if this node is in the visited list, which we will
            # pass it as an argument recursively to keep track with each iteration
            if node == destination_vertex:
                visited.add(node)
                path.append(node)
                return path
            if node not in visited:
                visited.add(node)
                path.append(node)
                print(node)

                # add all the surrounding neighbors of this node
                for neighbor in self.get_neighbors(node):
                    node_list.append(neighbor)
        
            return self.dfs_recursive(node_list, destination_vertex, path, visited)

        # the array will represent a stack
        #####################

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
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
