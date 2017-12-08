def is_word_unique(word, rest):
    return not word in rest

def is_passphrase_valid(passphrase):
    if passphrase == []:
        return True
    if is_word_unique(passphrase[0], passphrase[1:]):
        return is_passphrase_valid(passphrase[1:])
    else:
        return False

def string_sort(elem):
    return ''.join(sorted(elem))

result = 0
with open("input-day4.txt") as rfile:
    for line in rfile.readlines():
        if is_passphrase_valid(list(map(string_sort, line.strip().split(" ")))):
            result += 1
print(result)
