print(r'''
                   ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_move = input("Are you want to Go right or left?")
if first_move == "Left" or first_move == "left":
    print("Congratulation You come closer to Treasure Now your task to Go Island")
    second_move = input("So are you wait for boat or swim to reach Island")
    if second_move == "wait" or second_move == "Wait":
        print("Oh! Amazing you reached successfully The Treasure Island Go to Cave.")
        third_move = input("Choose one gate and Treasure is your's \n"
                                 "Red, Blue or Green")
        if third_move == "Red" or third_move == "red":
            print("Now you are burning and your Game is over")
        elif third_move == "Blue" or third_move == "blue":
            print("Welcomed by Beast and your Game is over")
        elif third_move == "Green" or third_move == "green":
            print("Congratulation you win the game and Take this Treasure and fullfill your life with Joyfully")
        else:
            print("Sorry you enter wrong exception case")
    else:
        print("In the Water have shark they are eating you")
else:
    print("You are falling in hole")