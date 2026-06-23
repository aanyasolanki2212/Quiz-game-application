questions = [
    ["q1. What is the capital of France?", "a) Paris", "b) London", "c) Berlin", "d) Madrid", "a"],
    ["Q2. What is the largest planet in our solar system?", "a) Earth", "b) Jupiter", "c) Mars", "d) Venus", "b"],
    ["Q3. Who wrote the play 'Romeo and Juliet'?", "a) William Shakespeare", "b) Charles Dickens", "c) Jane Austen", "d) Mark Twain", "a"],
    ["Q4. What is the chemical symbol for water?", "a) H2O", "b) CO2", "c) O2", "d) NaCl", "a"],
    ["Q5. Which country is known as the Land of the Rising Sun?", "a) China", "b) Japan", "c) South Korea", "d) Thailand", "b"]
]

p=0

print("This is a quix game, you will be asked 5 questions and you have to choose the correct answer from the options given. Each correct answer will give you 1 point. Let's start!")
i=1

for i in questions:
    print(i[0] + "\n" + i[1] + "\n" + i[2] + "\n" + i[3] + "\n" + i[4])
    s=input("Enter your answer:    ").lower()
    s=list(s)
    if i[-1::]==s:
        print("Your answer is right")
        p+=1
    else:    
        print("your Answer is wrong")
if p==5:
    print("Your total score is 5")
elif p>2 and p<5:
    print("yoy did a good job")
else:
    print("Need to work hard")
print(f"Your total score is {p}")