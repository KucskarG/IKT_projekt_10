for x in range(0,1001):
    print(x)


szo1 = input('első')
szo2 = input('második')
szo1h = len(szo1)
szo2h = len(szo2)

if szo1h > szo2h:
	print('Az első nagyobb')

elif szo1h==szo2h :
    print('Egyenlő')
    
else:
  	print('A másik a nagyobb')