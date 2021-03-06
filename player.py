import random
from middleware import *
from rank import *
from hands import sorryForMySlowness

list_of_combinations = [('A', 'A', 'p'), ('K', 'K', 'p'), ('3', '3', 'p'), ('4', '4', 'p'), ('5', '5', 'p'),
                        ('6', '6', 'p'),('7', '7', 'p'),('8', '8', 'p'),('9', '9', 'p'),('10', '10', 'p'),('J', 'J', 'p'),('Q', 'Q', 'p')]

players_map = {6 : 30,
                 5 : 48,
                 4 : 62,
                 3 : 83,
                 2 : 100}


class Player:
    VERSION = "We are not afraid of the rabbit"

    def betRequest(self, game_state):
        try:
    
            comm = game_state['community_cards']
            my = self.me(game_state)['hole_cards']
            me = self.me(game_state)
            
            player_count = get_me_player_count(game_state)
            get_rank = rank(my+comm)
            if is_preflop(game_state) and (player_count == 2):
                if game_state['current_buy_in'] < 200:
                    return game_state['current_buy_in']
            if not is_preflop(game_state):
                if get_rank > 0:
                    return self.more(game_state, me)
                else:
                    cond = []
                    cond += [self.overcard(comm, my) >= 2]
                    cond += [self.strit_draw(comm, my)]
                    cond += [self.flush_draw(comm, my)]
                    if cond.count(True) >= 2:
                        return self.more(game_state, me)
                return 0
            else:
                if sorryForMySlowness(my) <= players_map[player_count]:
                    return self.more(game_state, me)
                else:
                    return 0
        except:
            print "FUUUCCKK"
        return self.minimal(game_state, me)

    def showdown(self, game_state):
        pass

    def all_in(self, game, me):
        return me['stack']
    
    def more(self, game, me):
        return min(game['current_buy_in'] * 2 , me['stack'])

    def minimal(self, game, me):
        return int(game["minimum_raise"])

    def me(self, game_state):
        return game_state['players'][game_state['in_action']]

    def ace(self, comm, my):
        for card in my:
            if card['rank'] in ['A', 'K']:
                return True
        return False

    def pair(self, comm, my):
        for card in my:
            same = [comm_card for comm_card in comm + my if card['rank'] == comm_card['rank']]
            if len(same) >= 2 :
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

    def flush_draw(self, comm, my):
        cards = comm + my
        card_map = {}
        for card in cards:
            if card_map.has_key(card['suit']):
                card_map[card['suit']] += 1
            else:
                card_map[card['suit']] = 1                
        if max(card_map.values()) >= 4:
            return True

        return False
    

    def strit_draw(self, comm, my):
        cards = comm + my
        scores = sorted([self.card_score(card) for card in cards])
        max_len = 1
        for i in range(len(scores)):
            cur_len = 1
            prev = scores[i]
            for score in scores[i+1:]:
                if prev + 1 == score:
                    prev = score
                    cur_len += 1
                else:
                    break
            max_len = max(cur_len, max_len)
        return max_len >= 4

    def overcard(self, comm, my):
        max_comm = max([self.card_score(card) for card in comm])
        my_scores = [self.card_score(card) for card in my]
        return len([True for i in my_scores if i > max_comm])
    
    def card_score(self, card):
        try:
            return int(card['rank'])
        except:
            pass
        if card['rank'] == 'J':
            return 11
        elif card['rank'] == 'Q':
            return 12
        elif card['rank'] == 'K':
            return 13
        elif card['rank'] == 'A':
            return 14
        return 0

    
