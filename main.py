def timesTable(number):
    output = []
    for i in range(1, number + 1):
        
        table = []
        for x in range(1, number + 1):
            table.append(i * x)
   
        output.append(table)
    
    return output

# Testing
nums = int(input())
print(timesTable(nums))