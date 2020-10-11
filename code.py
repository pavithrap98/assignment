import random

count=-1                                            #to get count of line number
l=list()
fr = open("sample_input.txt", "r")
fw = open("sample_output.txt", "a")

first_line=fr.readline()
fw.write(first_line)                                #printingg the 1st line to a file
fw.write("Here the goodies that are selected for distribution are:\n\n")
words=first_line.split(":")
n=int(words[1])                                      #read no. of employes
        
randomlist = random.sample(range(3, 12), n)         #random number as line numbers

for line in fr:
    count=count+1
    if count in randomlist:
        words=line.split(":")
        number=int(words[1])
        l.append(number)                            #adding the list of all prices to a list
        fw.write(line)
        print(line)
    else:
        continue

max_price=max(l)                                    #finding the maximum value in the list of prices
min_price=min(l)                                    #finding the minimum value in the list of prices


difference=max_price-min_price

fw.write("\n\n")
fw.write('And the difference between the chosen goodie with highest price and the lowest price is %d'%difference)
fw.write("\n\n")
fr.close()
fw.close()