# Linear Search

```
def linear_search(list, target):
    for index, value in enumerate(list):
        if value == target:
            return index
    return -1
```

# Binary Search

In the previous videos we introduced two versions of binary search, an iterative and a recursive version. Code snippets for the iterative versions are provided below and match the explanation provided in the videos.

You will find the recursive version to be slightly different however. If you remember, when starting the recursive version of binary search I made one modification to the algorithm - instead of returning the index value, I returned True if the value was present in the list and False otherwise. There was a reason for that.

When we use list slices with recursive calls the index value returned, even with a successful search will always be 0. Each sublist created will have a new set of indexes and it becomes very difficult to track the relationship betwee the index of an item in the sublist and where that item existed in the original list.

In the worst case scenario, where it takes a log n + 1 number of splits to find the element we end up with a single element array. The target, at this point, will always be at index position 0 regardless of its index position in the original array.

While we were able to demonstrate how recursion worked and provide a recursive implementation of binary search, this is not a good implementation. For all the code snippets below I have provided the correct implementation for the recursive version of binary search.

It's not that much different and it might even seem familiar to you - it combines the techniques we used in both the iterative version and recursive version of binary search.

For an explanation of this version and some of its implications, read the Python section below. You should then be able to look for code snippets in the language of your choice understand what the code is doing.

## Iterative Binary Search
```
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

The way we've tackled the recursive version of binary serach is by using a combination of a recursive call and the iterative approach with start and end variables to keep track of the portion of the list we're searching.

```
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

It's important to keep in mind that this doesn't change the fact that Python has a maximum recursion depth and an iterative approach is still preferred.

