class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def get_friends(self):
        return self.friends

    def get_name(self):
        pass
        # do stuff here

def main():
    human_1 = Human("Maeve", 15)
    human_2 = Human("Kate", 11)
    human_3 = Human("Nicki", 21)

    human_1.add_friend(human_2)
    human_1.add_friend(human_3)

    friends = human_1.get_friends()
    for eachFriend in friends:
        print(eachFriend.name)

    print(human_1.name, human_1.age)
    print(human_2.name, human_2.age)
    print(human_1.friends[0].name)

main()
