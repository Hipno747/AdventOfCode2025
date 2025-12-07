# split the input into a list of lines
with open("challenge3input.txt", "r") as file:
    lines = [line.rstrip('\n') for line in file]

# initialise the total sum of the highest combination within each line
maxTotal=0

for line in lines:
    # find the position of the largest value in the line, excluding the last possible value as a second battery must be used
    largest = 9
    while largest >= 0:
        try:
            battery1pos = line.index(str(largest),0,len(line)-1)
            break
        except:
            largest -= 1
    # find the position of the largest value in the line, after the position of the first value
    largest = 9
    while largest >= 0:
        try:
            battery2pos = line[battery1pos+1:].index(str(largest))+battery1pos+1
            break
        except:
            largest -= 1
    # add the sum of the largest combination of 2 values to the total
    maxbattery = int(line[battery1pos] + line[battery2pos])
    maxTotal+=maxbattery

# output the total sum
print(maxTotal)