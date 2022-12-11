def day2a(filepath):
    list2 = ["X", "Y", "Z"]
    winning_association = {
        "A": "Y",
        "B": "Z",
        "C": "X"
    } 

    draw_association = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    } 
    points_sum=0
    with open(filepath) as f:
        for line in f:
            line = line.replace('\n', '')
            opponent = line[0]
            me = line[2]
            points = list2.index(line[2])+1
            if winning_association[opponent] == me:
                points += 6
            elif draw_association[opponent] == me:
                points += 3
            points_sum += points
    return points_sum

def day2b(filepath):
    list2 = ["A", "B", "C"]
    points_dict = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    winning_association = {
        "A": "B",
        "B": "C",
        "C": "A"
    } 

    lose_association = {
        "A": "C",
        "B": "A",
        "C": "B"
    } 
    points_sum=0
    with open(filepath) as f:
        for line in f:
            line = line.replace('\n', '')
            opponent = line[0]
            result = line[2]
            points = points_dict[result]
            if result == "X":
                points += list2.index(lose_association[opponent])+1
            elif result == "Z":
                points += list2.index(winning_association[opponent])+1
            else:
                points += list2.index(opponent)+1
            points_sum += points
    return points_sum

print(day2b('day2_veronica.txt'))
