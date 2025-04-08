f = open("list.txt", "r")
arr = f.readlines()
f.close()

arr = [x.strip() for x in arr]

for item in arr:
    print(item)
