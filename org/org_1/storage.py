import os.path as Path
import sqlite3


# выделить все в табл.
SQL_SELECT_ALL = 'SELECT * FROM t_org'

# выделить все задачи и статусы
SQL_SELECT_TASK_BY_STATUS = '''
    SELECT task, status 
    FROM t_org  
'''

# выделить все задачи со статусом "N" - завершенные
SQL_SELECT_TASK_BY_STATUS_N = '''
    SELECT task, status 
    FROM t_org
    WHERE status = 'N'
'''

# выделить все задачи со статусом "А" - активные
SQL_SELECT_TASK_BY_STATUS_A = '''
    SELECT task, status 
    FROM t_org
    WHERE status = 'A'
'''

# добавить задачу
SQL_INSERT_TASK = '''
    INSERT INTO t_org (task, status) 
    VALUES (?, 'A')
'''

    
# обновить задачу    
SQL_UPDATE_TASK = '''
    UPDATE t_org 
    SET task =? 
    WHERE task =?
'''    

# изменить статус активной задачи   
SQL_UPDATE_STATUS_A = '''
    UPDATE t_org 
    SET status =? 
    WHERE status ='F'
'''    

# возобновить завершенную задачу   
SQL_UPDATE_STATUS_F = '''
    UPDATE t_org 
    SET status =? 
    WHERE status ='A'
'''    

# удалить задачу    
SQL_DELETE_TASK = '''
    DELETE FROM t_org 
    WHERE task =?
'''    

# удалить все
SQL_DELETE_ALL = '''
      DROP t_org 
   '''

def dict_factory(cursor, row):
    d={}
    for idx, col in enumerate (cursor.description):
        d[col[0]] = row[idx]
    return d
    


def connect(db_name=None):
    """Устанавливает соединениеи с БД"""
    if db_name is None:
        db_name=':memory:'
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn


def initialize(conn, creation_script=None):
    """Инициализирует структуру БД """
    if creation_script is None:
        creation_script=Path.join(Path.dirname(__file__), 'resourses','schema.sql')
    
    with conn, open(creation_script) as f:
        conn.executescript(f.read())
        
        
        
def add_task(conn, task):
    "Добавляет задачу в БД"
    
    if not task: # если адрес получился пустям, нужно выдать исключение - нужна reis (try  - для другого)
        raise RuntimeError('не может быть пустым') # функцию останавливаем raise

    with conn: 
        cursor = conn.execute(SQL_INSERT_TASK, (task,)) # запятая  -картеж с одним значением . без зпт - будет просто значение
        pk=cursor.lastrowid
        conn.execute(SQL_UPDATE_TASK, (task, pk))
    return task
    
        

def find_task(conn, task):
    """Найти задачу"""
    with conn: 
        cursor=conn.execute(SQL_SELECT_ALL, (task,))  
        return cursor.fetchone() 


        
def find_all(conn):
    """Найти все задачи в БД"""
    with conn:
        cursor=conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()
    


        
def find_all_A(conn, task):
    """Найти незавершенные задачи в БД"""
    with conn:
        cursor=conn.execute(SQL_SELECT_TASK_BY_STATUS_A)
        return cursor.fetchall()
    
    
    
def change_A_F(conn):
    """Завершить задачу"""
    with conn:
        cursor=conn.execute(SQL_UPDATE_STATUS_A)
        return cursor.fetchone()   
    
    
def change_F_A(conn):
    """возобновить задачу"""
    with conn:
        cursor=conn.execute(SQL_UPDATE_STATUS_F)
        return cursor.fetchone()  