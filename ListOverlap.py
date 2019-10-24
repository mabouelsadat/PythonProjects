#program that returns a list that contains only the elements that are common between the lists (without duplicates)
__author = "Mohamed Abouelsaadat"

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 1 , 3]
c = []
for i in range(len(b)):
    if(b[i] in a and b[i] not in c):
        c.append(b[i])
print(c)