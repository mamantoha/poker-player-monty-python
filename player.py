import random

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
#        for player in  game_state['players']:
#            if player['name'] == 'Monty Python':
#                for card in player['hole_cards']:
#                    if card['rank'] == 'A':
#                        return player['stack']
        return random.randrange(100,500,5)

    def showdown(self, game_state):
        pass

