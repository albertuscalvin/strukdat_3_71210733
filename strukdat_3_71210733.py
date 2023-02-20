kamus = dict()
file = open("file.txt", "r")
file1 = file.read()
print(file1)
file2 = file1.split()
for file3 in file2:
    if file3 not in kamus:
        kamus[file3] = 1
    else :
        kamus[file3] += 1
print("total kata=", len(file2))
print(kamus)
