#THIS IS A ROT 13 ALGORITHM made with ❤ BY Mr. ANIKET KOLTE popularly known as R'xa3DAR
s=input(":- ENTER THE STRING TO BE ENCRYPTED BY ROT 13 :- ")
c=''
for i in s:
    if i.isupper(): 
        if(ord(i)+13<90):
            d=ord(i)+13
            c=chr(d)
        elif(ord(i)+13>90):
            c=chr((ord(i)+13)-90+(64))
    elif i.islower():
        if(ord(i)+13<122):
            d=ord(i)+13
            c=chr(d)
        elif(ord(i)+13>122):
            c=chr((ord(i)+13)-122+(96))

    print(c)
       

"""
l=[]
n=int(input(""))

for i in range(n):
    
    x,y,z = input("").split()
    
    if(x=="insert"):
        a=int(y)
        b=int(z)
        l.insert(a,b)
    elif(x=="print"):
        a=""
        b=""
        print(l)
    elif(x=="remove"):
        a=int(y)
        l.remove(a)
    elif(x=="append"):
        a=int(y)
        l.append(a)
    elif(x=="sort"):
        l.sort()
    elif(x=="reverse"):
        l.reverse()
    elif(x=="pop"):
        l.pop()
    
"""



     