# Money file module

def read_money():
    with open("money.txt") as file:
        return float(file.readline())

def write_money():
    with open("money.txt", "w") as file:
        file.write(str(money))