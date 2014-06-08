'''Simple Quest
Date: 6/6/2014
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

    # Initialize a Grue with 5 gems.
    def __init__(self):
        self.gems = 5


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

    # Return every room instance in map.
    ALL = [a, o, b, cr, e, l, vl, v, c]

    # Return all exits in the map. Rooms are dict keys.
    @staticmethod
    def all_exits(rooms):
        return pprint.pprint([{i.name: i.get_exits()} for i in rooms])


def main():
    '''This function runs the game.'''
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
    spawn_rooms.remove(m.c)
    if player_name != "":
        player = Player(player_name, random.choice(spawn_rooms))
        player.room.has_player = True
        print "Welcome, %s! You are currently in: %s Room." %\
              (player.name, player.room.name)
        print player.turns

        # As long as the conditions for winning have
        # not been met, the game will continue.
        while player.gems < 5:
            if player.turns % 4 != 0 or player.turns == 0:
                print 'Make a move! Remember type: n, s, e, w to try a door.'
                door = raw_input()
                print player.move(door)
            else:
                print 'Time for a rest! THE GRUE\'S GETTING CLOSER!'
                player.turns +=1
    else:
        main()


if __name__ == '__main__':
    main()
