import random
arrlist = []
for i in range(10):
    ran = random.randint(1,100)
    if ran not in arrlist:
        arrlist.append(ran)
print(arrlist)