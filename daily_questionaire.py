#this is a soul project
#it will ask the user questions to answer every day
#the questions will evaluate their impact and overall happiness
#and record their responses

def soul_questions():
    q1 = input("How is your day going?\n")
    if (q1 == "good"):
        input("What went well today?\n")
        input("What am I grateful for?\n")
        input("What am I proud of?\n")
        input("If I died today, would I be happy with how I spent the day?\n")
        input("What impact did I have on others today?\n")
    elif (q1 == "bad"):
        input("go fish, workout, read, write. Every little thing is gonna be alright!\n")
    else:
        input("Smile you are alive, go do something that makes you happy\n")

soul_questions()