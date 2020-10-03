from django.db.models import Avg, Max, Min

def calculate_max_season(game, all_games):
    max_points = 0

    for item in all_games:
        if item.points > max_points:
            max_points = item.points

        if item.id == game.id:
            break
    return max_points

def calculate_min_season(game, all_games):
    min_points = all_games.aggregate(Max('points'))['points__max']

    for item in all_games:
        if item.points < min_points:
            min_points = item.points

        if game.id == item.id:
            break
    return min_points

def is_min_break(game, all_games):
    min_season = calculate_min_season(game, all_games)
    is_break = False

    for i, game_item in enumerate(all_games):
        if i != 0:
            if game_item.points < min_season:
                min_season = game_item.points
                is_break = True
            else:
                is_break = False
        else:
            min_season = game_item.points
        
        if game.id == game_item.id:
            return is_break

def is_max_break(game, all_games):
    max_season = 0
    is_break = False

    for i, game_item in enumerate(all_games):
        if i != 0:
            if game_item.points > max_season:
                max_season = game_item.points
                is_break = True
            else:
                is_break = False
        else:
            max_season = game_item.points
        
        if game.id == game_item.id:
            return is_break

def get_break_max_amount(game, all_games):
    max_points = 0
    break_counter = 0
    for i, game_item in enumerate(all_games):
        if i != 0:
            if game_item.points > max_points:
                max_points = game_item.points
                break_counter = break_counter + 1
        else:
            max_points = game_item.points

        if game is not None and game.id == game_item.id:
            return break_counter
    return break_counter

def get_break_min_amount(game, all_games):
    min_points = all_games.aggregate(Max('points'))['points__max']
    break_counter = 0

    for i, game_item in enumerate(all_games):
        if i != 0:
            if game_item.points < min_points:
                min_points = game_item.points
                break_counter = break_counter + 1
        else:
            min_points = game_item.points
        
        if game is not None and game.id == game_item.id:
            return break_counter
    return break_counter
