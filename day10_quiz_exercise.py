questions = [["what is the capital of India?", "Delhi"],
             ["which language is used for web development?", "Python"],
             ["who is known as the father of computer?", "charles babbage"],
             ]
prize_money = [1000, 2000, 3000, 5000]
total_amount = 0

print("welcome to KBC quiz game\n")

for i in range(len(questions)):
    print("Question", i+1, ":", questions[i][0])
    answer = input("your answer: ")
    if answer.lower() == questions[i][1].lower():
        total_amount = prize_money[i]
        print("correct answer ✅")
        print("you won ", total_amount,"\n")
    else:
        print("wrong answer")
        break
print("game over")
print("total amount you are taking home is : ", total_amount)
