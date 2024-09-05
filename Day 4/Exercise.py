#Practice 1
import random
import my_module

randNum = random.randint(0, 1)
if randNum == 0:
    print("Heads")
else:
    print("Tails")

randFloat = random.random() * 10
randUni = random.uniform(1,10)
print(randFloat)
print(randUni)
print(my_module.greetings)


#Practice 2
fruits = ["Apple", "Mango", "Pineapple", "Orange", "Water melon"]

print(fruits[-1])
updatedFruits = fruits[-1] = "Cashew"
print(updatedFruits)
print(fruits.append("Straw berry"))



