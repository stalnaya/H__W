def bubble_sort(lst):
    for i in range(1, len(lst)): # цикл - просматривает все эл-ты списка от 1-го до последнего
        for j in range(i):# сравнение эл-тов на местах i и j.
            if lst[i] < lst[j]: # Если элемент i  меньше j
                lst[j], lst[i] = lst[i], lst[j] # поменять местами 
    return lst
