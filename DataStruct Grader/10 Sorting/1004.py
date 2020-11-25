def insertion_sort(lst):
    for i in range(1, len(lst)):
        value = lst[i]
        for j in range(i, -1, -1):
            if value < lst[j-1] and j > 0:
                lst[j] = lst[j-1]
            else:
                lst[j] = value
                break
    return lst

def get_median(sorted_list):
    length = len(sorted_list)
    if length % 2 == 0:
        return (sorted_list[length // 2 - 1] + sorted_list[length // 2])/2
    else:
        return sorted_list[length // 2]

lst = [e for e in input("Enter Input : ").split()]
if lst[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    lst=list(map(int, lst))
    sorting = []
    temp = []
    for item in lst:
        sorting.append(item)
        temp.append(item)
        insertion_sort(sorting)
        print(f"list = {temp} : median = {get_median(sorting):.1f}")