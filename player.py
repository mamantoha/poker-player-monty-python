import random

class Player:
    VERSION = "Default Python folding player"

    def search_player(name, game_state)
        for p in game_state['players']:
            if p['name'] == name:
                return p

    def betRequest(self, game_state):
        try:
            me = search_player('Monty Python', game_state)
            print me
            print "before"
            for player in  game_state['players']:
                if player['name'] == 'Monty Python':
                    print 'found'
                    for card in player['hole_cards']:
                        if card['rank'] == 'A':
                            print "all in", player['stack']
                            #return player['stack']
                            return random.randrange(100,300,5)
            print "after"
        except:
            print "Fuck"
            return random.randrange(100,300,5)

    def showdown(self, game_state):
        pass

