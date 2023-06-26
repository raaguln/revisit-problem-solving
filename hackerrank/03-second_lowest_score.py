# Final solution
records = []
low = [["",99]]
second_low = [["", 100]]
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    if score < low[0][1]:
        second_low = low
        low = [[name, score]]
    elif score == low[0][1]:
        low.append([name, score])
    else:
        if score < second_low[0][1]:
            second_low = [[name, score]]
        elif score == second_low[0][1]:
            second_low.append([name, score])
sorted_sec_low = sorted(second_low, key=lambda x: x[0])
for name, _ in sorted_sec_low:
    print(name)

# -----------------------------------------------------
# Input array
n = int(input())
records = []
for _ in range(n):
    name = input()
    score = float(input())
    records.append([name, score])

# Memory efficient method (n is not stored)
for _ in range(int(input())):
    name = input()
    score = float(input())