'''
sort
'''
# sorted without regard to case
>>> sorted(ns, key = lambda x: x.lower())
#['alex', 'Chris', 'fred', 'Heather', 'judy', 'Sam']
>>> ns
#['Chris', 'Heather', 'Sam', 'alex', 'fred', 'judy']
>>> ns.sort(key = lambda x: x.lower())
>>> ns
#['alex', 'Chris', 'fred', 'Heather', 'judy', 'Sam']
'''
Tuples are immutable, we cannot use append method as for lists; 
we can concatenate the new value at the end of the original tuple 
and reassign its value back to that tuple.
'''
>>> tupl = tuple(ns)
>>> tuple
<class 'tuple'>
>>> tupl
('alex', 'Chris', 'fred', 'Heather', 'judy', 'Sam')
>>> tupl += ('Bob',)
>>> tupl
('alex', 'Chris', 'fred', 'Heather', 'judy', 'Sam', 'Bob')
# create a new tuple names without 'Bob'
>>> names = tupl[:-1]  # we cannot use del or pop as list
>>> names     #('alex', 'Chris', 'fred', 'Heather', 'judy', 'Sam')
# We want to capitalize each name. (map does not change the original list)
>>> names = list(map(lambda x : x.title() , names))
>>> names
# ['Alex', 'Chris', 'Fred', 'Heather', 'Judy', 'Sam']
'''
Dictionary
'''
>>> dic = {'Alex': 23, 'Chris': 31, 'Fred': 28, 'Heather': 40, 'Judy': 35, 'Sam': 19}
>>> dic
#{'Fred': 28, 'Alex': 23, 'Judy': 35, 'Sam': 19, 'Chris': 31, 'Heather': 40} Notice the order
>>> dic.keys()
# dict_keys(['Fred', 'Alex', 'Judy', 'Sam', 'Chris', 'Heather'])
>>> ages = dic.values()
>>> ages
# dict_values([28, 23, 35, 19, 31, 40])
>>> dic.get("Fred")
#28
>>> 'Alex' in dic
# True
>>> 28 in dic
# False
>>> 28 in dic.values()
# True
