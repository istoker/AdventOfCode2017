def get_row_result(rowlist):
    i = len(rowlist)-1
    while i > 0:
        j = i-1
        while j >= 0:
            if rowlist[i] % rowlist[j] == 0:
                return rowlist[i] / rowlist[j]
            j -= 1
        i -= 1
    return None

result = 0
with open("input-day2.txt") as rfile:
    for row in rfile.readlines():
        result += get_row_result(sorted([int(i) for i in row.split("\t")]))

print(result)
