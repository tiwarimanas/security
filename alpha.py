import string

for i in string.ascii_letters:
    for j in string.ascii_letters:
        for k in string.ascii_letters:
            for l in string.ascii_letters:
                print(i,j,k,l)
                if i == 'Z' and j == 'Z' and k == 'Z' and l == 'Z':
                    break
