def binary_search(L, target):
    start = 0
    end = len(L) - 1

    while start <= end:
        mid = (start + end) // 2

        if target == L[mid]:
            return mid
        elif target < L[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return None


if __name__ == '__main__':
    print(2 == binary_search([1,2,3,4], 3))
    print(None == binary_search([1,2,3,6], 5))
    print(0 == binary_search([1,2,3,4,5,6], 1))
