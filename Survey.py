numPeople = 2
survey = ["name? ", "age", "favorite color? ", "favorite animal? ", "birthday month?", "favorite music genre? "]
keys = ["name","age","color","animal","birthday","music"]
allAnswers = []
for j in range(numPeople):
    answers = {}
    for i in range(len(survey)):
        answers[keys[i]] = input(survey[i])
    print(answers)
    allAnswers.append(answers)
print(allAnswers)
