# melee creep 36.5 gold 57 xp
# ranged creep 47.5 gold 69 xp
# siege creep 65.5 gold 88 xp
# 15:00 all lanes get +1 melee
# 30:00 all lanes get +1 melee
# 35:00 all lanes get +1 siege
# 40:00 all lanes get +1 ranged
# 45:00 all lanes get +1 melee


def time_based_calculation(minute, seconds):
    melee_creep_gold = 36.5
    melee_creep_xp = 57
    ranged_creep_gold = 47.5
    ranged_creep_xp = 69
    siege_creep_gold = 65.5
    siege_creep_xp = 88
    minute = int(minute)
    seconds = int(seconds)
    print(minute)
    print(seconds)
    ## calculations before minute 15
    if minute < 15:
        if seconds < 30:
            gold = minute * (melee_creep_gold * 3 + ranged_creep_gold) + minute // 5 * siege_creep_gold
            xp = minute * (melee_creep_xp * 3 + ranged_creep_xp) + minute // 5 * siege_creep_xp
            print("You gained {} gold and {} xp!".format(gold,xp))
        if seconds >= 30:
            gold = 2 * minute * (melee_creep_gold * 3 + ranged_creep_gold) + minute // 5 * siege_creep_gold
            xp = 2 * minute * (melee_creep_xp * 3 + ranged_creep_xp) + minute // 5 * siege_creep_xp
            print("You gained {} gold and {} xp!".format(gold,xp))
    ## calculations after minute 15 +1melee
    if 15 <= minute < 30:
        if seconds < 30:
            gold = minute * (melee_creep_gold * 4 + ranged_creep_gold) + minute // 5 * siege_creep_gold
            xp = minute * (melee_creep_xp * 4 + ranged_creep_xp) + minute // 5 * siege_creep_xp
            print("You gained {} gold and {} xp!".format(gold,xp))
        if seconds >= 30:
            gold = 2 * minute * (melee_creep_gold * 4 + ranged_creep_gold) + minute // 5 * siege_creep_gold
            xp = 2 * minute * (melee_creep_xp * 4 + ranged_creep_xp) + minute // 5 * siege_creep_xp
            print("You gained {} gold and {} xp!".format(gold,xp))
    ## calculations after minute 30 +1melee
    if 30 <= minute < 35:
        if seconds < 30:
            gold = minute * (melee_creep_gold * 5 + ranged_creep_gold) + minute // 5 * siege_creep_gold
            xp = minute * (melee_creep_xp * 5 + ranged_creep_xp) + minute // 5 * siege_creep_xp
            print("You gained {} gold and {} xp!".format(gold,xp))
        if seconds >= 30:
            gold = 2 * minute * (melee_creep_gold * 5 + ranged_creep_gold) + minute // 5 * siege_creep_gold
            xp = 2 * minute * (melee_creep_xp * 5 + ranged_creep_xp) + minute // 5 * siege_creep_xp
            print("You gained {} gold and {} xp!".format(gold,xp))
    ## calculations after minute 35 +1siege
    if 35 <= minute < 40:
        if seconds < 30:
            gold = minute * (melee_creep_gold * 5 + ranged_creep_gold) + 2 * minute // 5 * siege_creep_gold
            xp = minute * (melee_creep_xp * 5 + ranged_creep_xp) + 2 * minute // 5 * siege_creep_xp
            print("You gained {} gold and {} xp!".format(gold,xp))
        if seconds >= 30:
            gold = 2 * minute * (melee_creep_gold * 5 + ranged_creep_gold) + 2 * minute // 5 * siege_creep_gold
            xp = 2 * minute * (melee_creep_xp * 5 + ranged_creep_xp) + 2 * minute // 5 * siege_creep_xp
            print("You gained {} gold and {} xp!".format(gold,xp))
    ## calculations after minute 40 +1ranged
    if 40 <= minute < 45:
        if seconds < 30:
            gold = minute * (melee_creep_gold * 5 + 2 * ranged_creep_gold) + 2 * minute // 5 * siege_creep_gold
            xp = minute * (melee_creep_xp * 5 + 2 * ranged_creep_xp) + 2 * minute // 5 * siege_creep_xp
            print("You gained {} gold and {} xp!".format(gold,xp))
        if seconds >= 30:
            gold = 2 * minute * (melee_creep_gold * 5 + 2 * ranged_creep_gold) + 2 * minute // 5 * siege_creep_gold
            xp = 2 * minute * (melee_creep_xp * 5 + 2 * ranged_creep_xp) + 2 * minute // 5 * siege_creep_xp
            print("You gained {} gold and {} xp!".format(gold,xp))
    ## calculations after minute 45 +1melee
    if 45 <= minute:
        if seconds < 30:
            gold = minute * (melee_creep_gold * 6 + 2 * ranged_creep_gold) + 2 * minute // 5 * siege_creep_gold
            xp = minute * (melee_creep_xp * 6 + 2 * ranged_creep_xp) + 2 * minute // 5 * siege_creep_xp
            print("You gained {} gold and {} xp!".format(gold,xp))
        if seconds >= 30:
            gold = 2 * minute * (melee_creep_gold * 6 + 2 * ranged_creep_gold) + 2 * minute // 5 * siege_creep_gold
            xp = 2 * minute * (melee_creep_xp * 6 + 2 * ranged_creep_xp) + 2 * minute // 5 * siege_creep_xp
            print("You gained {} gold and {} xp!".format(gold,xp))

print("please enter the current time of the game \nexample: \n15\n30")
time_based_calculation(input(), input())
