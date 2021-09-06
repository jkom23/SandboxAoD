import random
print("Welcome to Zoltan's Fortune Reader")
#greets the user
name = input("What is your name?\n")
#ask user for name
print("Hello " + name)
#says hello
responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."] 
#makes list with responses
gameRun = True

while gameRun:
 #while the user wants to play, they ask a question and random response is made
    question = input("Ask a question\n")
    LikeAns = False
    n = random.choice(responses)
    print(n)
    while LikeAns==False:
    #while the user does not like their their answer
        print(name + ", do you like your answer?\n")
        reply = input("Yes: y  No: n  Quit: q\n")
        while reply not in ["y", "n", "q"]:
            reply = input("Invalid response. Type y, n, or q\n")
        if reply=="y":
                LikeAns = True
                #they like their answer so it asks another question
        elif reply=="n":
                n = random.choice(responses)
                print(n)
                #if they dont like answer, give them new answer
        else:
            gameRun = False
            LikeAns = True
            #quit game
                
print("Thanks for playing at Zoltan's Fortune Reader. Come again soon!")
 #closing message
       
        
