submitted = {int(input()) for _ in range(28)}
all_students = set(range(1, 31))

not_submitted = all_students - submitted
print(min(not_submitted))
print(max(not_submitted))
