# Money file module

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

def write_money(money):
    try:
        with open("money.txt", "w") as file:
            file.write(str(money) + "\n")
    except Exception:
        print("Error writing money file.")