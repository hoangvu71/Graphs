from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# make a walk def
# def walking(player)
# this function would do depth first traversal to find all the room
# now, if we run this dft, it will travel in one direction ( a random but singular direction until it reaches the end ) 
# once it reaches the end, it would return back to the last split (route) and repeat
# so we want it to move from "the end" to "the split" by using a breath first traversal to find the shortest distance.
# once bft is done, we will need to return the path and also the steps it took to that path

# lets traverse the maze first by dft

# make walk function
def walk(player):
# make stack
    rooms_visited = {}
    stack = []
# push current room into the stack
    current_room = player.current_room
    track_old_room = current_room

    current_room_id = current_room.id
    stack.append(current_room)

# while stack is not 0
    while len(stack) > 0:
# we pop the stack = node
        old_room = current_room
        current_room = stack.pop(-1)
        current_room_id = current_room.id
# check if that node in a visited list (ex: {
#   0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
#   5: {'n': 0, 's': '?', 'e': '?'}
# } )   

        if current_room_id not in rooms_visited:
            rooms_visited[current_room_id] = {}
            
            # over here is where we can do a breath first search
            # the breath first search will return us the shortest distance to that node
            # ex "[1,5,7]" where 1 is first node and 7 is destination node

            # make def bfs(current_room)
            def bfs(current_room, destination_room):
                def get_exits(node):
                    return node.get_exits()

            # enqueue the path
                visited = {}
                queue = []
                queue.append([current_room])
            # while size > 0
                while len(queue) > 0:
            # dequeue the path
                    path = queue.pop(0)
            # node = path[-1]
                    room = path[-1]
            # check if it is in visited
                    if room.id not in visited:
                        visited[room.id] = True
            # if not, add it in
            # check its neighbor
                        for exit in get_exits(room):
            # new path = list(path)
                            the_next_room = room.get_room_in_direction(exit)
                            new_path = list(path)
            # add neighbor to path
                            new_path.append(the_next_room)
            # then enqueue the new path
                            queue.append(new_path)
                            if the_next_room.id == destination_room:
                                path_transcribe = []
                                for eachPath in new_path:
                                    path_transcribe.append(eachPath.id)
                                return path_transcribe

            # once we have shortest distance list we need to turn that list into list of steps
            # ex "['n', 's', 's']"
            # we can do this by checking our rooms_visited list
            # if that particular room has a 'n' and it leads to room 1, then we add that direction
            
            # we can take the list [4, 3, 0 , 7]
            # 4 is the track_old_room
            # and 7 is the current room
            # make function list_step_transcribe
            # check the exits of the current room
            # if one of the exits == the next index in the list [ 4, 3, 0, 7] then
            transcribe_room_id = bfs(track_old_room, current_room_id)
            # make function transcribe_steps_list (list, current_room):
            # for each id in the list
            # from the second index
            # check if current_room get exits has an exit with result = to that second index id
            # add that exit to a list
            # update the current room
            def transcribe_steps_list(transcribe_room_id_list, current_room):
                print("Current room", current_room.id)
                steps_list = []
                for index in range(len(transcribe_room_id_list)):
                    if index > 0:
                        current_room_exits = current_room.get_exits()
                        for exit in current_room_exits:
                            next_room = current_room.get_room_in_direction(exit)
                            if next_room.id == transcribe_room_id_list[index]:
         
                                steps_list.append(exit)
                                current_room = next_room
                                traversal_path.append(exit)
                                break
                print(steps_list)
                return steps_list

            transcribe_steps_list(bfs(track_old_room, current_room_id), track_old_room)



            track_old_room = current_room


# if it not in the list
# add it to the list
# for each neighbor of the node,
            for eachNeighbor in current_room.get_exits():
# we add that node to the stack
                next_room = current_room.get_room_in_direction(eachNeighbor)
                stack.append(next_room)
                rooms_visited[current_room_id][eachNeighbor] = next_room.id

    


walk(player)







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

print("Traverse", traversal_path)
