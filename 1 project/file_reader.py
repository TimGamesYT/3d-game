# напиши код для виконання завдань тут

count = 0
with open('my_file.txt', 'r') as file:
    for string in file:
        string_list = string.split(" ")
        for symbol in string_list:
            if int(symbol) == 1:
                count += 1
print(count)

with open("my_file.txt", 'r') as file:
    lines = file.readlines()
    second_line = lines[13].split()
    item = int(second_line[7])
    print(item)
summ = 0
with open("my_file.txt", "r") as file:
    for string in file:
        string_list = string.split(" ")
        for symbol in string_list:
            summ += int(symbol)
print(summ)