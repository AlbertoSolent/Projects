nums = [5, 2, 5, 2, 2]

for xs in nums:
    output = ""
    for count in range(xs):
        output+="*"
    print(output)


    
rows = int(input())
cols = int(input())
for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print( )