def merge_sort(L):
    if len(L) == 1:
        return L

    # 분할
    divide_index = len(L) // 2
    left_list, right_list = L[:divide_index], L[divide_index:]
    # 병합
    return merge(merge_sort(left_list), merge_sort(right_list))

def merge(left_list, right_list):
    merged_list = []

    while left_list and right_list:
        if left_list[0] < right_list[0]:
            merged_list.append(left_list.pop(0))
        else:
            merged_list.append(right_list.pop(0))

    merged_list.extend(left_list)
    merged_list.extend(right_list)

    return merged_list


if __name__ == '__main__':
    print([1,2,3,4] == merge_sort([1,2,3,4]), merge_sort([1,2,3,4]))
    print([1,2,3,4] == merge_sort([4,3,2,1]), merge_sort([4,3,2,1]))
    print([1,2,3,4] == merge_sort([1,3,2,4]), merge_sort([1,3,2,4]))
    print([1,2,3,4,5] == merge_sort([1,3,2,4,5]), merge_sort([1,3,2,4,5]))
