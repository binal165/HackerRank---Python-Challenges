inp1 = raw_input()
inp2 = raw_input().split(" ")

print inp1[:int(inp2[0])] + inp2[1] + inp1[(int(inp2[0]) + 1):]