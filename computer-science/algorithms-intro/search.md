# Linear Search

```Python
def linear_search(list, target):
    for index, value in enumerate(list):
        if value == target:
            return index
    return -1
```

# Binary Search

recursive binary search, instead of returning the index value, returns True if the value was present in the list and False otherwise. reason: 

> When we use list slices with recursive calls the index value returned, even with a successful search will always be 0. Each sublist created will have a new set of indexes and it becomes very difficult to track the relationship betwee the index of an item in the sublist and where that item existed in the original list. In the worst case scenario, where it takes a log n + 1 number of splits to find the element we end up with a single element array. The target, at this point, will always be at index position 0 regardless of its index position in the original array.

## Iterative Binary Search
```Python
def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
    return -1
```

## Recursive Binary Search

Because Python has a maximum recursion depth, an iterative approach is preferred. This is using a combination of a recursive call and the iterative approach with start and end variables to keep track of the portion of the list we're searching.

```Python
def recursive_binary_search(list, target, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_binary_search(list, target, start, mid-1)
        else:
            return recursive_binary_search(list, target, mid+1, end)
```

The function has been modified to accept a start and end position with default values of 0 and None respectively. The default values allow us to pass a list and target without needing to specify the arguments when invoking the function. Inside the body we set the appropriate values like we did when setting first and last in the iterative approach.

We then use start and end like we did in the iterative approach to keep track of the slice of the list we're searching through. The big difference here is that with each recursive call, by passing in different values for start and end we can define the slice of the list we're searching through. We're not actually executing a slice operation and we use only one list in memory, but each recursive call now focuses on a smaller slice of the original list.

This definitely has implications for the runtime of our code. One point that was not covered in the course was the cost of the slice operation used in the recursive version of the function. A slicing operation is not a constant time operation and has a runtime of O(k) where k represents the size of the slice.

With the modified (and correct) version of recursive binary search, since we're not executing slicing operations we've eliminated that cost and our code now reflects the accurate runtime of the binary search algorithm at O(log n).

Slicing is also what lends to a space complexity of O(log n) for the original recursive version since each slice required additional storage. Since we're not slicing the lsit anymore, the space complexity is now constant - no additional storage is used.

Source: [Intro to Algorithms, Treehouse](https://teamtreehouse.com/library/introduction-to-algorithms/algorithms-in-code/binary-search-implementations)


#### Tail call 
A call, inside a function, to the same function itself as the last operation. Also called tail recursion

###Resources

[Wikipedia: Tail call](https://en.wikipedia.org/wiki/Tail_call)

[Stack Overflow: What Is Tail Call Optimization?](https://stackoverflow.com/a/310980/1071846)
