print("Welcome to Mybot")

question=[
    'hello',
    'hello there',
    'how are you',
    'iam fine, are you',
    'hi',
    'hiii..'

]



def train():
    try:
        while True:
            que=input("Question :")
            if que=="done":
                break
            ans=input("Ans :")
            question.append(que)
            question.append(ans)
        print("Bot Trained succesfully.########### 100%.")
    except:
        print("Something went wrong,")
def bot():
    try:
        while True:
            user=input("You :")
            if user in question:
                index=(question.index(user))+1
                bot=question[index]
                print(bot)
            elif user=="quit":
                break
                
            elif user not in question :
                print("Sorry,iam not trained for this question")
    except:
        print("Something went wrong,")
while True:
    u=int(input("1.to train,2.to chat ,3.Exit:"))
    if u==3:
        break
    if u==1:
        train()
    elif u==2:
        bot()



    