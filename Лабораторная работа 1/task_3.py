list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

count_of_players = len(list_players)
half = count_of_players//2

team1 = list_players[:half]
team2 = list_players[half:]
print(team1)
print(team2)
