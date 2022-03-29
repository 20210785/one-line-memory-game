game=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
import random
list1=random.sample(range(65,75),10)
list2=random.sample(range(65,75),10)    
len_game=len(game)
count1=0       #score player1
count2=0       #score player2
new_game=[]    #a new list  to show a new line with the two characters that equal to the numbers the player entered
stop=0         #that counter to stop the game and prove that all the list elements='*'
print("please enter number from 1 to 20")
for i in range (0,10):
    list1[i]=chr(list1[i])
    list2[i]=chr(list2[i])
    list1.append(list2[i]) #to make one list of characters
#print(list1)
while(stop<10):
    print("Welcome: ",game)
    print("player#1 - score" , count1 ,":")
    pl1_num1=int(input())
    pl1_num2=int(input()) 
    for i in range (0,len_game):
        if(i==(pl1_num1-1)):
            new_game.append(list1[i])
        elif(i==(pl1_num2-1)):
            new_game.append(list1[i])
        else:
            new_game.append(game[i])
    print("Welcome: " , new_game)
    print("Screen is cleared")
    print(" ")
    if (list1[pl1_num1-1]==list1[pl1_num2-1]):
        game[pl1_num1-1]=game[pl1_num2-1]='*'
        count1+=1
        stop+=1
    new_game.clear()  #to clear the new list from elements

    print("Welcome: ",game)
    print("player#2 - score" , count2 ,":")
    pl2_num1=int(input())
    pl2_num2=int(input())
    for i in range (0,len_game):
        if(i==(pl2_num1-1)):
            new_game.append(list1[i])
        elif(i==(pl2_num2-1)):
            new_game.append(list1[i])
        else:
            new_game.append(game[i])
    print("Welcome: " , new_game)
    print("Screen is cleared")
    print(" ")
    new_game.clear()
    if (list1[pl2_num1-1]==list1[pl2_num2-1]):
        game[pl2_num1-1]=game[pl2_num2-1]='*'
        count2+=1
        stop+=1

if (count1>count2):
    print("Player1 wins")
elif(count2>count1):
    print("Player2 wins")
else:
    print("Score is equal")
