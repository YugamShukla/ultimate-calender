a=int(input('enter date\n'))
b=int(input('enter month\n'))
y=int(input('enter year\n'))
c1=int(y/100)
c=int(c1*100)
l=int(y-c)
k=int(c/100)
m=int(k%4)
if m==int(0):
    i=int(0)
if m==int(1):
    i=int(5)
if m==int(2):
    i=int(3)
if m==int(3):
    i=int(1)
d=int(l-1)
q=int(d/4)
z=int(d-q)
w=int((z*1)+(q*2))
if b==int(1):
    x=int(0)
if b==int(2):
    x=int(31)
if b==int(3):
    x=int(59)
if b==int(4):
    x=int(90)
if b==int(5):
    x=int(120)
if b==int(6):
    x=int(151)
if b==int(7):
    x=int(181)
if b==int(8):
    x=int(212)
if b==int(9):
    x=int(243)
if b==int(10):
    x=int(273)
if b==int(11):
    x=int(304)
if b==int(12):
    x=int(334)
f=int(a+x)
total=(i+w+f)
u=int(y%4)
if u==int(0):
    total=int(total+1)
    day=int(total%7)
    if day==0:
        print('sunday')
    if day==int(1):
        print('monday')
    if day==int(2):
        print('tuesday')
    if day==int(3):
        print('wednesday')
    if day==int(4):
        print('thursday')
    if day==int(5):
        print('friday')
    if day==int(6):
        print('saturday')
else:
    total==int(i+w+f)
    day=int(total%7)
    if day==0:
        print('sunday')
    if day==int(1):
        print('monday')
    if day==int(2):
        print('tuesday')
    if day==int(3):
        print('wednesday')
    if day==int(4):
        print('thursday')
    if day==int(5):
        print('friday')
    if day==int(6):
        print('saturday')

  


