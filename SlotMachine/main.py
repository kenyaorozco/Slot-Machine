import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#  For our slot machine
ROWS = 3
COLS = 3

# create a dictionary to hold our "images "
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

#  ============ CHECK WIN FUNC =============


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    #  will check for the rows
    for line in range(lines):
        #  check for symbol in column in current row
        symbol = columns[0][line]
        #  will check for the symbol in the column
        for column in columns:
            symbol_to_check = column[line]
            #  check if symbols are the same or not
            if symbol != symbol_to_check:
                break
        else:
            # if it makes it thru the for loop if will give them their winnings
            winnings += values[symbol] * bet
            # check which lines they won on
            winning_lines.append(line + 1)

    return winnings, winning_lines


# ========== SLOT SPIN FUNC ===========
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            # underscore in an anonomus var

    columns = []
    # nested list to replicate our columns
    for _ in range(cols):
        column = []
        # make copy of list so letters can't be repeated the ':' is an indicator to copy the list
        current_symbols = all_symbols[:]
        for _ in range(rows):
            # picks a random letter from our list
            value = random.choice(current_symbols)
            #  removes the value after its been picked so it isn't repeated
            current_symbols.remove(value)
            # add the value to our column
            column.append(value)

        columns.append(column)
    return columns

#  ================== PRINT MACHINE COLUMNS ================


def print_slot_machine(columns):
    #  loop thru every single row
    for row in range(len(columns[0])):
        #  loop thru every column
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                # for every column we print on the current column we are on
                print(column[row], end="")
        print()


#  =================== DEPOSIT FUNC ===================
def deposit():
    # will keep track of users $
    while True:
        amount = input("how much would you like to deposit? $$")
        if amount.isdigit():
            # checking if the amount inputed is a number
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("please enter a number.")

    return amount

#  ==================  PLACE # OF BETS FUNC ============


def get_number_of_line():
    # will keep track of users line bets
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + " )? ")
        if lines.isdigit():
            # checking if the amount inputed is a number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines ")
        else:
            print("please enter a number.")

    return lines

# ================ GET BET FUNC =============


def get_bet():
    while True:
        amount = input("how much would you like to bet on each line? $$")
        if amount.isdigit():
            # checking if the amount inputed is a number
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number.")

    return amount

# ============== MAIN FUNC THAT CALLS OTHER FUNCS ============
def spin(balance):
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough funds to bet that amount, your current balance is: ${balance} ")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won  ${winnings}")
    print(f"You won on lines:", *winning_lines)
    return winnings- total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
main()