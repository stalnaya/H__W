import sys 

from org_1 import storage

get_connection = lambda:storage.connect('t_org.sqlite') 


    
# 1   
def action_show_all_A():
    """Выводит текущие задачи"""
    with get_connection() as conn:
        tasks=storage.find_all_A(conn)
    print (tasks)
    
    
# 2   
def action_add():
    """Добавляет задачу"""
    task=input('\nВведите задачу: ')
    
    with get_connection() as conn:
        task = storage.add_task(conn, task)
    print('Задача: {}'.format(task))
 
    
    
    
# 3 
def action_chahge():
    """Изменяет текущую задачу"""
    with get_connection() as conn:
        tasks=storage.find_all(conn)
    print (tasks)
    
#    for task in tasks:
 #       i=input('\nВыбрать задачу: ')
  #      task=tasks.get(i)
   # print (task)



# 4
def action_complete():
    """Завершает задачу"""    
    with get_connection() as conn:
        storage.change_A_F(conn)
    print ('выполнено')
    
    
    
# 5
def action_renew():
    """Возобновляет завершенную задачу"""
    

# m    
def action_show_menu():
    """Отображает меню"""
    print('''
         1. Вывести текущие задачи
         2. Добавить задачу
         3. Изменить задачу
         4. Завершить задачу
         5. Начать задачу снова
         m. Меню
         q. Выйти
''')


# q 
def action_exit():
    """Выход"""
    sys.exit(0) 
 


def main():
    with get_connection() as conn:
        storage.initialize(conn)
  
    actions = {
            '1': action_show_all_A,
            '2': action_add,
            '3': action_chahge,
            '4': action_complete,
            '5': action_renew,
            'm': action_show_menu,
            'q': action_exit,
            }
    action_show_menu()
    
    while 1:
        cmd=input('\nВведите команду:')
        action=actions.get(cmd)
        
        if action:
            try:
                action()
            except Exception as e:
                print (e)
            action()
        else:
            print('Не известная команда')
     

