funny = input()
totalTime = 0
numCorrect = 0
questions = {}
questionsSolved = []
while funny != "-1":
    stuff = funny.split()
    question = stuff[1]
    correct = stuff[2]
    if correct == 'right':
        totalTime += int(stuff[0])
        numCorrect += 1
        questionsSolved.append(question)
    else:
        if question not in questions:
            questions[question] = 20
        else:
            questions[question] += 20
    funny = input()

for question, time in questions.items():
    if question in questionsSolved:
        totalTime += time


print(numCorrect, totalTime)
