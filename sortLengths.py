fi=open("twl06.txt",'r')

words=[[],[],[],[],[],[],[]]
while True:
	lino=fi.readline()
	if len(lino)==0:
		break;
	if (len(lino)==3):
		words[0].append(lino[0:2])
	if len(lino)==4:
		words[1].append(lino[0:3])
       
	if len(lino)==5:
		words[2].append(lino[0:4])
	if len(lino)==6:
		words[3].append(lino[0:5])
	if len(lino)==7:
		words[4].append(lino[0:6])
	if len(lino)==8:
		words[5].append(lino[0:7])
	if len(lino)==9:
		words[6].append(lino[0:8])

fi.close()

for whichList in range(2,9):
	filename="words"+str(whichList)+".txt"
	fi=open(filename,'w')
	for word in words[whichList-2]:
		fi.write(word+"\n")
	fi.close()
