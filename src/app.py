def calculate_streak(habit_checkins: list) -> int:
    """..."""
    streak = 0
    for done in reversed(habit_checkins):
        if not done:
            break
        streak += 1
    return min(streak, 365)    # ← ЭТА СТРОКА ИЗМЕНЕНА
    print(f"...: {streak}")
    return streak