pos = int(50)
password = 0

# split the input into a list of instruction strings, e.g. 'R78'
with open("challenge1input.txt", "r") as file:
    lines = [line.rstrip('\n') for line in file]

#iterate through each instruction, using the first letter to determine addition or subtracting and the following numbers to determine the amount.
for instruction in lines:
    if instruction[0] == "R":
        for i in range(int(instruction[1:])):
            pos += 1
            if pos == 100:
                pos = 0
            if pos == 0:
                password += 1
    elif instruction[0] == "L":
        for i in range(int(instruction[1:])):
            pos -= 1
            if pos == -1:
                pos = 99
            if pos == 0:
                password += 1

print(password)
