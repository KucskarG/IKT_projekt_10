nyit = int (input('Irj be egy kerek egész számot mikor szeretnél elmenni a boltba: '))
if 8 <= nyit <= 16 :
    	print ('Még nyitva van a bolt ennyi óráig')	
        print (16-nyit, 'óráig még nyitva van')
elif 8 > nyit :
        print('Már zárva van')
        print(8-nyit, 'óra van még')




else:
    print('Zárva')
    if nyit > 16:
        print(32-nyit, 'óra mulva lesz nyitva')
        else:
            print(8-nyit, 'óra mulva lesz nyitva')
            
    
 


