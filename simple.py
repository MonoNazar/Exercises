def nails():
    # цвяхи
    l = int(input())
    rec = input()
    first_list = rec.split()
    first_list = [int(x) for x in first_list]
    first_list.sort()
    checker = True
    index = 1
    default_lenght = first_list[1] - first_list[0] + first_list[-1] - first_list[-2]
    for x in range(2, len(first_list) - 2):
        if first_list[x] - first_list[x-1] >= first_list[x+1] - first_list[x]:
            if not checker:
                checker = True
                index = 0
            elif first_list[x] == first_list[-3]:
                break
            if index == 2:
                index = 0
                default_lenght -= first_list[x] - first_list[x-1]
            default_lenght += first_list[x+1] - first_list[x]
            index += 1
        else:
            if checker:
                checker = False
                index = 0
                if x != 2:
                    continue
            if index == 2:
                index = 0
                default_lenght -= first_list[x-1] - first_list[x-2]
            default_lenght += first_list[x] - first_list[x-1]
            index += 1
    return default_lenght

pass
