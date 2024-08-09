class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = float(weight)
        self.category = category

        # Метод возвращает строку в формате <название>, <вес>, <категория>'.
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}."


class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        K = file.read()
        file.close()
        return K

    def add(self, *products):
        self.file = open(self.__file_name, 'a')
        for i in products:
            if i.name not in self.get_products():
                self.file.write(str(i) + '\n')
                self.file.seek(0)
            else:
                print(f"Продукт {i.name} уже есть в магазине.")
        self.file.close()


P1 = Product('Potato', 50.5, 'Vegetables')
P2 = Product('Spagetti', 3.4, 'Groceries')
P3 = Product('Potato', 5.5, 'Vegetables')

print(str(P2))
print()

s1 = Shop()
s1.add(P1, P2, P3)
print(s1.get_products())