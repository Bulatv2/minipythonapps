
def main():
    things = 11 # The game can have 7, 11, 15, 19, 21, ... things.
    print("""Game Bashe. There are 11 items. Rivals go in turn, \nfor each move any of the players can take 1, 2 or 3 items. \nLoses the one who is forced to take the last item.
             \nИгра Баше. 11 предметов. Соперники ходят по очереди, за каждый ход любой  из играющих может взять 1, 2 или 3 предмета. \nПроигрывает тот, кто вынужден взять последний предмет.\n""")
    while True:
        user = int(input('Enter: number 1, 2 or 3: '))
        things -= user
        if things < 5:
            apptake = 4 - user
        else:
            apptake = 3 - user
        if apptake == 0:
            apptake = 1
        things -= apptake
        print("The app took {}. Total left {}".format(apptake, things))
        if things == 0:
            print("You win!")
        elif things == 1:
            print("You lost!")
        if things == 0 or things == 1:
            print("Do you want play again? (y or n)")
            if input("> ").lower().startswith("n"):
                break
            else:
                print("Thanks for playing!")
                things = 11
if __name__ == "__main__":
    main()
