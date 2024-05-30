def create_cook_book(file_path):
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()
            i += 1

            if i < len(lines):
                ingredient_count = int(lines[i].strip())
                i += 1
            else:
                break

            ingredients = []
            for _ in range(ingredient_count):
                if i < len(lines):
                    ingredient_info = lines[i].strip().split(' | ')
                    if len(ingredient_info) == 3:
                        ingredient_dict = {
                            'ingredient_name': ingredient_info[0],
                            'quantity': int(ingredient_info[1]),
                            'measure': ingredient_info[2]
                        }
                        ingredients.append(ingredient_dict)
                    i += 1
                else:
                    break

            cook_book[dish_name] = ingredients

    return cook_book




file_path = 'recipes.txt'
cook_book = create_cook_book(file_path)
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
            else:
                shop_list[ingredient_name]['quantity'] += quantity

    return shop_list


dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
print(shop_list)