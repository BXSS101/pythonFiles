def drome(lst):
    is_des = True
    is_asc = True
    is_unique = True
    is_same = True
    unique_lst = []
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            is_des = False
        if lst[i] > lst[i+1]:
            is_asc = False
        if lst[i] in unique_lst:
            is_unique = False
        if lst[i] != lst[i+1]:
            is_same = False
        unique_lst.append(lst[i])
    if lst[len(lst)-1] in unique_lst:
        is_unique = False

    if is_same:
        return "Repdrome"
    elif is_asc and is_unique:
        return "Metadrome"
    elif is_asc and not is_unique:
        return "Plaindrome"
    elif is_des and is_unique:
        return "Katadrome"
    elif is_des and not is_unique:
        return "Nialpdrome"
    else:
        return "Nondrome"
in_lst = list(map(int, input("Enter Input : ")))
print(drome(in_lst))