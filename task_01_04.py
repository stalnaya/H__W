ax=int(input())
ay=int(input())
bx=int(input())
by=int(input())
cx=int(input())
cy=int(input())

AB=((bx-ax)**2+(by-ay)**2)
AC=((cx-ax)**2+(cy-ay)**2)
BC=((cx-bx)**2+(cy-by)**2)

if AB==(AC+BC) or AC==(AB+BC) or BC==(AB+AC):
    print('yes')
else: print('no')