import numpy as np

def new_predict(number:int=1) -> int:
    """Угадываем число посредством сжатия интервала в 2 раза после каждой попытки

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    b1 = 1     # нижняя граница интервала (>=)
    b2 = 101   # верхняя граница интервала (<)
    
    predict_number = b1 + (b2 - b1) // 2  # середина интервала

    while True:
        count += 1
        # predict_number = np.random.randint(1, 101) # предполагаемое число
        
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number < predict_number:
            b2 = predict_number
        else:
            b1 = predict_number
        
        predict_number = b1 + (b2 - b1) // 2
    
    #print('Число:', number, '  Кол-во попыток:', count)
    return(count)

#print(f'Количество попыток: {random_predict()}')

def score_game(f_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        f_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # 1000 !!! загадали список чисел

    for number in random_array:
        count_ls.append(f_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(new_predict)
    