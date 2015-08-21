#Simple word counter

from collections import defaultdict

d=defaultdict(list) # defaultdict(<class 'list'>)

word=input()

# eg word is Mississippi

for k in word:
    d[k] +=1

print(d.items())
