'''
3. Feladat
Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
- csak 3-mal osztható,
- csak 4-gyel osztható,
- 3-mal és 4-gyel is osztható,
- sem 3-mal, sem 4-gyel nem osztható!
'''
szám = int(input('Adj meg egy számot! '))

osztás3 = szám % 3
osztás4 = szám % 4
osztás = szám % 12

if osztás < 0.1 :
  print ('3-mal és 4-gyel is osztható')

elif osztás3 < 0.1 :
  print ('csak 3-mal osztható')
elif osztás4 < 0.1 :
  print ('csak 4-gyel osztható')

else :
  print ('sem 3-mal, sem 4-gyel nem osztható!')