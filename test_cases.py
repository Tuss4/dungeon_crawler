'''
##################################
###                            ###
###   SIMPLE QUEST THE GAME    ###
###                            ###
##################################

Start Date: 6/6/2014
Finish Date: 6/11/2014
Author: Tomjo Soptame
Description: Testing scenarios for what happens
if the player has 5 gems.
'''
import random

from simpleQuest import (Player, Grue, Map,
                         grue_spawn_room,
                         pre_gems,
                         post_gems)


test_player = Player('Bacon Lord 53')
test_player.gems = 5


def test_cases(player):
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
    spawn_rooms = m.ALL
    # spawn_rooms.remove(m.c)
    player.room = random.choice(spawn_rooms)
    print "Welcome, %s! You are currently in: %s Room." %\
          (player.name, player.room.name)
    grue = Grue(grue_spawn_room(player.room))
    print grue.room

    pre_gems(player, grue, m)

    post_gems(player, grue, m)

if __name__ == '__main__':
    test_cases(test_player)
