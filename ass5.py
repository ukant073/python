import random

comp_point=0
ujjwal_point=0
print("Welcome to Stone|Paper|Scissor")
    
def game_menu():
    
    print("Enter 1 for Stone:")
    print("Enter 2 for Papaer:")
    print("Enter 3 for Scissor:")
    
choice=True    
while(choice):
   
    game_menu()
    choice = int(input())
    
    if(choice==1):
        choice_name = "Stone"
        

    elif(choice==2):
        choice_name = "Paper"
        
    elif(choice==3):
        choice_name = "Scissor"
        
    else:
        print("Enter a valid number")

    print("ujjwal choice is:",choice_name)
    print("\nnow its computer turn")
    


    choice_comp = random.randint(1,3)
    
    while choice_comp == choice:
        choice_comp = random.randint(1,3)

        
    if(choice_comp==1):
        choice_comp_name = "Stone"
            

    elif(choice_comp==2):
        choice_comp_name = "Paper"

    else:
        choice_comp_name = "Scissor"
            
    print("computer choice is:",choice_comp_name)
    print(choice_name,"vs",choice_comp_name)

    
    if(choice==1 and choice_comp==2):
        print("I lost this round")
        comp_point=comp_point+1

    elif(choice==1 and choice_comp==3):
        print("i won this round")
        ujjwal_point=ujjwal_point+1

    elif(choice==2 and choice_comp==1):
        print("I won this round")
        ujjwal_point=ujjwal_point+1
    
    elif(choice==3 and choice_comp==1):
        print("i lost this round")
        comp_point=comp_point+1

    
    elif(choice==2 and choice_comp==3):
        print("i lost this round")
        comp_point=comp_point+1
    
    elif(choice==3 and choice_comp==2):
        print("i won this round")
        ujjwal_point=ujjwal_point+1

    else:
        print("huh?")      
              
        
    print("ujjwal",ujjwal_point,"computer",comp_point)


    if(ujjwal_point==5):
        print("ujjwal won the game")
        break
    elif(comp_point==5):
        print("computer won the game")
        break
    
    

c = input("Do you want to play again?(Y/N):")
if(c=="n"or c=="N"):
    choice = False
    print("I will see you next time")

elif(c=="y" or c=="Y"):
    choice = True


































    
