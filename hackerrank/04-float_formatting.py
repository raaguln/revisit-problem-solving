n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
marks = student_marks.get(query_name)
sum = 0
for score in marks:
    sum += score
print("{0:.2f}".format(sum / len(marks)))
# OR
# print(f"{sum / len(marks):.2f}")