def is_preflop(game_state):
    return len(game_state["community_cards"]) == 0
