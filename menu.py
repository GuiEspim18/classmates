import ricardo
import joao

classmates = ["Ricado", "João"]
def menu():
    for i in range(len(classmates)):
        print(f"{i + 1} - {classmates[i]}")
    try:
        opt = int(input("Choose a classmate: "))
        match (opt):
            case 1: print(ricardo.show())
            case 2: print(joao.show())
            case _: raise ValueError
    except ValueError:
        print("Invalid option!")
menu()