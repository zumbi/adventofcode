import sys
import datetime

def get_day(a):
    return a.strftime("%m%d")

def date_dt(a):
    a = a.split('] ')
    dt = datetime.datetime.strptime(a[0][6:], "%m-%d %H:%M")
    data = a[1].split()
    if data[0] == "Guard":
        if dt.hour == 23:
            dt += datetime.timedelta(days=1)
    return dt

#Sort lines
lines = sys.stdin.readlines()
lines = sorted(lines, key=date_dt)


#Find dates
dates = set()
for l in lines:
    dt = date_dt(l)
    dates.add(get_day((date_dt(l))))

#Create table
table=dict()
for d in dates:
    table[d] = 60 * [0] + [0]

#Fill table
for l in lines:
    dt = date_dt(l)
    data = l.split('] ')[1]
    data = data.split()
    if data[0] == "Guard":
        table[get_day(dt)][60] = int(data[1][1:])
        continue
    if data[0] == "wakes":
        for i in range(dt.minute,60):
            table[get_day(dt)][i] = 0
        continue
    if data[0] == "falls":
        for i in range(dt.minute,60):
            table[get_day(dt)][i] = 1

#sum data
work_time = dict()
for t in table:
    if table[t][60] not in work_time:
        work_time[table[t][60]] = [0] * 60
    for i in range(60):
        work_time[table[t][60]][i] += table[t][i]

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

