import os
import pandas as pd
import matplotlib.pyplot as plt
class transaction:
    def __init__(self, income, category):
        self.income = income
        self.category = category
    def save_to_csv(self):
        data = {"income" : [self.income], "category" : [self.category]}
        df = pd.DataFrame(data)
        if os.path.exists("Financial.csv"):
            df.to_csv("Financial.csv", header = False, index = False, mode = "a")
        else:
            df.to_csv("Financial.csv", index = False)
    def __init__(self, expense, category):
        self.expense = expense
        self.category = category
    def save_to_csv(self):
        data = {"expense" : [self.expense], "catgegory" : [self.category]}
        df = pd.DataFrame(data)
        if os.path.exists("Financial.csv"):
            df.to_csv("Financial.csv", header = False, index = False, mode = "a")
        else:
            df.to_csv("Financial.csv", index = False)
menu = 0
while menu != 6:
    menu = int(input("Choose your option - 1, 2, 3, 4, 5, 6"))
    if menu == 1:
        income = int(input("What is your income?"))
        category = input("What is the category?")
        s = transaction(int(income), category)
        s.save_to_csv
    elif menu == 2:
        expense = int(input("What is your expense?"))
        category = input("What is your category?")
        a = transaction(int(expense), category)
        a.save_to_csv
    elif menu == 3:
        df = pd.read_csv("Financial.csv")
        print(df)
        total_income = df[df["type"]=="income"]["amount"].sum()
        total_expense = df[df["type"]=="expense"]["amount"].sum()
        savings = total_income - total_expense
        print(f"Income: {total_income}")
        print(f"Expenses: {total_expense}")
        print(f"Savings: {savings}")
    elif menu == 4:
        df = pd.read_csv("Financial.csv")
        plt.bar(df["expense"], df["category"])
        plt.title("My annual expense")
        plt.xlabel("expense")
        plt.ylabel("category")
        plt.show()
    elif menu == 5:
        print("Quit! You are out")
        break
    




        




 


    

        


