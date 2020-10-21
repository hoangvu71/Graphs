import random
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # add as many users as num_users
        # for num in range numusers, we add user
        for user in range(num_users):
            self.add_user(user)


        # Create friendships
        # we can create a random add each time
        # for a random user(0-10), add a random friend(0-10)
        count = 0
        friendship_visited = {}
        while count < avg_friendships * num_users:
            random_user = random.randint(1, num_users)
            random_friend = random.randint(1, num_users)

            if random_user != random_friend and (random_user, random_friend) not in friendship_visited and (random_friend, random_user) not in friendship_visited:
                friendship_visited[random_user, random_friend] = True
                friendship_visited[random_friend, random_user] = True
                self.add_friendship(random_user, random_friend)
                count += 2

        print(self.friendships[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # this is actually not that bad
        # what we can do is to traverse the graph using that starting node and breath-first traversal
        # add all those nodes that we traveled into a visted_node set

        def get_neighbors(node):
            return self.friendships[node]
        # make queue
        queue = []
        # make visited_nodes
        visited_node = set()
        # add user_id to queue
        queue.append(user_id)
        # while queue size > 0
        while len(queue) > 0:
        # node = dequeue
            node = queue.pop(0)
        # check if node is in list visitednode
            if node not in visited_node:
        # if not, add the node in the list
                visited_node.add(node)
        # check the surround neighbor node, we will need to make a get_neighbors(node) for that
                for neighbor in get_neighbors(node):
                    queue.append(neighbor)
        # then add all the neighbor to the queue


        print("Visited", visited_node)







        # so from the above, what we will get is essential all the friends that are connected to starting node ( however far away that maybe )
        # once we have the friends
        # we can just call a function
        # called get_destination(starting_node, destination_node) where starting node is self explainatory,
        # destination node will be one of the friends ( or friend's friend, again, however far away that maybe)
        def get_destination(starting_node, destination_node):
            # in this function we will return the paths tot he destination node
            # and because this is the shortest path, we will use bfs again

            # make queue
            queue = []
            visited_node = set()
            # add path to queue, it's the path [starting node]
            queue.append([starting_node])
            # if starting node is the destination node
            # return the path of starting node
            if starting_node == destination_node:
                return [starting_node]
            # while queue size is > 0
            while len(queue) > 0:
            # dequeue the path
                path = queue.pop(0)
            # node = path[-1]
                node = path[-1]
            # check if the node is in list of visited_node
                if node not in visited_node:
                    visited_node.add(node)
            # if not, add it in
            # check the neighbor
                    for neighbor in get_neighbors(node):
            # make a new path
                        new_path = list(path)
            # add the neighbor
                        new_path.append(neighbor)
            # if the neighbor is the destination node
                        if neighbor == destination_node:
            # just return the path
                            return new_path
            # add the new path to the queue
                        queue.append(new_path)

        # now that we have the function
        # we can call  for each friend, we will call the starting node and destination node (each friend)
        # then we will add the result to the visited[eachfriend] = path

        for eachFriend in visited_node:
            visited[eachFriend] = get_destination(user_id, eachFriend)


        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
