>>> sorted(ns, key = lambda x: x.lower())
['alex', 'Chris', 'fred', 'Heather', 'judy', 'Sam']
>>> ns
['Chris', 'Heather', 'Sam', 'alex', 'fred', 'judy']
>>> ns.sort(key = lambda x: x.lower())
>>> ns
['alex', 'Chris', 'fred', 'Heather', 'judy', 'Sam']
