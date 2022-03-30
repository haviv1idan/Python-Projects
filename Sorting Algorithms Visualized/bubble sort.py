import random


def ascending_bubble_sort(lst):

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if num1 > num2:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def descending_bubble_sort(lst):

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if num1 < num2:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def main():
    min_val = 1
    max_val = 100
    length_of_arr = 50
    arr = [random.randint(min_val, max_val) for _ in range(length_of_arr)]

    print("arr before sort: \n", arr)
    ascending_bubble_sort(arr)
    print("sorted arr: \n", arr)

    arr = [random.randint(min_val, max_val) for _ in range(length_of_arr)]
    print("arr before sort: \n", arr)
    ascending_bubble_sort(arr)
    print("sorted arr: \n", arr)


if __name__ == '__main__':
    main()