# split the input into a list of lines
with open("challenge3input.txt", "r") as file:
    lines = [line.rstrip('\n') for line in file]

# initialise the total sum of the highest combination within each line
maxTotal = 0

for line in lines:
    # initialise the start and end positions for searching within each line
    startpos = 0
    endpos = len(line)-11

    # initialise the value of the selected batteries as an empty string
    linevalue = ""

    # loop 12 times to select 12 batteries
    for i in range(12):
        # search for the largest value within the line, with the beginning position being the position after the last value chosen, and the end position ensuring 12 values will be selected
        largest = 9 
        while largest >= 0:
            try:
                batterypos = line.index(str(largest),startpos,endpos)
                startpos = batterypos + 1
                endpos += 1
                # add the chosen battery value to the line value
                linevalue += line[batterypos]
                break
            except:
                largest -= 1

    # add the line value to the total sum
    maxTotal += int(linevalue)

# output the total sum
print(maxTotal)