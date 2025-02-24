def quizgame():
    print("Lets play the game...")
    score=0
    while(True):
        Q1=input("What is the Capital of India?")
        if(Q1.lower()=='delhi'):
            score+=1
        else:
            print("Wrong answer")
            break

        Q2=input("Who is the future CM of TN?")
        if(Q2.lower()=='vijay'):
            score+=1
        else:
            print("Wrong answer")
            break

        Q3=input("Which team won the T20 world cup in 2024?")
        if(Q3.lower()=='india'):
            score+=1
        else:
            print("Wrong answer")
            break

        Q4=input("Which team won the IPL 2020?")
        if(Q4.lower()=='mumbai'):
            score+=1
        else:
            print("Wrong answer")
            break

        Q5=input("Who is the PM of India?")
        if(Q5.lower()=='praveen'):
            score+=1
        else:
            print("Wrong answer")
            break
        break
    print("Total score",score)

quizgame()

     
