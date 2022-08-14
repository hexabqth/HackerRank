from itertools import combinations as combo
n=int(input())
lst=list(map(str,input().split()))
k=int(input())
combination=list(combo(lst,k))
print(str(len([_ for _ in combination if 'a' in _])/len(combination)),'.2f')