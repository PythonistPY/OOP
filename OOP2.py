class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        items_list = ', '.join([f"{item}: ${price}" for item, price in self.items.items()])
        return f"Store: {self.name}\nAddress: {self.address}\nItems: {items_list}"

# Создание объектов класса Store
store1 = Store("SuperMart", "123 Elm Street")
store2 = Store("BestGoods", "456 Oak Avenue")
store3 = Store("DailyNeeds", "789 Pine Road")

# Добавление товаров в ассортимент
store1.add_item("Apples", 0.5)
store1.add_item("Bananas", 0.75)
store2.add_item("Milk", 1.2)
store2.add_item("Bread", 2.0)
store3.add_item("Eggs", 2.5)
store3.add_item("Juice", 1.5)

# Тестирование методов
print("Store1 before updates:")
print(store1)

store1.update_price("Apples", 0.55)  # Обновляем цену на яблоки
print("\nStore1 after updating price of Apples:")
print(store1)

store1.remove_item("Bananas")  # Удаляем бананы
print("\nStore1 after removing Bananas:")
print(store1)

price_of_apples = store1.get_price("Apples")
print(f"\nPrice of Apples in Store1: ${price_of_apples}")

price_of_bananas = store1.get_price("Bananas")
print(f"Price of Bananas in Store1: {price_of_bananas}")
