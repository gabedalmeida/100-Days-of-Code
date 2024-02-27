class User:
    def __init__(self, user_id, user_name):
        #Initialise attributid
        self.id = user_id 
        self.user_name = user_name
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        



user1 = User("001", "gabriel")
    
user2 = User("453","james")
    


user1.follow(user2)

print(user1.following)
print(user1.followers)
print(user2.following)
print(user2.followers)

