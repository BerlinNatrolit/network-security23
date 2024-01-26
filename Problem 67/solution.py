
file = open('0067_triangle.txt', 'r')

pyramid = []
for line in file:
    pyramid.append([int(i) for i in line[:-1].split(' ')])    

counter = 0

for row in range(len(pyramid)-2, -1, -1):
    for index in range(len(pyramid[row])):
        o = pyramid[row][index]
        l = pyramid[row+1][index]
        r = pyramid[row+1][index+1]
        pyramid[row][index] = o + max(l,r)
        counter += 1

print(pyramid[0][0])
print("Count: " + str(counter))

output_file = open('output.txt', 'w')
for row in pyramid:
    output_file.write(str(list(row)) + '\n')
    
    
output_file.close()