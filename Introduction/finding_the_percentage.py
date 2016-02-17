n = int(raw_input())
d = {}

for x in range(0,n):
    l = raw_input()
    a = l.split()
    f = [float(a[1]),float(a[2]),float(a[3])]
    d[a[0]] = f
    
r = raw_input()
if (r in d):
    print("%.2f" % ((d[r][0] + d[r][1] + d[r][2])/3))
