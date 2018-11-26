def find_partition(arbitary_list, partition_set1, sum1, sum2, pos):
    # If entire array is traversed, compare both the sums. 
    if pos == len(arbitary_list):
        if sum1 == sum2:
            return True
        else : 
            return False     
  
    # Add current element to set 1. 
    partition_set1.append(arbitary_list[pos]) 
  
    # Recursive call after adding current element to set 1. 
    res = find_partition(arbitary_list, partition_set1, sum1 + arbitary_list[pos], 
        sum2, pos + 1)
  
    # If this inclusion results in equal sum 
    # sets partition then return true
    if res:
        return res 
  
    # Removing current element from set1
    partition_set1.pop()

    # Recursive call after for back tracking
    return find_partition(arbitary_list, partition_set1, sum1,  
                     sum2 + arbitary_list[pos], pos + 1) 
  
def is_partitionable(arbitary_list):
    n = len(arbitary_list)
    total_sum = sum(arbitary_list)

    # If sum of list is odd, it can not be divided into 2 equal subset

    if total_sum % 2 == 1:
        return False

    partition_set1 = []

    return find_partition(arbitary_list, partition_set1, 0, 0, 0) 

if __name__ == "__main__"  :
    arbitary_list = [1, 11, 5, 5]
    arbitary_list = [12, 1, 5, 9, 3]
    if is_partitionable(arbitary_list) == True:
        print ("Can be partitionable as equal sum") 
    else: 
        print ("Can not be partitionable as equal sum")
