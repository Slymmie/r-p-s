import random

CPU_wins = 0
Player_wins = 0

def Player_Option():
    user_choice = input("Choose...(R for rock) (P for paper) (S for scissors)")
    if user_choice in ["Rock","R","rock","r"]:
        user_choice = "R"
    elif user_choice in ["Paper","P","paper","p"]:
        user_choice = "P"
    elif user_choice in ["Scissors","S","scissors","s"]:
        user_choice = "S"
    else:
        print("not amongst our options, try again please.")
        Player_Option()
    return user_choice

def CPU_Option():
    CPU_choice = random.randint(1,3)
    if CPU_choice == 1:
        CPU_choice = "R"
    elif CPU_choice == 2:
        CPU_choice = "P"
    else:
        CPU_choice = "S"
    return CPU_choice

while True:
    print("")

    user_choice = Player_Option()
    CPU_choice = CPU_Option()

    print("")

    if user_choice == "R":
        if CPU_choice == "R":
            print("Player (Rock) : CPU (Rock) ...You Tied...")
        elif CPU_choice == "P":
            print("Player (Rock) : CPU (Paper) ...You Lose...")
            CPU_wins += 1
        elif CPU_choice == "S":
            print("Player (Rock) : CPU (Scissors) ...You Win...")
            Player_wins += 1

    elif user_choice == "P":
        if CPU_choice == "R":
            print("Player (Paper) : CPU (Rock) ...You Win...")
            Player_wins += 1
        elif CPU_choice == "P":
            print("Player (Paper) : CPU (Paper) ...You Tied...")
        elif CPU_choice == "S":
            print("Player (Paper) : CPU (Scissors) ...You Lose...")
            CPU_wins += 1
    
    elif user_choice == "S":
        if CPU_choice == "R":
            print("Player (Scissors) : CPU (Rock) ...You Lose...")
            CPU_wins += 1
        elif CPU_choice == "P":
            print("Player (Scissors) : CPU (Paper) ...You Win...")
            Player_wins += 1
        elif CPU_choice == "S":
            print("Player (Scissors) : CPU (Scissors) ...You Tied...")

    print("")
    print("Player_wins: "+str(Player_wins))
    print("CPU: "+str(CPU_wins))
    print("")

    user_choice = input("Do you want to play again?(y/n)")
    if user_choice in ["Y", "y", "yes","Yes"]:
        pass
    elif user_choice in ["N", "n", "no","No"]:
        print("See you again... Good bye")
        break
    else:
        break
