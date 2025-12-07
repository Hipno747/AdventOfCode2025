# Extract each range of codes from the input file
with open("challenge2input.txt", "r") as file:
    coderanges = file.read().split(",")

#Initialize sum of invalid codes
invalidsum = 0

# Split each range into lower and upper bounds
for coderange in coderanges:
    split = coderange.index("-")
    lowerbound = int(coderange[:split])
    upperbound = int(coderange[split + 1 :])
    # Check if each identifier in the range is invalid (first half matches second half), if invalid add to sum
    for identifier in range(lowerbound, upperbound + 1):
        stringid = str(identifier)
        if len(stringid) % 2 == 0 and stringid[: len(stringid) // 2] == stringid[len(stringid) // 2 :]:
            invalidsum += identifier

# Print the sum of invalid codes
print(invalidsum)