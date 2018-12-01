L = [2,4]
L1 = [1, 2, 3, 4, 5]

def pansu():
    if len(L)==1:
        while True:
            if L1[0] == L[0]:
                break
            else:
                L1.append(L1.pop(0))
    else:
        L1.remove(L[0])
        while True:
            if L1[0] == L[0]:
                break
            else:
                L1.append(L1.pop(0))
        L1.insert(0, L[0])
    print(L1)

    
if __name__ == "__main__":
    pansu()
    