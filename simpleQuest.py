'''Simple Quest
Date: 6/6/2014
Author: Tomjo Soptame
Description: Sleepy Giant code
challenge game.
'''


class Player:
    '''The player class. Keeps track of player's location,
    and gems.'''

    def __init__(self, name):
        self.name = name
        self.room = None

    # Get the player's current location.
    def get_room(self):
        return self.room

    # The function that helps you navigate the map!
    # Takes the object itself and a direction.
    def move(self, direction):
        print direction
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

    def __init__(self, name, north=None, south=None, east=None, west=None):
        self.name = name
        self.all_exits = {}
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

    # Default string representation of the instance.
    def __str__(self):
        return self.name


class Grue:
    pass


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