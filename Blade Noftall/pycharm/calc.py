for item in ['apples','bananas','oranges', 2, 3]:
    print ("it's getting warmer")

mylist = ["d", "0", "v", "i", "n"]
for item in mylist:
    print (item)

my2DList = [("1","1","1"),("1","1","1")]

grid = my2DList

for column in grid:
    row = ""
    for r in column:
        row += r
    print(row)