import matplotlib.pyplot as plt
Subjects = ["Maths", "English", "Science"]
marks = [75, 89, 84]
plt.pie(marks, labels=Subjects, autopct="%1.if%%")
plt.title("My marks distribution")
plt.show()
