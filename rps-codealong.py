#welcoming player and giving instructions
print("Welcome Players 1 and 2\n When asked for your choice please enter 'r', 'p', or 's'")

# getting players input
playerOneInput = input("player one selects: r, p, s; ")
playerTwoInput = input("player two selects: r, p, s; ")

# compare player input to determine reseult. Either player1 wins, player2 wins or a tie!
if playerOneInput == "s":
    if playerTwoInput == "s":
        print("Uh oh...It's a tie!")
    if playerTwoInput == "r":
        print("player two wins :) sorry player one!")
    if playerTwoInput == "p":
        print("player one wins <3 sorry player two.")

if playerOneInput == "r":
    if playerTwoInput == "r":
        print("Uh oh...It's a tie!")
    if playerTwoInput == "s":
        print("player one wins <3 sorry player two.")
    if playerTwoInput == "p":
        print("player two wins :) sorry player one!")

if playerOneInput == "p":
    if playerTwoInput == "p":
        print("It's a tie!")
    if playerTwoInput == "r":
        print("player one wins <3 sorry player two.")
    if playerTwoInput == "s":
        print("player two wins :) sorry player one!")