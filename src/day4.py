def day4a(filepath):
    count=0
    with open(filepath) as f:
        for line in f:
            int1, int2 = line.split(',')
            min1,max1 = int1.split('-')
            min2,max2 = int2.split('-')
            if int(min1)>int(min2):
                if int(max1)<= int(max2):
                    count +=1
            elif int(min2)>int(min1):
                if int(max2)<=int(max1):
                    count +=1 
            else:
                if int(max1)<= int(max2):
                    count +=1
                elif int(max2)<=int(max1):
                    count +=1 
    return count 

def day4b(filepath):
    count=0
    with open(filepath) as f:
        for line in f:
            int1, int2 = line.split(',')
            min1,max1 = int1.split('-')
            min2,max2 = int2.split('-')
            
            if int(min1)>=int(min2) and int(min1)<=int(max2):
                count += 1
                
            elif int(max1)>=int(min2) and int(max1)<=int(max2):
                count += 1
                
            elif int(min2)>=int(min1) and int(min2)<=int(max1):
                count += 1
            
    return count

print(day4b('day4_veronica.txt'))