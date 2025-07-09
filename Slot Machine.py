# importing important modules & declaring some parameters on a global scope first makes the process easier & time-saving.
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

Rows = 3
Cols = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# This is to choose symbols randomly & place them in the columns.
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    Column = []
    for _ in range(Cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(Rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        Column.append(column)

    return Column

# This is to transpose the columns into rows.
def print_slot_machine(Column):
    for row in range(len(Column[0])):
        for i, column in enumerate(Column):
            if i != len(Column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

# This is to check & calculate the winnings by judging the symbols.
def check_winnings(Column, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = Column[0][line]
        for column in Column:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# This is to start the game again & again easily.
def deposite():
    while True:
        amount = input("\nWhat would you like to deposite?\n$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than $0")
        else:
            print("Please enter a number.")

    return amount

# This is to get the number of total lines of the bet.
def get_number_of_lines():
    while True:
        lines = input("\nEnter the number of lines you want to bet on (1 - " + str(MAX_LINES) + ")? : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("\nEnter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

# This is to calculate the bet on each lines.
def get_bet():
    while True:
        amount = input("\nWhat would you like to bet on each line?\n$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be in between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    line = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * line
    print(f"You're betting ${bet} on {line} lines. Total bet : ${total_bet}.")

    slot = get_slot_machine_spin(Rows, Cols, symbol_count)
    print_slot_machine(slot)
    winnings, winning_lines = check_winnings(slot, line, bet, symbol_value)
    print(f"Congratulations! You've won ${winnings}.\n You've won in these lines : ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposite()
    while True:
        print(f"Current balance is : ${balance}")
        answer = input("Press enter to play again.(Q to quit) ").lower()
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with {balance}.")

main()

