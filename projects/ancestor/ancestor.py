
def earliest_ancestor(ancestors, starting_node):
    
    table = {}
    def initializing(ancestors):
        for eachNode in ancestors:
            # make vertex for each child
            table[eachNode[1]] = set()
        
        for eachNode in ancestors:
            # make key the child and values the parent
            table[eachNode[1]].add(eachNode[0])

    initializing(ancestors)
    
    def get_neighbor(vertex):
        if vertex in table:
            return table[vertex]
        else:
            return {"None"}

    def get(starting_node):

        # we can return paths, check up on length of each path, return the one with the most len(path)
        # else if len(path) the same across the board, return the path with the least id

        # so the moment their neighbor is none, we add the path to a list to keep track
        # this can be done by bfs or dfs, doesn't matter

        # i ll just use bfs
        paths = []
        # make queue
        queue = []
        # enqueue path
        queue.append([starting_node])
        # as long as path not empty
        while len(queue) > 0:
        # dequeue path
            path = queue.pop(0)
        # vertex is path last node
            node = path[-1]
        # we dont really need to check if it has been visited or not since this is a directed graph
        # there's only one way and it's not cyclic graph either

        # check its neighbor
            for neighbor in get_neighbor(node):
         # if neighbor is "None",
        # we will add that path to a list to keep track of all paths.
                if neighbor == "None" and node == starting_node:
                    paths.append([-1])
                elif neighbor != "None":
        # add neighbor to new path 
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                
        # enqueue the new path
       
        # so what happens if the neighbor is None, we can't exactly enqueue a None object
        # we can just say, if neigbor is not None, then we enqueue, if it is then we add it to the list
                elif neighbor == "None":
                    new_path = list(path)
                    paths.append(new_path)

        # once we are done with the while loop, we deal with the list that we keep track
        # make it sort_list(paths)
        # sort this list by the last digit and use max(paths, key = len) because this will return the biggest length path
        # if there two biggest length path, it will return the first one, therefore that is why we sort it by the last digit
    
        def sort_list(paths):
            # sort path by the last digit
            # actually, we can do it like this
            # we can put the last digit of paths to the front
                # for each path
            for path in paths:
                # save last digit to variable
                last_digit = path[-1]
                # insert that last digit to path
                path.insert(0, last_digit)
            # run sort and it will sort it by the first digit
            paths.sort()
            # then run max len
            new_paths = max(paths, key=len)
            # then return that first digit
            return new_paths[0]

        return sort_list(paths)
    return get(starting_node)






test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 2))