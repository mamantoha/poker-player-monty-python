import random
from middleware import *
from rank import *


list_of_combinations = [('A', 'A', 'p'), ('K', 'K', 'p'), ('3', '3', 'p'), ('4', '4', 'p'), ('5', '5', 'p'),
                        ('6', '6', 'p'),('7', '7', 'p'),('8', '8', 'p'),('9', '9', 'p'),('10', '10', 'p'),('J', 'J', 'p'),('Q', 'Q', 'p')]

class Player:
    VERSION = "We are not afraid of the rabbit"

    def betRequest(self, game_state):
        try:
    
            comm = game_state['community_cards']
            my = self.me(game_state)['hole_cards']
            me = self.me(game_state)
            
            minimal_amount = int(game_state["minimum_raise"])
            player_count = get_me_player_count(game_state)
            get_rank = rank(my+comm)
            if (player_count > 2) and not is_preflop(game_state):
                offer = 0
                if get_rank > 4:
                    offer = minimal_amount
                return offer
            else:
                if self.pair(comm, my):
                    return self.more(game_state, me)
                elif self.ace(comm, my):
                    return self.more(game_state, me)
                elif self.flush(comm, my):
                    return self.more(game_state, me)
        except:
            pass
        minimal_amount = int(game_state["minimum_raise"])
        return minimal_amount

    def showdown(self, game_state):
        pass

    def more(self, game, me):
        return min(game['current_buy_in'] * 2 , me['stack'])

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
            if len(same) >= 1 :
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
