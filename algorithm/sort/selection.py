def selection(L):
    for end_pos in reversed(range(len(L))):
        max_pos = end_pos
        for pos in range(end_pos):
            if L[pos] > L[max_pos]:
                max_pos = pos

        L[max_pos], L[end_pos] = L[end_pos], L[max_pos]

    return L


if __name__ == '__main__':
    print([1,2,3,4] == selection([1,2,3,4]), selection([1,2,3,4]))
    print([1,2,3,4] == selection([4,3,2,1]), selection([4,3,2,1]))
    print([1,2,3,4] == selection([1,3,2,4]), selection([1,3,2,4]))
    print([1,2,3,4,5] == selection([5,1,3,2,4]), selection([5,1,3,2,4]))
