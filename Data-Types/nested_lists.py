N = int(raw_input())

students = [[raw_input(), float(raw_input())] for _ in range(N)]

second_highest = sorted(list(set([marks for name,marks in students])))[1]

print('\n'.join([name for name,marks in sorted(students) if marks == second_highest]))
