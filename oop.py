class student:
    def __init__(self,name,college):
        self.name = name
        self.college = college
    def introduce(self):
        print(f"my name is {self.name} and i study at {self.college}")

student1 = student("Amlan", "Kiit")
student1.introduce()
student2 = student("Rahul", "IIT")
student2.introduce()
class KiitStudent(student):
    def __init__(self,name, branch):
        self.name = name
        self.branch = branch
    def info(self):
        print(f"my name is {self.name} and my kiit branch is {self.branch}!")
KiitStudent1 = KiitStudent("Amlan", "CSE WITH AI AND ML")
KiitStudent1.info()






        