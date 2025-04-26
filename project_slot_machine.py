# Slot Machine Program
# project 14
import random 


def spin_row():
    symbols = ["🍒","🍉","🍋","🔔","⭐️"]

    # 1 way to do it
    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results
    # second way to do it:
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        if row[0] == '🍉':
            return bet * 4
        if row[0] == '🍋':
            return bet * 5
        if row[0] == '🔔':
            return bet * 10
        if row[0] == '⭐️':
            return bet * 20
    return 0
def main():
    balance = 100
    print("************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐️")
    print("************************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("place your bet amount: ")

        if not bet.isdigit():
            print("please enter a valid number")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("insufficient funds")
            continue

        if bet <= 0:
            print("bet must be greater than 0")
            continue
        
        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)
        if payout > 0:
            print(f"you won ${payout}")
        else:
            print("sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break
        print("*******************************************")
        print(f"game over your final balance is ${balance}")
        print("*******************************************")

if __name__ == "__main__":
    main()