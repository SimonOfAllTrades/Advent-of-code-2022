inputFilename = "input/day2.txt"

roundList = []
points = 0

with open(inputFilename) as f:
    while(line := f.readline()):
        opponent = line[0]
        me = line[-2]

        if opponent == 'A':
            if me == 'X':
                points += 1 + 3
            elif me == 'Y':
                points += 2 + 6
            elif me == 'Z':
                points += 3 + 0
        elif opponent == 'B':
            if me == 'X':
                points += 1 + 0
            elif me == 'Y':
                points += 2 + 3
            elif me == 'Z':
                points += 3 + 6
        elif opponent == 'C':
            if me == 'X':
                points += 1 + 6
            elif me == 'Y':
                points += 2 + 0
            elif me == 'Z':
                points += 3 + 3


print(points)