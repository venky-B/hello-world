if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    total = per_v = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for j in range(len(student_marks[query_name])):
        total += student_marks[query_name][j]
        per_v = total/len(student_marks[query_name])

    print(per_v)

