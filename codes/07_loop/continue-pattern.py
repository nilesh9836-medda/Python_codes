for i in range(5):
    for j in range(5):
        if i == j:
            print("0",end=" ")
            continue
        print(j,end=" ")
    print()