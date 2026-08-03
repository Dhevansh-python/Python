basket1={"apple", "banana", "grape", "blueberry", "mango"}
basket2={"orange", "strawberry", "watermelon", "grape"}
print("basket1:", basket1)
print("basket2:", basket2)

basket1.add("kiwi")
basket2.add("plums")
print("Basket 1 after adding Kiwi:",basket1)
print("Basket 1 after adding plums:",basket2)

common_fruits=basket1.intersection(basket2)
print("Fruits in both baskets:", common_fruits)

import array as arr
fruit_counts=arr.array('i', [2, 7, 7, 1])
print("Fruits counts array:", fruit_counts)

fruit_counts.insert(0, 1)
fruit_counts.append(6)

count_of_7=fruit_counts.count(4)
print("Number of times 7 appears:", count_of_7)

fruit_counts.reverse()
print("Reversed fruit counts array:", fruit_counts)

print("")
print("===== CLASS FRUIT BASKET ORGANIER =====")
print("Basket1:",basket1)
print("Basket1:",basket1)
print("Shared fruits:", common_fruits)
print("Fruit counts:", fruit_counts)