# TODO Напишите функцию find_common_participants

def find_common_participants(string_1: str, string_2: str, ch : str=","):
    items_set_1 = set(string_1.split(ch))
    items_set_2 = set(string_2.split(ch))
    intersection_list = list(items_set_1.intersection(items_set_2))
    intersection_list.sort()
    return intersection_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
intersection_list = find_common_participants(participants_second_group, participants_first_group, "|")
print(intersection_list)