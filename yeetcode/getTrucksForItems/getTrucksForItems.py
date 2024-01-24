"""Given an array, trucks of n integers that represents the capacities of different trucks and an array, items, of m integers that represent the weight of different items for each item, find the index of the smallest truck which has a capacity greater than the items weight. If there are multiple such trucks, choose the one with the minimum index. If there is no truck that can carry the item, report -1. 

Note: Assume that the trucks are indexed starting from 0. Also, multiple items can be mapped to the same truck. Each item is mapped independently, hence the trucks do not lose any capacity when a particular item is mapped to it

Complete the function getTrucksForItems, it has following parameters int trucks[n], int items[q] 
Sample input, 
trucks = [5,3,8,1] items = [6,10] 
Output = [2, -1] 

sample input 2
trucks = [1,3,5,2,3,2] 
items = [1,2,3] 
Output = [3,1,2] 
items[0] = 1,2 is the smallest value in the array greater than 1. trucks[3] and trucks[5] are equal to 2. The minimum index among them is 3
items[1] = 2, 3 is the smallest value in the array greater than 2. trucks[1] and trucks[4] are equal to 3. The minimum index among them is 1.

Sample input 3
Trucks = [4,5,7,2] 
Items = [1,2,5] 
Output = [3,0,2]
The smallest truck that can carry the third weight 5, is truck 2 with a capacity of 7. Similar logic is applied to other elements and the answer is [3,0,2]  
"""
def getTrucksForItemsFurtherOptimized(trucks, items):
    # Create a list of truck indices sorted by their capacities
    sorted_indices = sorted(range(len(trucks)), key=lambda i: trucks[i])

    result = []
    for item in items:
        # Binary search to find the minimum truck capacity that exceeds the item's weight
        left, right = 0, len(sorted_indices) - 1
        min_index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if trucks[sorted_indices[mid]] > item:
                min_index = sorted_indices[mid]
                right = mid - 1  # Look for a smaller index
            else:
                left = mid + 1

        result.append(min_index)
    return result

# Re-test the further optimized function with the provided examples
trucks1 = [5, 3, 8, 1] 
items1 = [6, 10]
trucks2 = [1, 3, 5, 2, 3, 2]
items2 = [1, 2, 3]
trucks3 = [4, 5, 7, 2] 
items3 = [1, 2, 5]
further_optimized_output1 = getTrucksForItemsFurtherOptimized(trucks1, items1)
further_optimized_output2 = getTrucksForItemsFurtherOptimized(trucks2, items2)
further_optimized_output3 = getTrucksForItemsFurtherOptimized(trucks3, items3)

print(further_optimized_output1, further_optimized_output2, further_optimized_output3)


