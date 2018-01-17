#Hit Points: 104
#Damage: 8
#Armor: 1

objects = []


w = [[8,4,0],
    [10,5,0],
    [25,6,0],
    [40,7,0],
    [74,8,0],
    ]

a = [
    [13,0,1],
    [31,0,2],
    [53,0,3],
    [75,0,4],
    [102,0,5],
    [0,0,0],
    ]

r = [[25,1,0],
    [50,2,0],
    [100,3,0],
    [20,0,1],
    [40,0,2],
    [80,0,3],
    [0,0,0],
    ]

def inc(a):
    a[-1] +=1
    for i in range(len(a)-1,-1,-1):
        if a[i] >= len(objects[i]):
            if i == 0:
                return None
            a[i] = 0
            a[i-1] += 1
    return a

def win_fight(u_d,u_a):
    u_l = 100
    b_l = 104
    b_d = 8
    b_a = 1

    t_b = (b_l - 1) / max(1,(u_d - b_a))
    t_u = (u_l - 1) / max(1,(b_d - u_a))

    if t_u>=t_b:
        return True
    return False

objects = [w,a,r,r]
v = [0] * len(objects)

v[-1] = -1
cost = None
while True:
    v = inc(v)
    if v ==None:
        break
    u_d = 0
    u_a = 0
    price = 0
    for i in range(len(objects)):
        price += objects[i][v[i]][0]
        u_d += objects[i][v[i]][1]
        u_a += objects[i][v[i]][2]
    if cost != None and price <= cost:
        continue
    if v[-1] == v[-2]:
        continue
    if not win_fight(u_d,u_a):
        cost = price

print cost
