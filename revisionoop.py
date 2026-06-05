class phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def details(self):
        print(f"My brand is {self.brand} and my price is {self.price}!")
phone1 = phone("Samsung", 20000)
phone1.details()
phone2 = phone("Iphone", 80000)
phone2.details()
