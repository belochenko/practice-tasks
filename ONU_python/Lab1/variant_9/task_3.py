#you can try to change data in array to check if this solution is right
x = [[1, 1, 1, 1, 1],
     [0, 1, 2, 3, 4],
     [0, 2, 3, 5, 0],
     [5, 4, 3, 2, 1],
     [0, 0, 0, 0, 0]]


#this function returns line number and length of sequences
#in input we pass the array
def best_sequence_length(arr):
    arr_length = len(arr)
    if arr_length <= 1:
        return arr_length

    longest = [1]           
    best_idx_at_all = 0

    for idx in range(1, arr_length):
        best_len_now = 1            
        back = -1
        for i in range(len(longest)+1):
            if arr[i] < arr[idx] and best_len_now <= longest[i]:
                best_len_now = longest[i] + 1
                back = i

        longest.append(longest[back]+1 if back > -1 else 1)
        if longest[best_idx_at_all] < longest[idx]:
            best_idx_at_all = idx

    return longest[best_idx_at_all]


lenght_of_chain = [best_sequence_length(row) for row in x]

line_index = lenght_of_chain.index(max(lenght_of_chain))
line_length = max(lenght_of_chain)


print(f"Index of the line with the biggest chain of numbers, which is in ascending order, is: {line_index}")
print(f"Length of this chain is: {line_length}")