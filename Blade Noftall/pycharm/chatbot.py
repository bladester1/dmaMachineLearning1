


goodHobbies = [" rock climbing", " fishing", " baseball", " video games "]
badHobbies = ["stealing", "being mean"]
videoGames = ["csgo", "brawlhalla", "fortnite", "pubg", "wii sports", "guitar hero", "guitar hero 2", "guitar hero 3", "guitar hero 4", "guitar hero 5", "guitar 6", "guitar hero 7", "guitar hero 8", "agar.io", "temple run lite", "words with friends", "smashy roads", "crossy roads", "jumpy roads", "flappy birds", "gta san adreas", "fortnite", "dark suls", "call of duty", "pong", "et", "roblox", "minecraft", "overwatch", "pacman"]
snacks = ["rockets","smarties","popcorn","pizza","veggies","vegetables","chocolate","candy","you"]
name = ""
def q1():
    print("what is your hobby, " + name .format(name) + "?")
    question1 = input ()
    answer1 = question1
    if answer1 in goodHobbies:
        print(answer1 + " is a great hobby!")
    elif answer1 in badHobbies:
        print("you should stop doing that.")
    else:
        print("i don't know that hobby, it probably is terrible.")

def q2():
    global name
    print("what is your name?")
    name = input()

def q3():
    question2 = input("what video games do you play ")
    answer2 = question2
    if answer2 in videoGames:
        if (answer2 == "et"):
            print("I hate you")
        else:
            print(answer2+ " is great, i play it all the time")

def q4():
    question3 = input("whats your favourite snack food")
    answer3 = question3
    if answer3 in snacks:
        if answer3 == "you":
            print ( "hitting on a bot huh, how lonely are you?")
    elif answer3 in snacks:
        print(answer3+ ", Seriously? i love that too!")
    else:
        print(answer3+ " might be good, i will remember to try that sometime")

def q5():
    question4 = input("how many immediate family members do you have (write as a number)?")
    oneMoreThan = int(question4)-1

    print("wow! " +question4+ " members. that one more than " +str(oneMoreThan)+"!" )

def q6():
    question4 = input("do you have any friends?")
    answer4 = question4
    print("no you don't")











def end():
    print("good chat, talk soon! goodbye.")

# my program
q2()
q5()
q1()
q3()
q4()
q6()
end()

