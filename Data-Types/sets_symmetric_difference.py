M = raw_input()
s1 = set(list(map(int,raw_input().split())))
N = raw_input()
s2 = set(list(map(int,raw_input().split())))
d1 = s1.difference(s2)
d2 = s2.difference(s1)
s3 = sorted(d1.union(d2))

for s in s3:
    print s
