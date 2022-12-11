# a = 97
# A = 65

def day3a(filepath):
    priorities_sum = 0
    with open(filepath) as f:
        for line in f:
            length = len(line)
            for x in range(length//2):
                el = line[x]
                if el in line[length//2:]:
                    if ord(el) > 97:
                        priorities_sum += ord(el)-96
                    else:
                        priorities_sum += ord(el)-38 
                    break   
    return priorities_sum 

def day3b(filepath):
    priorities_sum = 0
    with open(filepath) as f:
        common_items = ""
        count = 0
        for line in f:
            count +=1
            if not common_items:
                    common_items =  line
            else:
                for el in common_items:
                    if el not in line:
                        common_items = common_items.replace(el, '')
            if count ==3:
                element_in_common = common_items[0]
                if ord(element_in_common) > 97:
                    priorities_sum += ord(element_in_common)-96
                else:
                    priorities_sum += ord(element_in_common)-38 
                common_items= ""
                count = 0  
    return priorities_sum                
print(day3b('day3_veronica.txt'))