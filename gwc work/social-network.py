# idea: social media no passcode, just user and email
class User:
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num
        #self.age = age
        self.pal = []

    def add_pal(self, pal):
        self.pals.append(pal)

    def get_pals(self):
        return self.pals

class Network:
    def __init__(self):
        self.users = []

    def add_users(self, user):
        new_id = len(self.users)
        u = User(user, new_id)
        self.users.append(u)

    def get_users(self, user):
        return self.users

def main():
    done = False
    n = Network()

    while not done:
        userchoice = input("You can... type 'u' to make a username, type 'p' to print the user(s), type 'c' to add a connection, type 'pc' to print the connection(s), or type 'q' to quit.")
        if(userchoice == "u"):
            usr = input("whats your name?")
            n.add_users(usr)

        if(userchoice == "p"):
            print(n.users)
        if(userchoice == "c"):
            x = input("First User:")
            y = input("Second User:")
            for i in range(len(n.users)):
                if x == n.users[i]:
                    n.users[i].add_pal(y)
                    y.add_pal(x)
        if(userchoice == "pc"):
            pc = input("what user do you want connections for?")
            # pc???
            usr.get_pals()
        if(userchoice == "q"):
            quit()
            done = True
main()
