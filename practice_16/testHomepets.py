from homepets import Cat

Cat1 = Cat('Семен', 'male', '2')
Cat2 = Cat('Флинт', 'male', '6')
Cat3 = Cat('Анфиса', 'female', '3')

cats = [Cat1, Cat2, Cat3]

for item in cats:
    if isinstance(item, Cat):
        if item.gender == 'male':
            gender_label = 'кот'
        else:
            gender_label = 'кошка'
        print(f'{gender_label} с именем {item.name}, возраст {item.age}')

    else:
        print('-----')


