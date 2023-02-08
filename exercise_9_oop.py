#==================================1. Завдання (Напишіть клас автомобіля)===========================================
class Auto:
    def __init__(self, model, color, engine):
        self.model = model
        self.color = color
        self.engine = engine

    def drive_back(self):
        return 'drive back method'

    def drive_forward(self):
        return 'drive forward method'

class Truck(Auto):

    def turn_left(self):
        return 'turn left method'

    def turn_right(self):
        return 'turn right method'

man = Truck('Johndeer', 'v170', 6.0)
print(man.turn_right())


#===================3. Завдання (Клас паралелограм та клас квадрат)=====================================================
import math
class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return math.sqrt(self.width**2 - self.length**2)*self.length
    """
    якщо у нас паралелограм, діагональ якого перпендикулярна до його сторони, то в нас паралелограм
    складається з двох прямокутних трикутників. Я взяв width як бокову сторону паралелограма,
    а length як нижню або верхню сторону. Тому щоб знайти площу паралелограма, потрібно знайти площу трикутника
    помножену на 2. Площа прямокутного трикутника дорівнює добутку сторін прилеглих до прямого кута поділено на 2.
    Так як однієї сторони трикутника, а саме висоти або діагоналі в нашому випадку паралелограма ми не знаємо,
    то потрібно її знайти. Її квадрат буде дорівнювати width в квадраті мінус length в квадраті.
    Так як квадрат нам не потрібен, через бібліотеку math ми убираємо квадрат за допомогою квадратного кореня.
    І фінально не ділемо на 2 наше рішення, тому що так як повинна бути площа паралелограма, ми повинні будемо поділити
    на 2 для площі трикутника і знову помножити на 2, так як паралелограм у нас з двох однакових трикутників
    """
area_parallelogram = Parallelogram(6, 5)
print(area_parallelogram.get_area())

class Square(Parallelogram):
    def get_area(self):
        if self.width == self.length:
            return self.width * self.width
        else:
            return f'Введені дані {self.length} та {self.width} не рівні, тому розрахунок неможливий. У квадрата сторони повинні бути рівними'

    """
    Для квадрату я перопреділив метод з класу parallelogram. Але так як для квадрату що width що length 
    э його сторонами. То за основу ми можемо взяти саме атрибути з батьківсього методу, змінивши умову розрахунку
    площі в дочірньому методі, враховуючи що це саме квадрат і його сторони повинні бути рівними.
    """
area_square = Square(5, 5)
print(area_square.get_area())


#====================================================2. Завдання=======================================================
class TextProcessor:

    def get_clean_string(self, text):
        temporary_string = ''.join([i for i in str(text) if i.isalnum() or i == ' '])
        return temporary_string

    def __is_punktiantian(self, *args):
        for i in str(*args):
            if i.isalnum() or i == ' ':
                return True
            else:
                return False

    def print_is_punktiantian(self):
        return self.__is_punktiantian('12df $#$w')
    '''
    в умові def print_is_punktiantian не було, але я записав щоб дійсно перевірити приватний метод
    '''

# n = TextProcessor()
# # print(n.get_clean_string('Hello%%%% Who are you????2233'))
# # print(n.print_is_punktiantian())

class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ''

    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print('Виводиться очищений текст')
        return self.__clean_string


class Datainterface:
    def __init__(self):
        self._text_loader = TextLoader()

    def process_texts(self, data):
        for text in data:
            self._text_loader.set_clean_text(text)
            print (self._text_loader.clean_string)

data = ['hellooo12$$$3!','How are (you)?']
yy = Datainterface()
yy.process_texts(data)

#!!!Примітка для вчителя. По класу TextProcessor я зробив алгоритм, який залишає тільки цифри, букви та пробіли.
# Тому що в деяких тлумаченнях про знаки пунктуації, дужки або інші види скобок не вважаються знаками пунктуації.
# Вирішив убрати всі спец символи. Але якщо треба, можу переробити залишивши більш простий цикл
# for i in '.,!?{}[]():";'