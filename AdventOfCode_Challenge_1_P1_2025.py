pos = int(50)
password = 0

# split the input into a list of instruction strings, e.g. 'R78'
with open("input.txt", "r") as file:
    lines = [line.rstrip('\n') for line in file]

#iterate through each instruction, using the first letter to determine addition or subtracting and the following numbers to determine the amount.
for instruction in lines:
    if instruction[0] == "R":
        pos += int(instruction[1:])
    elif instruction[0] == "L":
        pos -= int(instruction[1:])
    # use the modulus function to ensure that the value remains between 0 and 99
    pos = pos % 100
    #the password is incremented if the current position is zero
    if pos == 0:
        password += 1
        
print(password)
