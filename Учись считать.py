import random

lowDiapozon = 10 # нижняя граница чисел
highDiapozon = 100 # верхняя граница чисел
sign = 0 # Знак операции
playGame = True # главный цикл
count = 0 #Ксоличество решоных примеров
right = 0 #Правильные ответы
score = 0 #Очки

while (playGame):
    
    print(f'Всего примеров: {count}')
    print(f'Правильные ответы: {right}')
    print(f'Очки: {score}')
    print('*' * 20)
    

    sign = random.randint(0, 3)

#++++++++++++++++++++++++++++++++++

    if (sign == 0):

        z = random.randint(lowDiapozon, highDiapozon)
        x = random.randint(lowDiapozon, z)
        
        y = z - x

        if (random.randint(0, 1) == 0):
            print(f'{x} + {y} = ?')
        else:
            print(f'{y} + {x} = ?')

#----------------------------------

    elif  (sign == 1):

        x = random.randint(lowDiapozon, highDiapozon)
        y = random.randint(0, x)
        
        z = x - y

        print(f'{x} - {y} = ?')
        
#***********************************

    elif (sign == 2):

        x = random.randint(lowDiapozon, highDiapozon)
        y = random.randint(0, highDiapozon)

        z = x * y

        if (random.randint(0, 1) == 0):
            print(f'{x} * {y} = ?')
        else:
            print(f'{y} * {x} = ?')

#//////////////////////////////////////
    else:
        
        x = random.randint(1, (highDiapozon - lowDiapozon) // 10 + 1)
        y = random.randint(lowDiapozon, highDiapozon) // x

        if (y == 0):
            y = 1

        x *= y
        z = x // y

        print(f'{x} * {y} = ?')

    print(f'Чит: {z}')

    user = ''

    while (not user.isdigit()
           and user.upper() != 'STOP'
           and user.upper() != 'S'
           and user.upper() != 'Ы'
           and user.upper() != 'ЫЕЩЗ'):

        user = input('Введите ответ:')
            
        if (user.upper() == 'HELP'
                or user.upper() == 'H'
                or user == '?'
                or user.upper() == 'Р'
                or user.upper() == 'РУДЗ'):
            
            if (z > 9):
                print(f'Число оканчивается на: {z % 10}')
            else:
                print(f'Число однозначное!')

            score -= 10
            
        elif (user.upper() == 'STOP'
                or user.upper() == 'S'
                or user.upper() == 'Ы'
                or user.upper() == 'ЫЕЩЗ'):

            playGame = False

        else:
            count += 1
            if (int(user) == z):
                print('\nПравильно!\n')
                score += 20
                right += 1
            else:
                score -= 10
                print(f'Неправельный ответ! Правильный {z}')
                print(f'Вы можете получить подсказку за -10 очков, написав HELP  или ?')

print('*' * 20)
print(f'Всего примеров: {count}')
print(f'Правильные ответы: {right}')
print(f'Очки: {score}')
print(f'Количество неправельных ответов: {count - right}')
                
