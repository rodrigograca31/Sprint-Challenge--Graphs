from room import Room
from player import Player
from world import World
from collections import deque

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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


# DFT/S - Breath First Traversal
q = deque()
q.append([player.current_room])
visited = set()

my_graph = {}
my_graph[player.current_room.id] = {}


last_dir = None
prev_room = None
path_length = 1
while len(q) > 0:
    room_path = q.pop()
    # print("back=?")
    current_room = room_path[-1]

    # if len(room_path) > path_length:

    #     print("forward")
    # else:
    #     print("back")

    # path_length = len(room_path)

    # print()

    # if len(room_path) > 1:
    #     print(room_path[-2].id)
    #     print(current_room.id)
    #     prev_room = room_path[-2]

    # print(room_path)
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

            q.append(
                room_path + [current_room.get_room_in_direction(direction)])

            last_dir = direction
            # traversal_path.append(last_dir)
            # print("go", direction)

            # else:
            #     print("back")
            #     print(current_room.id)
        # print("forward?")
        # print(current_room.id)
        # print(direction)
        # print(q[-1])
    # else:
        # print("back 2")
        # print(current_room.id)
        # print(direction)
        # print(q[-1])
        # print(my_graph)
        # print(my_graph[current_room.id])
        # print("visited", current_room.id)
    #     print(room_path)
    # print(last_dir)

# print()
# print(traversal_path)
# print()
# print(my_graph)
# print()

print("====================================")
print("====================================")

# DFT/S - Breath First Traversal
# q = deque()
# qq = deque()
# q.append([0])
# qq.append(["e"])
# visited = set()

# # print(qq)

# while len(q) > 0:
#     room_path = q.pop()
#     # dirr = qq.pop()
#     current_room = room_path[-1]
#     # print(dirr)

#     if current_room not in visited:

#         print(current_room)
#         visited.add(current_room)
#         for room in my_graph[current_room]:
#             # print(my_graph[current_room][room])
#             # if my_graph[current_room][room] not in visited:
#             # print("visited", my_graph[current_room][room], "already")
#             q.append(room_path + [my_graph[current_room][room]])
#             # print("room", )
#             # if my_graph[current_room][room] not in visited:
#     qq.append([room])
#     # else:
#     # print("dont try")
#     # print(current_room)
#     # print("aa")
#     # print(current_room)
#     # print()

# print(qq)


def dft_recursive(starting_vertex, visited=set(), direction=None):
    """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

    if starting_vertex not in visited:
        # print(starting_vertex)
        # print(direction)
        traversal_path.append(direction)
        # print()
        visited.add(starting_vertex)

        # directions = my_graph[starting_vertex]
        # directions = list(directions)
        # random.shuffle(directions)

        for next_vertex in my_graph[starting_vertex]:
            # print(next_vertex)
            # print(my_graph[starting_vertex][next_vertex])
            # pass
            dft_recursive(my_graph[starting_vertex]
                          [next_vertex], visited, next_vertex)
            # print("aaaaa")

        # print(len(q), visited)
        if len(visited) >= len(room_graph):
            # print("aaaaaaa")
            return

        if direction == "n":
            # print("s")
            traversal_path.append("s")
        if direction == "s":
            # print("n")
            traversal_path.append("n")
        if direction == "e":
            # print("w")
            traversal_path.append("w")
        if direction == "w":
            # print("e")
            traversal_path.append("e")


dft_recursive(0, set())
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
