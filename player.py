import random

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        comm = game_state['community_cards']
        my = self.me(game_state)['hole_cards']
        me = self.me(game_state)

        if self.pair(comm, my):
            return me['stack']
            
        if self.ace(comm, my):
            return me['stack']
            
        return random.randrange(100,300,5)

    def showdown(self, game_state):
        pass

    def me(self, game_state):
        return game_state['players'][game_state['in_action']]

    def ace(self, comm, my):
        for card in my:
            if card['rank'] == 'A':
                return True

    def pair(self, comm, my):
        for card in my:
            same = [comm_card for comm_card in comm if card['rank'] == comm_card['rank']]
            if len(same) > 0 :
                return True
        return False
        
        

