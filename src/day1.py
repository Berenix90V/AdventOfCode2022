

def day1a(filepath):
    max_sum = 0
    with open(filepath) as f:
        sum = 0
        for line in f:
            line = line.replace('\n', '')
            if line:
                sum += int(line)
            else:
                if sum > max_sum:
                    max_sum = sum
                sum = 0
    return max_sum


def day1b(filepath):
    elf_list = []
    with open(filepath) as f:
        sum_energy = 0
        for line in f:
            line = line.replace('\n', '')
            if line:
                sum_energy += int(line)
            else:
                elf_list.append(sum_energy)
                sum_energy = 0
        elf_list.sort()
        elf_list_max = elf_list[-3:]
        elf_sum = sum(elf_list_max)
    return elf_sum

print(day1b('day1_veronica.txt'))
print(day1b('day1_henna.txt'))    
print("Hello")
