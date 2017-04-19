
# How many words in aesop?
with open("aesop.txt") as aesopfile:
    aeaesoptext=aesopfile.read()  ## if use with, we do not need to close the file by aesopfile.close()
    aesoptowords=aesoptext.split()  #split with no arguments splits on whitespace
    print len(aesopwords)

# Or you can use with syntax and the closing will be automatically done
  
# How many times that "wolf" appears in aesop?
lowcase= [word.lower() for word in aesopwords]
lowcase.count("wolf")

# How many times each unique word apears respectively?
uniquelowcase= set(lowcase)
uniquedict= {}
for k in uniquelowcase:
  uniquedict[k]= lowcase.count(k)
  
# What is the top 10 most-used words?
# Hint: sort by the frequency of the words, in desceding order.
top= sorted(uniquedict.iteritems(), key= lambda (k,v): v, reverse= True)[:10]    # items are (k,v) pairs.
top  # top is a list now

# Plot a bar chart for the ranking of top 10 most-used words
import numpy as np
import matplotlib.pyplot as plt 
x= np.arrange(len(top))
plt.bar(x, [e[1] for e in top]);  # each element of list top is a pair of ("word", number).
x.ticks(x+0.4, [e[0] for e in top])




