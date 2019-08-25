def funv(samv):
    first = second = 984561
    cnt = 0
    for i in range(len(samv)):
        if samv[i][1] < first:
            second = first
            first = samv[i][1]
        elif samv[i][1] < second and samv[i][1] != first:
            second = samv[i][1]
            index = i

    for j in range(len(samv)):
        cnt += samv[j].count(samv[index][1])

    if cnt > 1:
        for k in range(len(samv)):
            if samv[k][1] == samv[index][1]:
                print(samv[k][0])
    else:
        print(samv[index][0])


if __name__ == '__main__':
    arrv = []
    for i in range(int(input())):
        arrv.append([])
        name = input()
        score = float(input())
        arrv[i].append(name)
        arrv[i].append(score)
    funv(arrv)

