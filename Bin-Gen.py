import random
for i in range (int(input('count of cards : '))):
 g=(input('BIN : ' ))+str(''.join(random.choice(['1','2','3','4','5','6','7','8','9','0'])for i in range((10))))+'|'+str(''.join(random.choice(['01','02','03','04','05','06','07','08','09','10','11','12'])for i in range((1))))+'|20'+str(''.join(random.choice(['2','3'])for i in range((1))))+str(''.join(random.choice(['3','4','5','6','7','8','9'])for i in range((1))))+'|'+str(''.join(random.choice(['1','2','3','4','5','6','7','8','9','0'])for i in range((3))))
 print(g)
