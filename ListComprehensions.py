#Program that takes this list  and makes a new list that has only the even elements of this list in it
__author = "Mohamed Abouelsaadat"

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
c = []
for i in range(len(a)):
    if (i%2 == 0):
     c.append(a[i])
print(c)