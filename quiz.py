import time
import os
import pandas as pd
questions = {
    "python" : [
        {
            "Question" : "What is used to create a function?",
            "Options" : ["class", "def", "import", "pandas"],
            "Answer" : 2
        },
        {
            "Question" : "What is visualization is used for?",
            "Options" : ["max", "min", "Bar Graph", "nothing"],
            "Answer" : 3
        },
        {
            "Question" : "How many types od data are there?",
            "Options" : [3, 2, 5, 4],
            "Answer" : 4
        }
    ],
    "sports" : [
        {
            "Question" : "How many players are there in football?",
            "Options" : [11, 12, 14, 15],
            "Answer" : 1
        },
        {
            "Question" : "Which sport have to deal with bat and ball?",
            "Options" : ["Football", "Cricket", "Tennis", "Basket_Ball"],
            "Answer" : 2
        },
        {
            "Question" : "Which sport has most fan in the world?",
            "Options" : ["Cricket", "Football", "Rugby", "Super_bowl"],
            "Answer" : 2
        }
    ],
    "General Knowledge" : [
        {
            "Question" : "Who is virat kohli?",
            "Options" : ["Cricketer", "footballer", "Tennis person"],
            "Answer" : 1
        },
        {
            "Question" : "Who is Sachin tandulkar?",
            "Options" : ["Goat", "God", "noone", "Who cares"],
            "Answer" : 2
        },
        {
            "Question" : "Who is Ronaldo?",
            "Options" : ["Goat", "no_one", "God", "no_one"],
            "Answer" : 1
        }
    ]
}
class Quiz:
    def __init__(self, player_name, topic):
        self.player_name = player_name
        self.topic = topic
        self.score = 0
    def play(self):
        for q in questions[self.topic]:
            print(q["Question"])
            print(q["Options"])
            start = time.time()
            answer = int(input("What is your answer?"))
            end = time.time()
            if answer == q["Answer"]:
                print("You are correct!")
                self.score += 1
            else:
                print("You are wrong!")
        time_taken = end - start
        print(f"Total time taken is: {time_taken:.2f} seconds!")
        print(f"Your final score is: {self.score}!")
    def save_to_csv(self):
        data = {"player_name" : [self.player_name], "topic" : [self.topic], "score" : [self.score]}
        df = pd.DataFrame(data)
        if os.path.exists("Quiz.csv"):
            df.to_csv("Quiz.csv", mode = "a", header = False, index = False)
        else:
            df.to_csv("Quiz.csv", index = False)
menu = 0
while menu != 5:
    print("1. python quiz")
    print("2. sports quiz")
    print("3. general knowledge quiz")
    print("4. leaderboard")
    print("5. quit")
    menu = int(input("Choose your menu!"))
    if menu == 1:
        name = input("What is your name?")
        quiz = Quiz(name, "python")
        quiz.play()
        quiz.save_to_csv()
    elif menu == 2:
        name = input("What is your name?")
        quiz = Quiz(name, "sports")
        quiz.play()
        quiz.save_to_csv()
    elif menu == 3:
        name = input("What is your name?")
        quiz = Quiz(name, "General Knowledge")
        quiz.play()
        quiz.save_to_csv()
    elif menu == 4:
        df = pd.read_csv("Quiz.csv")
        print(df)
    elif menu == 5:
        print("Bye!")
        break



        
        
        




    
