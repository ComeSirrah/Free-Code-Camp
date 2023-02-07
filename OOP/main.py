from item import Item
from phone import Phone

item_1 = Item("my_item", 750)

item_1.apply_increment(0.2)
item_1.apply_discount()

print(item_1.price)

some_list = ["this", "is", "a", "sentence."]
print(len(some_list))