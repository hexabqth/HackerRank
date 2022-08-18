from collections import defaultdict
from collections import namedtuple


step=namedtuple('ok','ret')
d=defaultdict(step)
step1=step(ok=1,ret='whooo')
#d['step1']=step1
print(d)
