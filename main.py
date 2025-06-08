import random


# First option
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))


# Second option
random_friend = random.randint(0,4)
print(friends[random_friend])