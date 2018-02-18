def dec2bin(number):
    c=''
    while number > 0:
        y = str(number % 2)
        c = c + y
        number = int(number / 2)
    return c[::-1]


    
def dec2oct(number):
    c=''
    while number > 0:
        y = str(number % 8)
        c = c + y
        number = int(number / 8)
    return c[::-1]



def dec2hex(number):   
    D = {
         0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
         10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'
         }
    q=0
    q = number
    result = ""
    while q != 0:
        r = q % 16
        q = q // 16
        result += D[r]
    result = ''.join(reversed(result))
    return result



def bin2dec(number):
    c=0
    for i in range (0, len(number)):
        c=c+int(number[i])*(2**(len(number)-i-1))
    return c   



def oct2dec(number):
    c=0
    for i in range (0, len(number)):
        c=c+int(number[i])*(8**(len(number)-i-1))
    return c   

   


def hex2dec(number):
    D = {
          '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
         'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15
         }
    a=[]
    for i, val in enumerate(reversed(number)):
        a.append(D[val]*16**(i))
    return sum(a)
   