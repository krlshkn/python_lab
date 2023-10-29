# TODO Напишите функцию для поиска индекса товара

def find_index(items_list: list[str], item: str):
    for index in range(len(items_list)):
        if items_list[index] == item:
            return index
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# TODO Вызовите функцию, чтобы получить индекс товара
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
