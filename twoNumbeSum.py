# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    # Write your code here.
    
    arr = {}
    for i in range(len(array)):
        key = array[i]
        if key in arr:
            return [key,arr[key]]
        arr[targetSum-array[i]]=array[i]

    return []