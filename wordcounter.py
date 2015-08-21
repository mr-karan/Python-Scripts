#Simple word counter

from collections import defaultdict

d=defaultdict(int) # defaultdict(<class 'int'>)

word=input()

# eg word is Mississippi

for letter in word:
    d[letter] +=1

print(list(d.items()))
