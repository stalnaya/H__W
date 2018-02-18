from time import sleep 

def pause(sec):
    def dec(func):
        def wrapper(*args, **kwargs):
           sleep(sec)
           return func()
        return wrapper 
    return dec
 
    
#@pause(2) 
#def func(): 
    #print('Функция выполняется с задержкой 2 секунды!') 
#func() 