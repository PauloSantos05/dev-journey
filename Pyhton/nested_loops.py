rows = int(input("Type the number of rows: "))
columns = int(input("Type the number of columns: "))
symbol = input("Type a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')  # print symbol without a newline
    print()  # print a newline after each row