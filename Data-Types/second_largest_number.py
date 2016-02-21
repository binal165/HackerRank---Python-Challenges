input1 = int(raw_input())
input2 = list(map(int,raw_input().strip().split()))[:input1]
z = max(input2)
while max(input2) == z:
    input2.remove(max(input2))

print max(input2)