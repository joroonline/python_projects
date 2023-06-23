#! /usr/bin/env python3

def get_input() -> int:
    while True:
        try:
            inp = int(input("Type a number between 1 and 9: "))
            if inp < 10 and inp > 0:
                return inp
        except ValueError:
            print()


def field(location):
    print("\033c", end="")

    print(f"""
     {location[0]}|{location[1]}|{location[2]}
    -------
     {location[3]}|{location[4]}|{location[5]}
    -------
     {location[6]}|{location[7]}|{location[8]}
    """)


def win(location):
    if location[0] == location[1] == location[2]:
        return True
    elif location[3] == location[4] == location[5]:
        return True
    elif location[6] == location[7] == location[8]:
        return True
    elif location[0] == location[3] == location[6]:
        return True
    elif location[1] == location[4] == location[7]:
        return True
    elif location[2] == location[5] == location[8]:
        return True
    elif location[0] == location[4] == location[8]:
        return True
    elif location[2] == location[4] == location[6]:
        return True
    else:
        return False


if __name__ == "__main__":
    set_ = "x"
    location = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    field(location)

    for i in range(9):
        inp = get_input() - 1

        if location[inp] != "x" and location[inp] != "o":
            location[inp] = set_
            field(location)
            win_ = win(location)

            if win_ is not False:
                print(f"Player {set_} won the game!")
                break
            if set_ == "x":
                set_ = "o"
            else:
                set_ = "x"

    if win_ is False:
        print("No one won the game!")
