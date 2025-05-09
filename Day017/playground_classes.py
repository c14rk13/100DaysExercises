class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following +=1

user_1 = User("001","Ola" )
user_2 = User("002", "Blah")

user_1.follow(user_2)

print(f"User 1 follower count is {user_1.followers}; following count is {user_1.following}")
print(f"User 2 follower count is {user_2.followers}; following count is {user_2.following}")
