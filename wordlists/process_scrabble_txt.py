import funcy 
fi = open("scrabble_dict.txt",'r')
contents = fi.read().lower().strip().split("\n")
fi.close()
grouped_by_length = funcy.group_by(len,contents)
for i in range(1,9):
    outfilename = "scrabble_words_%d.txt" % i
    outfile = open(outfilename,'w')
    for word in grouped_by_length[i]:
        outfile.write(word+"\n")
    outfile.close()

