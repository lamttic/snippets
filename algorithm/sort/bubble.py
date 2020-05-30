def bubble(L):
    for idx in reversed(range(len(L))):
        for pos in range(idx):
            if L[pos] > L[pos+1]:
                L[pos], L[pos+1] = L[pos+1], L[pos]

    return L


if __name__ == '__main__':
    print([1,2,3,4] == bubble([1,2,3,4]))
    print([1,2,3,4] == bubble([4,3,2,1]))
    print([1,2,3,4] == bubble([1,3,2,4]))
