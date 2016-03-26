def is_preflop(game_state):
    return len(game_state["community_cards"]) == 0

def get_me_player_count(game_state):
    return len(game_state["players"])
