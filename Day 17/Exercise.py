class User:
    def __init__(self, username, user_id):
        self.username = username
        self.id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


User_1 = User("Husssaini", "001")
User_2 = User("Ahmed", "002")
User_1.follow(User_2)
print(User_2.followers)

class Car:
    def __init__(self, seats):
        self.seats = seats
        print(seats)

my_car = Car(5)
print(my_car)