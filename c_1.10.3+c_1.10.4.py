class Client:
    def __init__(self, first_name, last_name, city, balance=0.0, status=0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance
        self.status = status

    def info_client(self):
        return f"Имя: {self.first_name}, Фамилия: {self.last_name}, Город: {self.city}, Баланс: {self.balance} руб., Статус: {self.status}"

client_1 = Client("Василий", "Васильев", "Москва", "120", "Новичёк")
client_2 = Client("Асклепий", "Корсаков", "Новгород", "200", "Настаник")
print(client_1.info_client())
print(client_2.info_client())