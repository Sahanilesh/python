str = "teeterabcd"
count = 0
for char in str:
    print(char)
    if str.count(char) == 1:
        print("Char is: ", char)
        break;
