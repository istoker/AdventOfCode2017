result = 0
with open("input-day2.txt") as rfile:
    for row in rfile.readlines():
        rowlist = [int(i) for i in row.split("\t")]
        result += max(rowlist) - min(rowlist)

print(result)
