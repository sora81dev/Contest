import collections
import itertools

s=list(input())
counter = collections.Counter(s)

mode_v = counter.most_common()[0][-1]
it = itertools.takewhile(
    lambda kv: kv[-1] == mode_v, counter.most_common()
)

t = list((k for k, v in it))

t.sort()
print(t[0])