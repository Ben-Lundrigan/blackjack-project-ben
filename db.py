# Money file module: Handles reading/writing player money to a file.

# Reads player's money amount from file
def read_money():
    try:
        with open("money.txt") as file:
            line = file.readline().replace("\n", "")
            return float(line)
    except FileNotFoundError:
        print("Money file not found. Starting with 100.0.")
        return 100.0
    except ValueError:
        print("Money file corrupted. Resetting to 100.0.")
        return 100.0

# Updates player's money amount to file
def write_money(money):
    try:
        with open("money.txt", "w") as file:
            file.write(str(money) + "\n")
    except Exception:
        print("Error writing money file.")