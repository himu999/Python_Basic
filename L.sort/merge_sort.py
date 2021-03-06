def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_list(left, right)


def merge_two_sorted_list(a, b):
    c = []
    len_a = len(a)
    len_b = len(b)

    i = j = 0

    while len_a > i and len_b > j:
        if a[i] <= b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j += 1

    while i < len_a:
        c.append(a[i])
        i = i + 1

    while j < len_b:
        c.append(b[j])
        j = j + 1

    return c


if __name__ == "__main__":

    z = [45, 5, 56, 78, +9, -9, 78, 565, 000, 258]
    print(merge_sort(z))
