# Подаем на вход последовательность чисел, преобразуем в список
# array = [int(x) for x in input("Введите последовательность чисел через пробел:").split()]
array = [10,8,3,5,6,66,77,123]
# Сортируем список по возрастанию элементов в нем методом сортировки
def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Выводим отсортированный список
array_sort = merge_sort(array)
print(array_sort)


#  Запрашиваем у пользователя любое число и проверяем, что оно соответствует указанному в условии ввода данных
while True:
    try:
        user_element = int(input('Введите любое число:'))
        break
    except ValueError:
        print('Вы ввели не число, попробуйте снова: ')

# Реализуем функцию, в которой устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу
def binary_search(array_int, element, left, right):
    if max(array_int) < element:
        return print('введенное число больше максимального элемента в списке')
    if min(array_int) > element:
        return print('введенное число меньше минимального элемента в списке')

    middle = (right + left) // 2  # находим середину
    if array_int[middle] == element:
        return middle  # возвращаем этот индекс
    elif element < array_int[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array_int, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array_int, element, middle + 1, right)

element_pos = binary_search(array_sort, user_element, 0, len(array_sort)-1)
if element_pos is not None: # нельзя просто писать If element_pos. Там мы приводим переменную к Bool и None = 0
    print('номер позиции элемента в отсортированном списке, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу:', element_pos)


