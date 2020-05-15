from room import Room
from player import Player
from world import World
from collections import deque

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


# DFT/S - Depth First Traversal
s = deque()
s.append([player.current_room])
visited = set()

my_graph = {}
my_graph[player.current_room.id] = {}


while len(s) > 0:
    room_path = s.pop()
    current_room = room_path[-1]

    if current_room not in visited:
        visited.add(current_room)

        my_graph[current_room.id] = dict.fromkeys(current_room.get_exits())

        for direction in current_room.get_exits():
            # print(direction)

            # traversal_path.append(current_room.get_room_in_direction(room))
            # print(current_room.get_room_in_direction(room))

            my_graph[current_room.id][direction] = current_room.get_room_in_direction(
                direction).id
            # avoids going back to the room it came from!?
            # if current_room.get_room_in_direction(direction) not in visited:

            s.append(
                room_path + [current_room.get_room_in_direction(direction)])


# print()
# print(traversal_path)
# print()
# print(my_graph)
# print()

print("====================================")
print("====================================")


def dft_recursive(starting_vertex, visited=[], direction=None):

    if starting_vertex not in visited:

        visited.append(starting_vertex)
        traversal_path.append(direction)

        # uncomment and use directions array/list in the for loop to randomly save some steps
        # directions = my_graph[starting_vertex]
        # directions = list(directions)
        # random.shuffle(directions)

        for next_vertex in my_graph[starting_vertex]:

            dft_recursive(my_graph[starting_vertex]
                          [next_vertex], visited, next_vertex)

        if len(visited) >= len(room_graph):
            return

        if direction == "n":
            traversal_path.append("s")
        if direction == "s":
            traversal_path.append("n")
        if direction == "e":
            traversal_path.append("w")
        if direction == "w":
            traversal_path.append("e")


dft_recursive(0)

# traversal_path.pop()
traversal_path = traversal_path[1:]  # removes None
print()

for move in traversal_path:
    # print(move)
    player.travel(move)
    # print(player.current_room.id)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
