import random

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            print "before"
            for player in  game_state['players']:
                if player['name'] == 'Monty Python':
                    print 'found'
                    for card in player['hole_cards']:
                        if card['rank'] == 'A':
                            print "all in", player['stack']
                            #return player['stack']
                            return random.randrange(100,300)
            print "after"
        except:
            print "Fuck"
            return random.randrange(100,300)

    def showdown(self, game_state):
        pass

