inputFilename = "input/day1q1.txt"

caloriesList = []

with open(inputFilename) as f:
    calories = 0
    while(line := f.readline()):
        if line == '\n':
            caloriesList.append(calories)
            calories = 0
        else:
            calories += int(line)

print(max(caloriesList))
