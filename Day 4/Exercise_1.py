import random
males = ["Charlie", "David", "Emmanuel", ]
females = ["Alice", "Angela", ]
friends = [males, females] #Nested lists

#Option 1
randomNum = random.randint(0 , int(len(friends) - 1))
print(friends[randomNum])

#Option 2
randFriend = random.choice(friends)
print(randFriend)

