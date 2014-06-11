'''
##################################
###                            ###
###   SIMPLE QUEST THE GAME    ###
###                            ###
##################################

Start Date: 6/6/2014
Finish Date: 6/10/2014
Author: Tomjo Soptame
Description: Sleepy Giant code challenge game.
'''

import random
import pprint


class Player:
    '''The player class. Keeps track of player's location,
    and gems.'''

    # Initialize a player with a name.
    def __init__(self, name, room=None):
        self.name = name
        self.room = room
        if self.room:
            self.room.has_player = True
        self.gems = 0
        self.turns = 0

    # Get the player's current location.
    def get_room(self):
        return self.room

    # The function that helps you navigate the map!
    # Takes the object itself and a direction.
    def move(self, direction):
        room = self.room
        room.has_player = False
        if direction in room.all_exits.keys():
            self.room = room.all_exits[direction]
            self.room.has_player = True
            self.turns += 1
            return 'You are now in %s Room! You have %i turns left before rest.' %\
                   (self.room, 4-self.turns)
        else:
            return "Sorry you can't move that way," +\
                   "try a different direction."

    # You get attacked by the Grue.
    # Oh noes.
    def death(self, rooms):
        self.gems = 0
        self.room.has_player = False
        new_room = random.choice(rooms.ALL)
        self.room = new_room
        self.room.has_player = True
        return 'Game Over. You died. Re-spawning in %s with 0 gems.' %\
               (self.room)


class Room:
    '''The room class. Initialize an instance with at least a room name.
    Keeps track of room exits and gems.'''

    # Initialize a room with a name.
    def __init__(self, name):
        self.name = name
        self.all_exits = {}
        self.has_player = False
        self.has_grue = False

    # Setup your room exits.
    def set_exits(self, north=None, south=None, east=None, west=None):
        if north:
            self.all_exits['n'] = north
        if south:
            self.all_exits['s'] = south
        if east:
            self.all_exits['e'] = east
        if west:
            self.all_exits['w'] = west

    # Return all exits in the room!
    def get_exits(self):
        return self.all_exits

    # Default instance representation.
    def __repr__(self):
        return '<Room: {}>'.format(self.name)

    # Default string representation of the instance.
    def __str__(self):
        return self.name


class Grue(Player):
    '''The Grue aka THE ANTAGONIST. If he attacks you,
    you lose all your gems and you re-spawn in a random
    location. Moves every rest turn. If the Grue flees
    it drops a gem.'''

    # Initialize a Grue with 5 gems and a spawn room.
    def __init__(self, room=None):
        self.gems = 5
        self.room = room
        if self.room:
            self.room.has_grue = True

    # Using the path of rooms returned from
    # BFS algorithm turn that room into a door key
    # in the exit dictionary.
    def room_to_exit(self, room):
        for k, v in self.room.all_exits.iteritems():
            if v == room:
                return k

    # Override the inherited move function
    # to account for the BFS algorithm.
    def move(self, path_room):
        door = self.room_to_exit(path_room)
        self.room.has_grue = False
        new_room = self.room.all_exits[door]
        new_room.has_grue = True
        self.room = new_room

    # If a player actively enters a room containing a grue,
    # the grue will flee leaving a gem behind.
    def flee(self, player):
        room = self.room
        self.room.has_grue = False
        self.gems -= 1
        player.gems += 1
        new_room = room.all_exits[random.choice(room.all_exits.keys())]
        new_room.has_grue = True
        self.room = new_room

        return '{}, you just picked up a gem. Careful a grue must be nearby!'.\
               format(player.name) + ' You have {} gem(s).'.format(player.gems)


class Map:
    '''Initialize our playable map of rooms'''
    # Instantiate all the rooms.
    a = Room('Aquamarine')
    o = Room('Ochre')
    b = Room('Burnt Sienna')
    cr = Room('Chartreuse')
    e = Room('Emerald')
    l = Room('Lavender')
    vl = Room('Violet')
    v = Room('Vermillion')
    c = Room('Cobalt')

    # Setup the exits.
    a.set_exits(None, vl, None, c)
    o.set_exits(v, o, cr)
    b.set_exits(e, None, l)
    cr.set_exits(o, e)
    e.set_exits(None, a, l, c)
    l.set_exits(None, None, cr, b)
    vl.set_exits(None, b, b, cr)
    v.set_exits(None, a, o)
    c.set_exits(v, b, None, v)

    # Set the teleportation room
    TELEPORTATION_ROOM = c  # Default is set to Cobalt.

    # Return every room instance in map.
    ALL = [a, o, b, cr, e, l, vl, v, c]

    # Graph of map
    graph = {r: [[k, v] for k, v in r.all_exits.iteritems()]for r in ALL}

    # Return all exits in the map. Rooms are dict keys.
    @staticmethod
    def all_exits(rooms):
        return pprint.pprint([{i.name: i.get_exits()} for i in rooms])


