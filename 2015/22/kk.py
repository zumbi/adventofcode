import copy
#mana hit armor heal manap length


spells = [[53,4,0,0,0,0],
            [73,2,0,2,0,0],
            [113,0,7,0,0,6],
            [173,3,0,0,0,6],
            [229,0,0,0,101,5]]

points_user = 50
mana = 500

points_boss = 55
damage_boss = 8
effects = []

min_mana = None
sum_mana = 0
armor_user = 0

state = [effects, mana, sum_mana, points_user, points_boss, armor_user]
wq = [state]

def apply_effects(state):
    [effects, mana, sum_mana, points_user, points_boss, armor_user] = state

    armor_user2 = 0
    effects2 = []
    for i in range(len(effects)):
        spell = spells[effects[i][0]]
        points_boss -= spell[1]
        armor_user2 += spell[2]
        mana += spell[4]
        if effects[i][1] == 1:
            continue
        effects2 += [[effects[i][0],effects[i][1]-1]]

    return [effects2, mana, sum_mana, points_user, points_boss, armor_user2]

min_points_boss = points_boss
while len(wq) > 0:
    state = wq[0]
    wq = wq[1:]

    [effects, mana, sum_mana, points_user, points_boss, armor_user] = state
    if min_mana and sum_mana > min_mana:
        continue

    if points_boss < min_points_boss:
        min_points_boss = points_boss
        print min_points_boss

    #user
    points_user -= 1
    if points_user <=0:
        continue
    state = [effects, mana, sum_mana, points_user, points_boss, armor_user]
    #effect
    state = apply_effects(state)
    [effects, mana, sum_mana, points_user, points_boss, armor_user] = state
    if points_boss <= 0:
        if min_mana == None or sum_mana < min_mana:
            min_mana = sum_mana
            print min_mana

    todo = []
    for i in range(len(spells)):
        if mana < spells[i][0]:
            continue
        already_effect = False
        for e in effects:
            if i == e[0]:
                already_effect = True
                break
        if already_effect:
            continue
        s2 = copy.deepcopy(state)
        [effects2, mana2, sum_mana2, points_user2, points_boss2, armor_user2] = s2
        mana2 -= spells[i][0]
        sum_mana2 += spells[i][0]
        if spells[i][-1] >0:
            effects2 += [[i,spells[i][-1]]]
            s2 = [effects2, mana2, sum_mana2, points_user2, points_boss2, armor_user2]
            todo += [s2]
            continue
        points_boss2 -= spells[i][1]
        points_user2 += spells[i][3]

        if points_boss2 <=0:
            if min_mana == None or sum_mana2 < min_mana:
                min_mana = sum_mana2
                print min_mana
            continue

        s2 = [effects2, mana2, sum_mana2, points_user2, points_boss2, armor_user2]
        todo += [s2]

    #boss
    while len(todo) >0:
        state2 = todo[0]
        todo = todo[1:]
        state2 = apply_effects(state2)
        [effects2, mana2, sum_mana2, points_user2, points_boss2,armor_user2] = state2
        if points_boss2 <= 0:
            if min_mana == None or sum_mana2 < min_mana:
                min_mana = sum_mana2
                print min_mana
        #attack
        points_user2 -= max(1,damage_boss - armor_user2)
        if points_user2 <=0:
            continue
        state2 = [effects2, mana2, sum_mana2, points_user2, points_boss2, armor_user2]
        wq += [state2]

print min_mana

#1382 too high
#1362 too high
#1295 too high
#1309 is worng
