# Creating a Class
# To leave a class or function empty we use the keyword "pass"
class User:
    def __init__(self, user_id, user_name): # Constructor
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user): # Class Method
        user.followers += 1
        self.following += 1

user_1 = User("001", "Saksham")
user_2 = User("002", "Jaiswal")

user_1.follow(user_2)

print(user_1.id, user_1.username, user_1.followers, user_1.following)
print(user_2.id, user_2.username, user_2.followers, user_2.following)