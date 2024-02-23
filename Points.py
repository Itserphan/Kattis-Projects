winner = 0
winner_grade = 0
for player in range(1,6):
    grades = [int(x) for x in input().split()]
    player_grade = sum(grades)
    if player_grade > winner_grade:
        winner = player
        winner_grade = player_grade
print(winner,winner_grade)


