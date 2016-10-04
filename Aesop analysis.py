

aesopfile=open("aesop.txt")
aesoptext=aesopfile.read()
aesopfile.close()
aesoptokens=aesoptext.split()  #split with no arguments splits on whitespace
len(aesoptokens)
