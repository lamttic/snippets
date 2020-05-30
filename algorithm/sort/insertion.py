def insertion(L):
    for size in range(1, len(L)):

        '''
        for idx in range(size):
            if L[idx] > L[size]:
                L.pop(size)
                L.insert(idx, current_value)
                break
        '''
        for idx in reversed(range(size)):
            if L[idx+1] < L[idx]:
                L[idx], L[idx+1] = L[idx+1], L[idx]
            else:
                break

    return L


if __name__ == '__main__':
    print([1,2,3,4] == insertion([1,2,3,4]), insertion([1,2,3,4]))
    print([1,2,3,4] == insertion([4,3,2,1]), insertion([4,3,2,1]))
    print([1,2,3,4] == insertion([1,3,2,4]), insertion([1,3,2,4]))
    print([1,2,3,4,5] == insertion([5,1,3,2,4]), insertion([5,1,3,2,4]))
