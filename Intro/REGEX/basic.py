import re

r=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
num=input()
mo=r.search(num)
breakpoint()
print(mo.group(1))
breakpoint()