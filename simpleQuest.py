'''Simple Quest
Date: 6/6/2014
Author: Tomjo Soptame
Description: Sleepy Giant code
challenge game.
'''

import pprint


class Player:
    '''The player class. Keeps track of player's location,
    and gems.'''

    def __init__(self, name, room=None):
        self.name = name
        self.room = room

    # Get the player's current location.
    def get_room(self):
        return self.room

    # The function that helps you navigate the map!
    # Takes the object itself and a direction.
    def move(self, direction):
        room = self.room
        if direction in room.all_exits.keys():
            self.room = room.all_exits[direction]
            return 'You are now in {}!'.format(self.room)
        else:
            return "Sorry you can't move that way," +\
                   "try a different direction."



class Room:
    '''The room class. Initialize an instance with at least a room name.
    Keeps track of room exits and gems.'''

    def __init__(self, name):
        self.name = name
        self.all_exits = {}

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


class Grue:
    pass


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

    def all_exits(self):
        return pprint.pprint([{i.name: i.get_exits()} for i in self.ALL])


def main():
    player_name = raw_input('Enter your name: ')
    player = Player(player_name)
    print "Welcome, {}!".format(player.name)
    room_name = raw_input('Enter a room name: ')
    room = Room(room_name)
    player.room = room 
    print player.get_room()


if __name__ == '__main__':
    main()