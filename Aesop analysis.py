
# How many lines in aesop?
aesopfile=open("aesop.txt")
aesoptext=aesopfile.read()
aesopfile.close()
aesoptolines=aesoptext.split()  #split with no arguments splits on whitespace
len(aesoplines)
