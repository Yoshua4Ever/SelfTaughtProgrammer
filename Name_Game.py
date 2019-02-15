def name_game():
    print("LET'S HAVE FUN WITH YOUR NAME")
    print("Find out if your name is Even or Odd.")
    print("Then let's build a pyramid based on the length of your name.")

    full_name = input("Type your full name: ")
    name_len = len(full_name)

    if name_len != 0:
        name_type = name_len % 2
        if name_type == 0:
            print("Your name is EVEN.")
            print("Now let's build a star pyramid from the number of characters in your name.")

            star = "*"
            for i in range(name_len):
                print(star)
                star = star + "*"
            print("Run the program to play again with a different name.")
        else:
            print("Your name is ODD.")
            print("Now let's build a star pyramid from the number of characters in your name.")

            star = "*"
            for i in range(name_len):
                print(star)
                star = star + "*"
            print("Run the program to play again with a different name.")

    else:
        print("You did not type your name. The Game won't work.")
        print("Run the program again and type your full name.")
    

name_game()
