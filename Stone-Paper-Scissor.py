import random

# Game symbols
game_move = {
    1: "🪨",   # Stone
    2: "📃",   # Paper
    3: "✂️"    # Scissor
}

print("-----------------------------")

try:
    user_input = int(input(
        "Welcome To 🪨 📃 ✂️ Game\n"
        "-----------------------------\n"
        "1. Stone (🪨)\n"
        "2. Paper (📃)\n"
        "3. Scissor (✂️)\n"
        "Choose Any One By Number : "
    ))

    if user_input not in game_move:
        print("❌ Invalid Choice! Please select 1, 2, or 3.")
    else:
        pc = random.randint(1, 3)

        print("-----------------------------")
        print("PC CHOOSE   :", game_move[pc])
        print("USER CHOOSE :", game_move[user_input])
        print("-----------------------------")

        if pc == user_input:
            print("Match Tie 😑")
        elif (
            (user_input == 1 and pc == 3) or
            (user_input == 2 and pc == 1) or
            (user_input == 3 and pc == 2)
        ):
            print("You Win 💐")
        else:
            print("You Lose 😢")

except ValueError:
    print("❌ Invalid Input! Please enter a number.")

print("-----------------------------")
print("Thanks For Playing 😀")
print("Hope You Enjoy The Game!")
print("-----------------------------")
print("Game Designed By\n\t~ H a c k y B o y")
print("Developer - Hardik Patel")
print("-----------------------------")
