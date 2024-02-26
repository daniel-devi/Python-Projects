import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

highscore = 1000

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


start = input("Do you want to Play our Maths GAME : (Y)/(N)").upper()

while start == "Y":
    input("Press enter to start!")
    wrong =0
    print("----------------------")

    start_time = time.time()

    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        while True:
            guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
            if guess == str(answer):
                break
            wrong += 1

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    if total_time <= highscore:
        print("################ New Highscore Achieved ########################")
        highscore = total_time
    else:
        pass
    if wrong == 0:
        print("Yahh you got none Wrong")
    else:
        print(f"You got {wrong} Wrong")
        

    print(f"You Highscore is {highscore} seconds... ")
    print("----------------------")
    print("Nice work! You finished in", total_time, "seconds!")
    print("----------------------")

print("Thanks for Playing")