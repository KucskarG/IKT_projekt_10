def gyertyak (x):
    if x==1:
        print(r"""
          1     
        11111 
        1   1 
        1   1 
        11111  
        """)
    elif x==2:
        print(r"""
          1     1      
        11111 11111  
        1   1 1   1  
        1   1 1   1 
        11111 11111 
        """)
    elif x==3:
        print(r"""
          1     1     1    
        11111 11111 11111 
        1   1 1   1 1   1  
        1   1 1   1 1   1 
        11111 11111 11111
        """)
    elif x==4:
        print(r"""
          1     1     1     1
        11111 11111 11111 11111
        1   1 1   1 1   1 1   1 
        1   1 1   1 1   1 1   1
        11111 11111 11111 11111
        """)


nap = int (input("December hanyadika van: "))
if nap>24:
    print("Már karácsony elmult")
print (24-nap , " nap van még karácsonyig")
print(r"""Az eddig meggyújtott gyertyáid """)
fa =  (input("Nyomj egy enter a tovább lépéshez"))
if nap<=5:
    gyertyak(1)
elif nap<=12:
    gyertyak(2)
elif nap<=19:
    gyertyak(3)
elif nap<=25:
    gyertyak(4)
else:
    print("CSAK 4 GYERTYA LEHET")
#nézze el ha a számok nem stimmelnek nemtudom mikor kell uj gyertyát gyujtani de működik és értem a kódot

