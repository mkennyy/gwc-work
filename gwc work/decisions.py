print("Tomorrow is your first day at your new job!")

done = False
right1 = "You go to the party with your friends and stay out late. By the time you get home it's 3AM and you have to be at work by 8AM."
left1 = "You go to bed early and prepare for work tomorrow. Your clothes are laid out and your lunch is premade."

while not done:
    decision1 = input("You have two options; type 'right' for the 'right option' or type 'left' for the 'left option':")
    if decision1 == "right":
        print (right1)
        done = True
    elif decision1 == "left":
        print (left1)
        done = True;


print("No matter what you did, you still woke up late because the power went out in your building and your alarm didn't wake you up.")

done = False
right2= "You decide to take the train to work so you don't get stuck in traffic, and you make it to work only 5 minutes late."
left2= "You decide to take your car to work, despite the high risk of traffic, and in turn you get to work 40 minutes late."

while not done:
    decision2 = input("You have two options; type 'right' for the 'right option' or type 'left' for the 'left option':")
    if decision2 == "right":
        print (right2)
        done = True
    elif decision2 == "left":
        print (left2)
        done = True;

print("Your boss asks you why you're late and you respond...")

done = False
right3 = "You decide to lie and tell your boss that you had a family emergency last minute."
left3 = "You tell your boss the truth about what happened."

while not done:
    decision3 = input("You have two options; type 'right' for the 'right option' or type 'left' for the 'left option':")
    if decision3 == "right":
        print (right3)
        done = True
    elif decision3 == "left":
        print (left3)
        done = True;

done = False
right4 = "As you walk out of your meeting with your boss, you let the door slam in his face and he breaks his nose and fires you!"
left4 = "As you walk out of your meeting with your boss, a good looking co-worker spills his coffee on you and wants to take you to dinner to make up for it."

while not done:
    decision4 = input("You have two options; type 'right' for the 'right option' or type 'left' for the 'left option':")
    if decision4 == "right":
        print (right4)
        done = True
    elif decision4 == "left":
        print (left4)
        done = True;

done = False
right5 = "You go to a club to distract you from your first day sorrows and you see your co-worker that stood you up from the date you had planned! "
left5 = "You contract an illness from a bug bite and you have to go to the hospital immediately!"

while not done:
    decision5 = input("You have two options; type 'right' for the 'right option' or type 'left' for the 'left option':")
    if decision5 == "right":
        print (right5)
        done = True
    elif decision5 == "left":
        print (left5)
        done = True;

done = False
right6 = "You decide you've had enough with this terrible day and go home to sleep it off. GAME OVER"
left6 = "You decide you've had enough with this terrible day and go home to sleep it off. GAME OVER"

while not done:
    decision6 = input("You have two options; type 'right' for the 'right option' or type 'left' for the 'left option':")
    if decision6 == "right":
        print (right6)
        done = True
    elif decision6 == "left":
        print (left6)
        done = True;
