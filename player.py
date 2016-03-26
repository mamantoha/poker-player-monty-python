import random

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        comm = game_state['community_cards']
        my = self.me(game_state)['hole_cards']
        me = self.me(game_state)

        if self.pair(comm, my):
            return self.more(game_state, me)
        elif self.ace(comm, my):
            return self.more(game_state, me)
        elif self.flush(comm, my):
            return self.more(game_state, me)
        
        minimal_amount = int(game_state["minimum_raise"])
        return minimal_amount

    def showdown(self, game_state):
        pass

    def more(self, game, me):
        min(game['current_buy_in'] * 2 , me['stack'])

    def me(self, game_state):
        return game_state['players'][game_state['in_action']]

    def ace(self, comm, my):
        for card in my:
            if card['rank'] in ['A', 'K']:
                return True
        return False

    def pair(self, comm, my):
        for card in my:
            same = [comm_card for comm_card in comm if card['rank'] == comm_card['rank']]
            if len(same) > 0 :
                return True
        return False
        
        

    def flush(self, comm, my):
        cards = comm + my
        card_map = {}
        for card in cards:
            if card_map.has_key(card['suit']):
                card_map[card['suit']] += 1
            else:
                card_map[card['suit']] = 1                
        if max(card_map.values()) >= 5:
            return True

        return False
