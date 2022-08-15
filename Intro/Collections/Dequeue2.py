'''collections.deque()
A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same  performance in either direction.

Click on the link to learn more about deque() methods.
Click on the link to learn more about various approaches to working with deques: Deque Recipes.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
import re
d=deque()
for k in range(int(input())):
    i=input()
    
    if re.findall('append\s+',i):
        a,b=i.split(' ')
        
        d.append(b)
    elif 'appendleft' in i:
        a,b=i.split(' ')
        d.appendleft(b)
    elif re.findall(r'^pop$',i):
        d.pop()
    elif re.findall('popleft',i):
        d.popleft()
    
print(' '.join(d))