import os 
import pandas as pd
import matplotlib.pyplot as plt
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def save_to_csv(self):
        data = {"name" : [self.name], "marks" : [self.marks]}
        df = pd.DataFrame(data)
        if os.path.exists("student.csv"):
            df.to_csv("student.csv", mode = "a", header = False, index = False)
        else:
            df.to_csv("student.csv", index=False)
menu = 0
while menu != 6:
    menu = int(input("Choose ur option - 1, 2, 3, 4, 5, 6"))
    if menu == 1:
        name = input("What is ur name?")
        marks = input("What is ur marks?")
        s = student(name, int(marks))
        s.save_to_csv()
    elif menu == 2:
        df = pd.read_csv("student.csv")
        print(df)
    elif menu == 3:
        df = pd.read_csv("student.csv")
        print(df.describe())
    elif menu == 4:
        df = pd.read_csv("student.csv")
        plt.bar(df["name"], df["marks"])
        plt.title("All students marks!")
        plt.xlabel("name")
        plt.ylabel("marks")
        plt.show()
    elif menu == 5:
        score = 0
        print("Quiz time!")
        Quiz1 = int(input("1) What is used to create a function? 1) class 2) def 3)for 4) import"))
        if Quiz1 == 2:
            print("U are correct!")
            score = score + 1
        else:
            print("U are wrong!")
        Quiz2 = int(input("2) for graph what we used? 1) class 2) nothing 3) visualization 4) def"))
        if Quiz2 == 3:
            print("U are correct!")
            score = score + 1
        else:
            print("U are wrong!")
            
        print(f"Your score is {score}/2")
    elif menu == 6:
        print("Quit! You are out!")
        break

        







                    

            



        




    