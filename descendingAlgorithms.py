import main


# Complete
def descending_bubble_sort(draw_info):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if num1 < num2:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                main.draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED})
                yield True


# Complete
def descending_insertion_sort(draw_info):
    arr = draw_info.lst

    for i in range(1, len(arr)):

        val = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] < val:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                main.draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED})
                yield True
            else:
                break
            j -= 1
        yield True
    print(arr)


# Complete
def descending_selection_sort(draw_info):

    arr = draw_info.lst
    for i in range(0, len(arr) - 1):
        min_val = arr[i]
        min_index = i
        for j in range(i + 1, len(arr)):
            main.draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED})
            if arr[j] > min_val:
                min_val = arr[j]
                min_index = j
            yield True
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Complete
def descending_mergesort(draw_info, arr, p_mid_arr):

    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # divide arr to single numbers
        if len(left) % 2 == 1:
            yield from descending_mergesort(draw_info, left, p_mid_arr - (len(left) // 2 + 1))
        else:
            yield from descending_mergesort(draw_info, left, p_mid_arr - (len(left) // 2))

        yield from descending_mergesort(draw_info, right, p_mid_arr + (len(right) // 2))

        # start sorting
        k, i, j = 0, 0, 0
        p_left_arr = p_mid_arr - mid
        p_right_arr = p_mid_arr
        while i < len(left) and j < len(right):
            main.draw_list(draw_info,
                           {p_left_arr + k: draw_info.BLUE,
                            p_left_arr + i: draw_info.GREEN,
                            p_right_arr + j: draw_info.RED})
            if left[i] > right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            yield True

        # When one of them is over one has to add what is left of the other
        while i < len(left):
            main.draw_list(draw_info,
                           {p_left_arr + k: draw_info.BLUE,
                            p_left_arr + i: draw_info.GREEN,
                            p_right_arr + j: draw_info.RED})
            arr[k] = left[i]
            i += 1
            k += 1
            yield True

        while j < len(right):
            main.draw_list(draw_info,
                           {p_left_arr + k: draw_info.BLUE,
                            p_left_arr + i: draw_info.GREEN,
                            p_right_arr + j: draw_info.RED})
            arr[k] = right[j]
            j += 1
            k += 1
            yield True

        lst = draw_info.lst
        lst[p_left_arr: p_left_arr + len(arr)] = arr
        draw_info.set_list(lst)
        main.draw_list(draw_info,
                       {p_left_arr + k: draw_info.BLUE,
                        p_left_arr + i: draw_info.GREEN,
                        p_right_arr + j: draw_info.RED})
        yield True
