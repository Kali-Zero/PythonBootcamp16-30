class Car:
    #Constructor (initializer)
    #Will get called every time you create a new instance of the class
    # Sets initial attributes for the class
    def __init__(self, seats):
        self.seats = seats

    #always needs the 'self' parameter first
    #usually used on all methods INSIDE a class
    def enter_race_mode(self):
        self.seats = 2

# Sets the 'seats' attribute(variable) to '5'
my_car = Car(5)
#Works the same as writing my_car.seats = 5

class User:
    def __init__(self, user_id, username):
        #print("New User Being Created...")
        # Takes in a user_id, which is passed in whenever a new user is constructed
        self.user_id = user_id
        self.username = username
        #Isn't included in init parameters, because it starts the same for everyone.
        #It's only updated sometime AFTER creation
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


#Creates instance of the class
user_1 = User("001", "Kali")
user_2 = User("002", "Jack")

print(f"User ID: {user_1.user_id}\n    Username: {user_1.username}"
      f"\n    Followers: {user_1.followers}\n    Following: {user_1.following}\n")

#Creates attributes for the instance of the class NOT in init
user_1.follow(user_2)
user_2.follow(user_1)

print(f"User ID: {user_1.user_id}\n    Username: {user_1.username}"
      f"\n    Followers: {user_1.followers}\n    Following: {user_1.following}\n")
print(f"User ID: {user_2.user_id}\n    Username: {user_2.username}"
      f"\n    Followers: {user_2.followers}\n    Following: {user_2.following}\n")