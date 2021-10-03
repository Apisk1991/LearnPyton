def find_min_el(array):
    for element in array:
        for element2 in array:
            if element < element2:
                min_elem = element
    return min_elem



print(find_min_el([5, 4, 3, 2, 1, 6]))