import json


def cook_book_dict(path, book_dict=None):
    if book_dict is None:
        book_dict = {}
    with open(path, 'r', encoding='utf-8') as f:
        file_list = f.read().split('\n')

    temporary_list = []
    final_list = []

    for i in file_list:
        if i != '':
            temporary_list.append(i)
        else:
            final_list.append(temporary_list.copy())
            temporary_list.clear()
    final_list.append(temporary_list.copy())

    for i in final_list:
        book_dict[i[0]] = []
        for j in i[2:]:
            ingredient = j.split(' | ')
            book_dict[i[0]].append(
                {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})
    return book_dict


def get_shop_list_by_dishes(dishes, person_count, shop_list=None):
    if shop_list is None:
        shop_list = {}
    if not dishes:
        return 'Список пуст!'
    else:
        for i in dishes:
            if i not in cook_book_dict(recipes):
                print(f'{i} нет в книге рецептов!')
                break
            else:
                for j in cook_book_dict(recipes)[i]:
                    if j['ingredient_name'] not in shop_list:
                        shop_list[j['ingredient_name']] = {'measure': j['measure'],
                                                           'quantity': j['quantity'] * person_count}
                    else:
                        shop_list[j['ingredient_name']]['quantity'] += j['quantity'] * person_count
    return shop_list


recipes = "files/recipes.txt"

print(f'Задание 1:\n{json.dumps(cook_book_dict(recipes), sort_keys=False, indent=2, ensure_ascii=False)}\n')
print(f'Задание 2:\n{json.dumps(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2), sort_keys=False, indent=2, ensure_ascii=False)}')

