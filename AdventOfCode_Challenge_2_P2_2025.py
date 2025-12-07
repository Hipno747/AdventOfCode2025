# extract each range of codes from the input file
with open("challenge2input.txt", "r") as file:
    coderanges = file.read().split(",")

# initialise sum of invalid codes
invalidsum = 0

# split each range into lower and upper bounds
for coderange in coderanges:
    split = coderange.index("-")
    lowerbound = int(coderange[:split])
    upperbound = int(coderange[split + 1 :])
    # iterate through each identifier in the range
    for identifier in range(lowerbound, upperbound + 1):
        stringid = str(identifier)

        # for each value from 1 to half the length of the string, check if the value repeated forms the whole string. If so, add to invalid sum.
        for value in range(1, len(stringid)//2 + 1):
            if stringid[:value] * (len(stringid) // value) == stringid:
                invalidsum += identifier
                # break from the loop to ensure each invalid identifier is only counted once
                break

# output the sum of invalid codes

print(invalidsum)
