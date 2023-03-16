people = int(input())

marble = {
    'meals': 19,
    'munch': 200
}

marble_plus = {
    'meals': 19,
    'munch': 350
}

quartz = {
    'meals': 14,
    'munch': 200
}

quartz_plus = {
    'meals': 14,
    'munch': 350
}

for p in range(people):
    person = input().split()
    if person[1] == "Marble+":
        plan = marble_plus
    elif person[1] == "Marble":
        plan = marble
    elif person[1] == "Quartz":
        plan = quartz
    else:
        plan = quartz_plus
    swipes_left = plan.get("meals") - int(person[2])
    money_left = round(plan.get("munch") - float(person[3]), 2)
    if swipes_left > 0 and money_left > 0:
        custom = "Use meal swipe or munch money"
    elif swipes_left > 0 and money_left == 0:
        custom = "Use meal swipe"
    elif swipes_left == 0 and money_left > 0:
        custom = "Use munch money"
    else:
        custom = "Go to Downtown Golden!"
    print(f"{person[0]} {swipes_left} {money_left} {custom}")