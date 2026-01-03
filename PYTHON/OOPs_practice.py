class Product:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count += 1
    
    def get_info(self):
        print(f"this is {self.name} or price is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"total product is {cls.count}")

p1 = Product("Laptop",40000)
p2 = Product("macbook",50000)
p3 = Product("pc",60000)

p1.get_info()
p2.get_info()
p3.get_info()

p1.get_count()