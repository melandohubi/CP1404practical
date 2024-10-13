name = input("Please enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

with open('name.txt', 'r') as file:
    name_from_file = file.readline().strip()
    print(f"Hi {name_from_file}!")

with open('numbers.txt', 'w') as file:
    file.write("17\n42\n400\n")

with open('numbers.txt', 'r') as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())
    total = first_number + second_number
    print(f"The sum of the first two numbers is: {total}")


with open('numbers.txt', 'r') as file:
    total_sum = 0
    for line in file:
        total_sum += int(line.strip())
    print(f"The total of all numbers is: {total_sum}")