
def day6a(filepath):
    char_count=0
    with open(filepath) as f:
        for line in f:
            length = len(line)
            found = False
            for n in range(0,length-4+1):
                for x in range(n,n+4):
                    el = line[x]
                    if line[n:n+4].count(el)>1:
                        break
                    elif x == n+3 and line[n:n+4].count(el)==1:
                        found=True
                        char_count += n+3+1 
                if found:
                    break 
    return char_count


def day6b(filepath):
    char_count=0
    with open(filepath) as f:
        for line in f:
            length = len(line)
            found = False
            for n in range(0,length-14+1):
                for x in range(n,n+14):
                    el = line[x]
                    if line[n:n+14].count(el)>1:
                        break
                    elif x == n+13 and line[n:n+14].count(el)==1:
                        found=True
                        char_count += n+13+1 
                if found:
                    break 
    return char_count

#print(day6a('day6_veronica.txt'))
#print(day6a('henna_day6.txt'))
#print(day6b('henna_day6.txt'))
print(day6b('day6_veronica.txt'))