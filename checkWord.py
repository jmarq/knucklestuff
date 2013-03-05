words=[]
wordLists=[[],[],{},{},{},{},{},{}]

def scrambleWord(word):
    a1=word[0]+word[4]+word[1]+word[5]
    a2=word[2]+word[6]+word[3]+word[7]
    biga=a1+a2
    b1=word[4]+word[0]+word[5]+word[1]
    b2=word[6]+word[2]+word[7]+word[3]
    bigb=b1+b2
    return([biga,bigb])

def checkWord(word):
    length=len(word)
    index=length-1
    if index==1 or index==0:
        if word in wordLists[index]:
            return True
        else:
            return False
    else:
        if word[0:2] in wordLists[index]:
            if word in wordLists[index][word[0:2]]:
                return True
            else:
                return False
        else:
            return False
    

def checkWords(wordPair):
    if checkWord(wordPair[0]) and checkWord(wordPair[1]):
        
        return True;
    
def checkTat(tat):
    scrambles=scrambleWord(tat); 
    for scramble in scrambles:
        for i in range(0, 5):
            if i==0:
                #check if the scrambles are in the 8 letter word list
                if checkWord(scramble):
                    
                    return True;
            elif i==4:
                w41=scramble[0:4]
                w42=scramble[4:8]
                if(checkWords([w41,w42])):
                    
                    return True;
            else:
                small=i;
                big=8-i;
                ws1=scramble[0:small];
                ws2=scramble[8-small:8];
                wb1=scramble[small:8];
                wb2=scramble[0:8-small];
                if(checkWords([ws1,wb1])):
                    
                    return True;
                if(checkWords([ws2,wb2])):
                    
                    return True;
                
            
                    
                
                
            
        




for i in range(1,9):
    filename='words'+str(i)+".txt"
    fi=open(filename,'r')
    filewords=fi.read().split()
    fi.close()
    words.append(filewords)
   

for i in range(0,8):
    for word in words[i]:
        if(i==0) or (i==1):
            wordLists[i].append(word)
        else:
            if word[0:2] not in wordLists[i]:
                wordLists[i][word[0:2]]=[word]
            else:
                wordLists[i][word[0:2]].append(word)
            
    
    
coolScrambles=[]
outfile="fourByfours.txt"
i=0
for word in words[3]:
    
    for word2 in words[3]:
        i+=1
        if i%50000==0:
            print i;
        tat1=word+word2
        tat2=word2+word
        if checkTat(tat1):
            coolScrambles.append(tat1)
        if checkTat(tat2):
            coolScrambles.append(tat2)

tatsAndScrambles=[]
for tat in coolScrambles:
    tatsAndScrambles.append([tat,scrambleWord(tat)])
fi=open(outfile,'w')
for combo in tatsAndScrambles:
    fi.write(str(combo)+"\n")
fi.close()
        
        
        
            
    
    

    


