import sys

def date_num(a):
    a = a.split('] ')
    a = a[0]
    a = a.replace(" ","")
    a = a.replace("[","")
    a = a.replace(":","")
    a = a.replace("-","")
    return int(a)

#Sort lines
lines = sys.stdin.readlines()
lines = sorted(lines, key=date_num)

work_time = dict()
guard = 0

#Fill table
for l in lines:
    data = l.split('] ')[1]
    data = data.split()
    if data[0] == "Guard":
        guard = int(data[1][1:])
        if guard not in work_time:
            work_time[guard] = [0] * 60
        continue
    minute = date_num(l) % 100
    if data[0] == "wakes":
        for i in range(minute,60):
            work_time[guard][i] -= 1 
        continue
    if data[0] == "falls":
        for i in range(minute,60):
            work_time[guard][i] += 1
        continue

#Step 1
#sum_data
worker = dict()
for w in work_time:
    worker[w] = sum(work_time[w])

lacy = max(worker, key=worker.get)
best_min = work_time[lacy].index(max(work_time[lacy]))
print(lacy * best_min)

#Step 2
#max_data
worker = dict()
for w in work_time:
    worker[w] = max(work_time[w])

lacy = max(worker, key=worker.get)
best_min = work_time[lacy].index(max(work_time[lacy]))
print(lacy * best_min)

