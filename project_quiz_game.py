#  quiz game
# project 8


questions = ("how many roles are in valorant?: ","what year was valorant created?: ","what agent has knifes as an ult?: ","what agent is from australia?: ","what role does viper have?: ")

options = (("A. 5","B. 6","C. 4","D. 3"),
           ("A. 2021","B. 2020","C. 2022","D. 2023"),
           ("A. sova","B. waylay","C. kayo","D. jett"),
           ("A. phoenix","B. skye","C. cypher","D. clove"),
           ("A. sentinel","B. initiator","C. dualist","D. controller"))

answers = ("C","C","D","B","D")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num +=1

print("------------------------")
print("        RESULT          ")
print("------------------------")

print("answers: ",end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"your score is: {score}%")