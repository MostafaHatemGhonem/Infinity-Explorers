LETTER = input("Add Letter From A to Z: ").upper()


if len(LETTER) > 1:

    print("You Must Write One Character Only")

elif LETTER not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

    print("The Letter Not In A - Z")

else:

    try:

        print(f"You Typed {LETTER}")

    except ZeroDivisionError:

        print("Can't Divide By Zero")

    except Exception as e:

        print(f"Something went wrong: {e}")

# Your Code Here