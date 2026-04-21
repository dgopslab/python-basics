logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def get_operator(operations):
    while True:
        for symbol in operations:
            print(symbol)

        user_operation = input("Pick an operation: ")

        if user_operation in operations:
            return user_operation

        print("Input ERROR. Try again.")


def user_num(question):
    while True:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Input ERROR. Try again.")


def result_text(n1, n2, operator, final_result):
    print(f"{n1} {operator} {n2} = {final_result}")


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


start_calculator = True

while start_calculator:
    print(logo)

    another_round = True
    first_number = user_num("What's the first number?: ")

    while another_round:
        user_operation = get_operator(operations)
        next_number = user_num("What's the next number?: ")

        if user_operation == "/" and next_number == 0:
            print("You can't divide by zero. Try again.")
            continue

        result = operations[user_operation](first_number, next_number)
        result_text(first_number, next_number, user_operation, result)

        ask_again = True

        while ask_again:
            go_again = input(
                f"Type 'y' to continue calculating with {result}, "
                "or type 'n' to start a new calculation, "
                "or type 'q' to quit: "
            ).lower()

            if go_again == "y":
                first_number = result
                ask_again = False
            elif go_again == "n":
                another_round = False
                ask_again = False
                print("\n" * 100)
            elif go_again == "q":
                start_calculator = False
                another_round = False
                ask_again = False
                print("Goodbye!")
            else:
                print("Input ERROR. Try again.")
