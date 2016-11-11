# The homework solution:
string = "helloworld"
'''
1. Insert a space between the 'hello' and 'world' to create a new string "hello world"
* Why this answer is wrong?
tolist = list(string)  # good! You already know the string is not mutable, so you change the string to list firstly.
newlist = tolist.insert(5, ' ')  # This caused the problem, because list.insert() 
''.join(newlist)
'''
tolist = list(string)
tolist              # ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
newlist = toList.insert(5, ' ')
type(newlist)       # <class 'NoneType'>
tolist.insert(5, " ")
tolist              #['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
''.join(tolist)     #'hello world'
# Another way is using the python index slicing
>>> ind = string.find('world')
>>> ind
# 5
>>> newstring = string[ :ind] + ' ' + string[ind: ]
>>> newstring
# 'hello world'
'''
2. Capitalize the 'h' and 'w' in the new string
'''
>>> newstring.title()
# 'Hello World'
'''
3. reverse the new string into 'dlrow olleh'
'''
>>> newstring[:: -1]  # This does not change newstring 
# 'dlrow olleh'
>>> newstring
# 'hello world'
# Another way to reverse the string
>>> reversed(newstring)  # This changed the newstring
# <reversed object at 0x10210df28>
>>> newstring
# 'hello world'
# difference: list.reverse() VS. reversed(string)
