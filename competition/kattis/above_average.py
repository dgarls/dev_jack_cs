tests = int(input())
for test in range(tests):
    i = input().split()
    num_students = int(i[0])
    grades = []
    
    for student in range(1, num_students + 1):
        grades.append(int(i[student]))
    
    total_score = sum(grades)
    avg = total_score / num_students
    num_above = 0
    for grade in grades:
        if grade > avg:
            num_above += 1
    
    print(f"{(num_above / num_students * 100):.3f}%")