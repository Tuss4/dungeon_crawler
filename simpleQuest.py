'''Simple Quest
Date: 6/6/2014
Author: Tomjo Soptame
Description: Sleepy Giant code
challenge game.
'''


class Player:
    def __init__(self, name):
        self.name = name


class Room:
    def __init__(self, name):
        self.name = name

class Grue:
    pass


def main():
    player_name = raw_input('Enter your name: ')
    player = Player(player_name)
    print "Welcome, {}!".format(player.name)
    room_name = raw_input('Enter a room name: ')
    room = Room(room_name)
    print room.name

if __name__ == '__main__':
    main()