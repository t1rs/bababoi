class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show_info(self):
        print(f"Имя: {self.__name}, Количество лет: {self.__age}")


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def update_info(self, new_name, new_age):
        self.__name = new_name
        self.__age = new_age

    def show_info(self):
        super().show_info()
        print(f"Должность: {self.position}")


class Manager(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def show_info(self):
        super().show_info()
        print(f"Отдел: {self.department}")


person1 = Person("Анна Иванова", 30)
employee1 = Employee("Иван Иванов", 25, "Прогаммный инженер")
manager1 = Manager("Мария Петрова", 35, "Человеческие ресурсы")

def display_info(person):
    person.show_info()

display_info(person1)
display_info(employee1)
display_info(manager1)
