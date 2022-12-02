inputFilename = "input/day2.txt"

roundList = []
points = 0

with open(inputFilename) as f:
    while(line := f.readline()):
        opponent = line[0]
        me = line[-2]

        if opponent == 'A':
            if me == 'X':
                points += 0 + 3
            elif me == 'Y':
                points += 3 + 1
            elif me == 'Z':
                points += 6 + 2
        elif opponent == 'B':
            if me == 'X':
                points += 0 + 1
            elif me == 'Y':
                points += 3 + 2
            elif me == 'Z':
                points += 6 + 3
        elif opponent == 'C':
            if me == 'X':
                points += 0 + 2
            elif me == 'Y':
                points += 3 + 3
            elif me == 'Z':
                points += 6 + 1


print(points)