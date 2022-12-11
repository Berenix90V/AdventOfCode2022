list1 = ['B','G','S','C']
list2 = ['T','M','W','H','J','N','V','G']
list3 = ['M','Q','S']
list4 = ['B','S','L','T','W','N','M']
list5 = ['J','Z','F','T','V','G','W','P']
list6 = ['C','T','B','G','Q','H','S']
list7 = ['T','J','P','B','W']
list8 = ['G','D','C','Z','F','T','Q','M']
list9 = ['N','S','H','B','P','F']

stack_dict={
    1: list1,
    2: list2,
    3: list3,
    4: list4,
    5: list5,
    6: list6,
    7: list7,
    8: list8,
    9: list9
}

def day5a(filepath):
    with open(filepath) as f:
        for line in f:
            if line[0] == 'm':
                results = line.split(' ')
                moves = int(results[1])
                origin = int(results[3])
                destination = int(results[5])
                for n in range(0,moves):
                    length = len(stack_dict[origin])
                    stack_dict[destination].append(stack_dict[origin].pop(length-1))
    endings = ''
    for i in range(1,10):
        endings += stack_dict[i][-1]
    return endings

def day5b(filepath):
    with open(filepath) as f:
        for line in f:
            if line[0] == 'm':
                results = line.split(' ')
                moves = int(results[1])
                origin = int(results[3])
                destination = int(results[5])
                stack_dict[destination].extend(stack_dict[origin][-moves:])
                stack_dict[origin]= stack_dict[origin][:-moves]
    endings = ''
    for i in range(1,10):
        endings += stack_dict[i][-1]
    return endings

print(day5b('day5_veronica.txt'))