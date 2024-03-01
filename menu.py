from show import Show

classmates = ["Ricado", "João"]
def menu():
    show = Show()
    for i in range(len(classmates)):
        print(f"{i + 1} - {classmates[i]}")
    try:
        opt = int(input("Choose a classmate: "))
        match (opt):
            case 1: print(show.ricardo())
            case 2: print(show.joao())
            case 3: print(show.truck())
            case 4: print(show.bears())
            case _: raise ValueError
    except ValueError:
        print("Invalid option!")
menu()