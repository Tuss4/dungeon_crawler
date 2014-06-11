from simpleQuest import Player


test_player = Player('Bacon Lord 53')
test_player.gems = 5

def test_cases(player):
	print (player.name, player.gems)

if __name__ == '__main__':
	test_cases(test_player)
