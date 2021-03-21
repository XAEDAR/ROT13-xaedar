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
       
