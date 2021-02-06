from math import ceil


def categories_split_in_two(queryset):
    '''
        Разделяем на две части чтобы постов было примерно поровну
        TODO: переписать попроще
    '''
    arr_one = []
    arr_two = []
    count_one = 0
    count_two = 0
    for item in queryset:
        if count_one <= count_two:
            arr_one.append(item)
            count_one += item.children.count()
        else:
            arr_two.append(item)
            count_two += item.children.count()
    return arr_one, arr_two


def parting(arr, parts):
    '''Разделяем массив на части'''
    part_len = ceil(len(arr)/parts)
    return [arr[part_len*k:part_len*(k+1)] for k in range(parts)]
