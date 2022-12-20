# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов. Вам необходимо написать программу, которая позволит составить список гостей. В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.
#
# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class Client:
    def __init__(self, name, surname, city, balance):
      self.name = name
      self.surname = surname
      self.city = city
      self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс {self.balance} руб.'

    def get_guest(self):
        return f'{self.name} {self.surname}, {self.city}'

client_1 = Client('Иван','Петров','Москва', 50)
client_2 = Client('Мария', 'Иванова', 'Москва', 100)
client_3 = Client('Валерий', 'Виноградов', 'Коломна', 80)
client_4 = Client('Игорь', 'Костров', 'Обнинск', 30)
client_5 = Client('Светлана', 'Рогова', 'Ярославль', 60)

guest_list = [client_1, client_2, client_3, client_4, client_5]

for guest in guest_list:
    print(guest.get_guest())



