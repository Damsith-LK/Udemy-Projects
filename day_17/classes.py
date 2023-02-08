# I quite understood this classes thing

class InstagramUser:

    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id
        self.followers = 0
        self.following = 0
        print("A new user has been registered.")  # Whenever a new object is made this is going to be printed out

    def follow(self, user):
        self.following += 1
        user.followers += 1
        print(f"The followers number of {user.username} changed to {user.followers}")
        print(f"And the following amount of {self.username} changed to {self.following}")


user_1 = InstagramUser("Damsith-LK", "0001")
user_2 = InstagramUser('Devmith-NZ', '0002')

# Here the user_2 is going to follow the user_1
user_2.follow(user_1)

print(user_1.followers)
print(user_2.following)
print(user_1.following)
print(user_2.followers)