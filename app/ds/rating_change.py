def calculate_rating_change(
    current_rating: float,
    opponent_avg_rating: float,
    game_wins: int,
    game_losses: int,
    past_game_count: int
) -> float:
    total_games = game_wins + game_losses
    if total_games == 0:
        return 0.0

    # Expected score using Elo formula
    expected_score = 1 / (1 + 10 ** ((opponent_avg_rating - current_rating) / 400))
    actual_score = game_wins / total_games

    # Dynamic K-factor based on total career games (faster for new players)
    if past_game_count < 30:
        k_factor = 40  # very fast adjustment for new players
    elif past_game_count < 100:
        k_factor = 24  # medium adjustment
    else:
        k_factor = 16  # stable for experienced players

    # Apply rating change scaled by how many games were played in this match set
    change = k_factor * (actual_score - expected_score) * (total_games / 5)  # 5 = full session size

    return round(change, 2)

