def quick_sort(L):
    if len(L) <= 1:
        return L

    # 가장 첫번째 원소를 피벗으로 정함
    pivot = L[0]

    left_list, right_list = [], []

    for el in L[1:]:
        if el > pivot:
            right_list.append(el)
        else:
            left_list.append(el)

    return quick_sort(left_list) + [pivot] + quick_sort(right_list)


if __name__ == '__main__':
    print([1,2,3,4] == quick_sort([1,2,3,4]), quick_sort([1,2,3,4]))
    print([1,2,3,4] == quick_sort([4,3,2,1]), quick_sort([4,3,2,1]))
    print([1,2,3,4] == quick_sort([1,3,2,4]), quick_sort([1,3,2,4]))
    print([1,2,3,4,5] == quick_sort([1,3,2,4,5]), quick_sort([1,3,2,4,5]))
    print([1,2,3,3,5] == quick_sort([1,3,2,3,5]), quick_sort([1,3,2,3,5]))
