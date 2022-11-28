x = 123
y = str(x)
helper = y[::-1]

for i in y:
    for j in helper:
        if y[i] != helper[j]:
            print(y[i], helper[j])
            print("Itt megszakad")
            break
        else:
            print(y[i], helper[j])
            print("Szep")