def bfs_path(map, grue_room, player_room):
    '''
    Using a Breadth First Search algorithm to compute the shortest
    path to the player's room for the grue.

    BFS Algorithm Python implementation adapted from StackOverflow answer:
    http://stackoverflow.com/a/8922151/1781091
    '''

    queue = []

    queue.append([grue_room])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == player_room:
            return path
        for adj in map.get(node, []):
            new_path = list(path)
            new_path.append(adj[1])
            queue.append(new_path)


def grue_spawn_room(player_room):
    '''Generate a random room for the Grue to spawn in,
    based upon the player's spawn room.'''

    # Set the level one exit key
    level_one_key = random.choice(player_room.all_exits.keys())

    # Set the first random room
    level_one_room = player_room.all_exits[level_one_key]

    # Set the second exit key
    grue_room_key = random.choice(level_one_room.all_exits.keys())

    # Set the grue room!
    grue_room = level_one_room.all_exits[grue_room_key]

    # Return it!
    return grue_room


def game_status(status, player=None, map=None):
    '''Print out a game status message.'''

    if status == 'ohno':
        print 'OH NO... It\'S THE GRUE!'
    elif status == 'close':
        print 'The Grue is getting closer.'
    elif status == 'victory':
        print '''
              YOU WON! Congratulations, {}!\nHit ^D to quit.
              '''.format(player.name)
    elif status == 'teleport':
        print '''
              {0}, you have {1} gems. Find the {2} room!
              '''.format(player.name,
                         player.gems,
                         map.TELEPORTATION_ROOM)


def player_can_move(player):
    '''Function to make sure the player has the ability to take a turn.'''

    if player.turns % 4 != 0 or player.turns == 0:
        return True
    else:
        return False


def player_input(output_text, player=None):
    '''Standard output prompt for player turns.'''

    instructions = ' Type: n, s, e, w:'
    if output_text == 'move':
        print 'Make a move!{}'.format(instructions)
    elif output_text == 'grue':
        print 'Move carefully, the grue is near!{}'.format(instructions)
    elif output_text == 'rest':
        print '''
              {0}, you\'ve moved quite a bit. Rest up.
              You currently have: {1} gem(s).
              '''.format(player.name, player.gems)


def main():
    '''This function runs the game.'''

    # Stylized title, yo!
    title = '''
            ##################################
            ###                            ###
            ###   SIMPLE QUEST THE GAME    ###
            ###                            ###
            ##################################
            '''
    # Initialize our Map.
    m = Map()

    # Initialize player and spawn them in a
    # random room.
    print title
    player_name = raw_input('Enter your name: ')
    spawn_rooms = m.ALL
    # spawn_rooms.remove(m.c)
    if player_name != "":
        player = Player(player_name, random.choice(spawn_rooms))
        print "Welcome, %s! You are currently in: %s Room." %\
              (player.name, player.room.name)
        grue = Grue(grue_spawn_room(player.room))
        print grue.room

        # As long as the conditions for winning have
        # not been met, the game will continue.
        while player.gems < 5:
            if player_can_move(player):
                if player.room.has_grue:
                    print grue.flee(player)
                    player_input('grue')
                    door = raw_input()
                    print player.move(door)
                player_input('move')
                door = raw_input()
                print player.move(door)
            else:
                player_input('rest', player)
                path = bfs_path(m.graph, grue.room, player.room)
                # Uncomment the next line to see the Grue's path.
                # print path
                path_room = path[0]
                if len(path) > 1:
                    path_room = path[1]
                grue.move(path_room)
                if grue.room.has_player:
                    game_status('ohno')
                    print player.death(m)
                else:
                    game_status('close')
                player.turns = 0

        if player.gems == 5:
            if player_can_move(player):
                if player.room == m.TELEPORTATION_ROOM:
                    game_status('victory', player)
                else:
                    game_status('teleport', player, m)
            else:
                player_input('rest', player)
                player.turns = 0
    else:
        main()


if __name__ == '__main__':
    main()
