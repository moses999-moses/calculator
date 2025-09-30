class Calculator:
    def __init__(self):
        # Инициализация атрибутов класса
        self.otvet = 0  # Результат вычисления
        self.a = 1
        self.b = 1
        self.deistv = ""  

    def get_input(self):
        # Метод для получения входных данных от пользователя
        self.a = int(input("Введите первое число: "))  
        self.b = int(input("Введите второе число: "))  
        self.deistv = input("Выберите действие: +,-,*,/: ") 

    def calculate(self):  # Добавлен отсутствующий метод calculate
        # Основной метод для выполнения вычислений
        if self.deistv == '+':
            self.otvet = self.summa()
        elif self.deistv == '-':
            self.otvet = self.minus()
        elif self.deistv == '*':
            self.otvet = self.umnojenie()  
        elif self.deistv == '/':
            self.otvet = self.delenie()
        else:
            print("Неверное действие!")
            return False
        return True

    def summa(self):
        # Метод для сложения
        return self.a + self.b

    def minus(self):
        # Метод для вычитания
        return self.a - self.b

    def umnojenie(self):
        # Метод для умножения
        return self.a * self.b

    def delenie(self):
        # Метод для деления с проверкой деления на ноль
        if self.b == 0:
            print("Ошибка: деление на ноль!")
            return None
        return self.a / self.b

    def show_result(self): 
        # Метод для вывода результата
        print(f"Ответ: {self.otvet}")


# Создание экземпляра калькулятора
calc = Calculator()

# Получение данных от пользователя
calc.get_input()

# Выполнение вычисления и вывод результата
if calc.calculate():
    calc.show_result()