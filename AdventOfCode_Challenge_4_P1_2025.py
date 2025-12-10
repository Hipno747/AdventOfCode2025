# split the input into a list of lines, 
with open("challenge4input.txt", "r") as file:
    lines = [line.rstrip('\n') for line in file]

number_of_rows = len(lines)
number_of_columns = len(lines[0])

# initialise variable for number of characters surrounding "@", and total accessible @ characters(less than 4 adjacent "@" characters)
surrounding = 0
total_accessible = 0

# initialise current_row to keep track of which row we are on, and current_character to keep track of which character we are on
current_row = -1
current_character = -1

# you can use lines[row][column] to access a character    

# iterate through each row, counting which row we are on
for current_row, row in enumerate(lines):
    # iterate through each character in the row
    for current_character, char in enumerate(row):
        # reset surrounding counter for this cell
        surrounding = 0

        # only check neighbours when this cell is an "@"
        if char != "@":
            continue
        
        # check all 8 surrounding positions for "@" characters
        # positions are checked with boundaries of the data to prevent index errors

        # left
        if current_character - 1 >= 0 and row[current_character - 1] == "@":
            surrounding += 1
        # right
        if current_character + 1 < number_of_columns and row[current_character + 1] == "@":
            surrounding += 1

        # down-left
        if current_row + 1 < number_of_rows and current_character - 1 >= 0  and lines[current_row + 1][current_character - 1] == "@":
            surrounding += 1
        # down
        if current_row + 1 < number_of_rows  and lines[current_row + 1][current_character] == "@":
            surrounding += 1
        # down-right
        if current_row + 1 < number_of_rows and current_character + 1 < number_of_columns and lines[current_row + 1][current_character + 1] == "@":
            surrounding += 1

        # up-left
        if current_row - 1 >= 0 and current_character - 1 >= 0 and lines[current_row - 1][current_character - 1] == "@":
            surrounding += 1
        # up
        if current_row - 1 >= 0  and lines[current_row - 1][current_character] == "@":
            surrounding += 1
        # up-right
        if current_row - 1 >= 0 and current_character + 1 < number_of_columns and lines[current_row - 1][current_character + 1] == "@":
            surrounding += 1

        # if the number of surrounding "@" characters is less than 4, increment the total accessible count
        if surrounding < 4:
            total_accessible += 1

# output total accessible "@" characters
print(total_accessible)
            
            
            

