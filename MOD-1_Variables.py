# Практическое задание по работе в Pycharm - "Переменные"




# Задача «Сложная сдача».

cherry_price = 34
cherry_kilo = 4.5
money = 500         # предполагаемая сумма
total_price = cherry_kilo * cherry_price
change = money - total_price

print('Сдача: ' + str(change) + ' рублей')
# допускаю -float- так как возможна стоимость с копейками




# Задача «Сдача всем».

one_kilo_price = 50
num_kilo = 2.7
money = 1500
total_price = one_kilo_price * num_kilo

print('Сдача: ' + str(int(money - (total_price))) + ' рублей')
# на мой взгляд, две однотипные задачи. Разница лишь в названии переменных.
# В первой задаче только черешня, в данной название переменных условно.
# int - так как на выводе по условию целое число




# Задача «Работаем с выводом данных».

name = 'Клубника'
one_kilo_price = 25
num_kilo = 3
total_price = one_kilo_price * num_kilo
money = 2000

print('Чек: ' + name + '-вес-' + str(num_kilo) + ' кг')
print('Цена: ' + str(one_kilo_price) + ' р/кг')
print('Итого: ' + str(total_price) + ' руб')
print('Внесено: ' + str(money) + ' руб')
print('Сдача: ' + str(int(money - (total_price))) + ' рублей')




# Задача «Самая простая задача на свете».

# вариант 1

num_repet = 5

print('Купи конструктор! ' * num_repet)

# вариант 2

num_repet = 5
phrase = 'Купи конструктор! '

print(phrase * num_repet)




# Задача «Автоматизируем простоту!».

num_repet = 5
phrase = '"ФОТОСЪЁМКА"!'

print(('Обожаю писать ' + phrase + ' / ') * num_repet)











