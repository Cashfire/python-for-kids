# The homework solution:
string = "helloworld"
###
1. capitalized the H and W in the string "hello world"
* Why this answer is wrong?
tolist = list(string)  # good! You already know the string is not mutable, so you change the string to list firstly.
newlist = tolist.insert(5, ' ')  # This caused the problem, because list.insert() 
''.join(newlist)
###
tolist = list(string)
tolist
['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
newlist = toList.insert(5, ' ')
type(newlist)  # <class 'NoneType'>
tolist.insert(5, " ")
tolist
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
''.join(tolist)
'hello world'
