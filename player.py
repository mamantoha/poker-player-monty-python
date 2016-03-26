import random

class Player:
    VERSION = "Default Python folding player"

    def search_player(self, name, game_state):
        for p in game_state['players']:
            if p['name'] == name:
                return p

    def betRequest(self, game_state):
        for player in  game_state['players']:
            if player['name'] == 'Monty Python':
                print 'found'
                for card in player['hole_cards']:
                    if card['rank'] == 'A':
                        print "all in", player['stack']
                        return player['stack']
        return random.randrange(100,300,5)

    def showdown(self, game_state):
        pass

    def me(self, game_state):
        return game_state['players'][game_state['in_action']]


    def has_pair(self, game_state):
        comm_cards = game_state['community_cards']
        my_cards = self.me(game_state)['hole_cards']
        for my_card in my_cards:
            same = [comm_card for comm_card in comm_cards if my_cards['rank'] == comm_card['rank']]
            if len(same) > 0 :
                return True
        return False
        
        

