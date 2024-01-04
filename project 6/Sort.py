#Bobble_sort
def Bobble_Sort(list):
    n=len(list)
    for i in range(n):
        for j in range(n-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list


#selection-sort
def Selection_Sort(list):
    n=len(list)
    for i in range(n):
        minimum=i
        for j in range(i+1, n):
            if list[minimum]>list[j]:
                minimum=j
        list[i],list[minimum]=list[minimum],list[i]
    return list


#insertion_sort
def Insertion_Sort(list):
    n=len(list)
    for i in range(1,n):
        key=list[i]
        while list[i-1]>key and i>0:
            list[i] , list[i-1]=list[i-1],list[i]
            i=i-1
    return list


#merge_sort
def Merge_Sort(list):
    if len(list)>1:
        left_list=list[:len(list)//2]
        right_list=list[len(list)//2:]

        Merge_Sort(left_list)
        Merge_Sort(right_list)

        i=0 #left-list index
        j=0 #right_list index
        k=0 #merged list index

        while i<len(left_list)and j<len(right_list):
            if left_list[i]<right_list[j]:
                list[k]=left_list[i]
                i+=1
            else:
                list[k]=right_list[j]
                j+=1
            k+=1

        while i<len(left_list):
            list[k]=left_list[i]
            i+=1
            k+=1
        
        while j<len(right_list):
            list[k]=right_list[j]
            j+=1
            k+=1

    return list


#quick_sort
def quick_sort(arr , left , right):
    if left < right:
        partition_pos = partition(arr , left , right)
        quick_sort(arr,left, partition_pos-1)
        quick_sort(arr, partition_pos+1 , right)

def partition(arr, left,right):
    i=left
    j=right -1
    pivot = arr[right]

    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[right],arr[i]
    if arr[i]> pivot:
        arr[i],arr[right]=arr[right],arr[i]
    
    return i


#count_sort
def count_sort(array):
    # Finding the maximum element of input_array.
    maximum = max(array)
 
    # Initializing count_array with 0
    count_array = [0] * (maximum + 1)
 
   
    for num in array:
        count_array[num] += 1
 
    
    for i in range(1, maximum + 1):
        count_array[i] += count_array[i - 1]
 
    # Creating output_array from count_array
    output_array = [0] * len(array)
 
    for i in range(len(array) - 1, -1, -1):
        output_array[count_array[array[i]] - 1] = array[i]
        count_array[array[i]] -= 1
 
    return output_array

#buket_sort
def bucketSort(x):
    arr = []
    slot_num = 10  # 10 means 10 slots, each
    
    for i in range(slot_num):
        arr.append([])
 
    
    for j in x:
        index_arr = int(slot_num * j)
        arr[index_arr].append(j)
 
    
    for i in range(slot_num):
        arr[i] = Insertion_Sort(arr[i])
 
   
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x




# def run_sorting_method(method_name, input_list):
#     valid_methods = ["bubble_sort", "selection_sort", "insertion_sort", "merge_sort", "quick_sort", "count_sort", "bucket_sort"]
#     if method_name not in valid_methods:
#         print("نام متد نامعتبر است.")
#         return None


#     if method_name == "bubble_sort":
#         return Bobble_Sort(input_list.copy())
#     elif method_name == "selection_sort":
#         return Selection_Sort(input_list.copy())
#     elif method_name == "insertion_sort":
#         return Insertion_Sort(input_list.copy())
#     elif method_name == "merge_sort":
#         return Merge_Sort(input_list.copy())
#     elif method_name == "quick_sort":
#         result_quick_sort = input_list.copy()
#         quick_sort(result_quick_sort, 0, len(result_quick_sort) - 1)
#         return result_quick_sort
#     elif method_name == "count_sort":
#         return count_sort(input_list.copy())
#     elif method_name == "bucket_sort":
#         return bucketSort(input_list.copy())



# method_name = "bubble_sort"
# input_list = [64, 25, 12, 22, 11]
# result = run_sorting_method(method_name, input_list)
# print(f"{method_name.capitalize()} Result:", result)


# method_name = "selection_sort"
# input_list = [38, 27, 43, 3, 9, 82, 10]
# result = run_sorting_method(method_name, input_list)
# print(f"{method_name.capitalize()} Result:", result)


# method_name = "merge_sort"
# input_list = [12, 11, 13, 5, 6, 7]
# result = run_sorting_method(method_name, input_list)
# print(f"{method_name.capitalize()} Result:", result)

