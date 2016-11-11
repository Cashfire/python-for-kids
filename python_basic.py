# The homework solution:
string = "helloworld"
>>> l = list(string)  
>>> l    # ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
# notice: list() does not convert the string to a list ["hello", "world"]

'''
# 1. convert the string to list ["hello", "world"]
'''
>>> tolist = string[:5] + ' ' + string[5:]
>>> tolist  #'hello world'
>>> newlist = tolist.split()
>>> newlist
# ['hello', 'world']

'''
2. find the index of 'l' in the 'world' of the whole string/ list.
'''
# string.find()
>>> ind = string.find('ld')  
>>> ind  # 8
# list.index() 
>>> i = l.index('l')
>>> i  # 2

#2, insert a space to between the 'hello' and 'world' to "hello world"
'''
Homework Question: Change the string "helloworld" to string "hello world"
* Why this answer is wrong?
tolist = list(string)  # good! You already know the string is not mutable, so you change the string to list firstly.
newlist = tolist.insert(5, ' ')  # This caused the problem, because list.insert() 
''.join(newlist)
'''
# string is immutable, but we can create a new string with a space.
>>> ind = string.find('world')
>>> ind   # 5
>>> newstring = string[ :ind] + ' ' + string[ind: ]
>>> newstring   # 'hello world'

# insert in the list, and then join
tolist = list(string)
tolist              # ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
newlist = toList.insert(5, ' ')
type(newlist)       # <class 'NoneType'>
tolist.insert(5, " ")
tolist              #['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
''.join(tolist)     #'hello world'

'''
2. Capitalize the 'h' and 'w' in the new string
'''
>>> newstring.title()
# 'Hello World'
# notice: str.capitalize() just capitalize the 1st word
>>> newstring.capitalize() #'Hello world'
# How to title the list newlist ['hello', 'world'] to ['Hello', 'World']?
>>> map(lambda str : str.title() , newlist) # This works in Python 2.7
# <map object at 0x10217d0f0>   shows in Python 3.5
>>> list(map(lambda str : str.title() , newlist))  # Python 3.5 requires us to convert the map object to list
# ['Hello', 'World']
'''
3. reverse the string newstring 'hello world' to 'dlrow olleh'.
'''
>>> newstring[:: -1]  # This will not change the original string.
# 'dlrow olleh'
>>> newstring
# 'hello world'
'''
4. reverse the list newlist ['hello', 'world'] to ['world', 'hello'].
'''
>>> newlist.reverse() # This will change the list
>>> newlist #['world', 'hello']
'''
Notice difference: list.reverse() VS. reversed(string)
'''
>>> reversed(newstring)
# <reversed object at 0x10210db00>
>>> list(reversed(newstring))
['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
>>> newstring
'hello world'
