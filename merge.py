def merge(str_list, add_str, remove_str):
    for i in add_str:
        if i not in str_list:
            str_list.append(i)

    for i in remove_str:
        if i in str_list:
            str_list.remove(i)

    sorted_list = len_sort(str_list)
    return sorted_list
    

def len_sort(str_list):
    n = len(str_list)
    for i in range(n):
        for j in range(i+1,n):
            if len(str_list[i]) < len(str_list[j]):
                temp = str_list[i]
                str_list[i] = str_list[j]
                str_list[j] = temp

            elif len(str_list[i]) == len(str_list[j]):
                temp = min(str_list[i].lower(), str_list[j].lower())
                str_list[i] = max(str_list[i].lower(), str_list[j].lower())
                str_list[j] = temp
    return str_list



def main():
    str_list = []
    add_str = []
    remove_str = []
    
    n_str_list = int(input("Enter the # of elements in your original list: "))
    for i in range(0, n_str_list):
        element = str(input())
        str_list.append(element)

    n_add_str = int(input("Enter the # of elements in your list of elements to add: "))
    for i in range(0, n_add_str):
        element = str(input())
        add_str.append(element)

    n_remove_str = int(input("Enter the # of elements in your list of elements to remove: "))
    for i in range(0, n_remove_str):
        element = str(input())
        remove_str.append(element)

    print(merge(str_list, add_str, remove_str))
    return 

main()
