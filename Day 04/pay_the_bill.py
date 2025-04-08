import random

friends = ["Alice", "Charles", "Ben", "Jane", "Olivia", "Hugh"]
random_friend = random.randint(0, len(friends) - 1)
print(friends[random_friend])