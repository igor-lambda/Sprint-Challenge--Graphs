from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
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
graph_dict = {}

'''
The player travels by player.travel(direction), however we must
have a way to travel to a random room from a given room, and to 
check for unexplored room so as not to backtrack our old steps.
'''

# This step creates a room in our graph_dict
def create_vertex(self, room):
    room_dict = {}
    for e in room.get_exits():
        room_dict[e] = "?"
        graph_dict[player.current_room.id] = room

# Here we append any room which is unknown to a list, and select
# one randomly
def get_random_blind_exit(room):
    blind = []
    for e in room.get_exits():
        # rooms in our graph_dict are refernced by id
        if graph_dict[room.id][e] == "?":
            blind.append(e)

    return random.choice(blind)


player.current_room.get_exits()
print('lll', random.choice([2, 3, 4, 5]))

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
