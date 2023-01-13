def count(list, value):
    end = findend(list, value)
    start = findstart(list, value)
    if end != -1 and start != -1:
        return(end - start + 1)
    else:
        return 0


def findstart(list, value):
    start = 0
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if value == list[mid]:
            high = mid -1
            start = mid     
        elif value < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if list[start] == value:
        return start
    else:
        return -1




def findend(list, value):
    end = 0
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if value == list[mid]:
            low = mid + 1
            end = mid         
        elif value < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if list[end] == value:
        return end
    else:
        return -1


"""
time complexity of this binarycount:
1. find the start: assume the list has n elements, we keep divide the list and search half side of it till the elements number less than 2, so T = O(logn)
2. find the end: same as find the start
3. count: O(1)
so the time complexity of this binary count is O(logn) + O(logn) + O(1) -> O(logn)

binary search count vs. built-in list count
1.  the base case 
    case #0    
        X: range [1, 250,000), size 2,500 
        Y: range [1, 250,000), size 50,000

        Linear Search: 0.6742978096008301 seconds
        Binary Search: 0.1482839584350586 seconds

2. change the size of X(Keep the number of items in Y the same as 25000):
    case #1 -> smaller list
        X: range [1, 250,000), size 500 
        Y: range [1, 250,000), size 50,000 
        
        Linear Search: 0.14248895645141602 seconds
        Binary Search: 0.11556410789489746 seconds
    
    case #2 -> smaller list
        X: range [1, 250,000), size 250
        Y: range [1, 250,000), size 50,000
        
        Linear Search: 0.07215571403503418 seconds
        Binary Search: 0.09877300262451172 seconds
    
    case #3 -> longer list
        X: range [1, 250,000), size 25,000 
        Y: range [1, 250,000), size 50,000
        
        Linear Search: 7.635131120681763 seconds
        Binary Search: 0.19052696228027344 seconds

3. change the range of the numbers added to X (Keep the size of X as 2500 and keep the number of items in Y the same as 25000)
    case #4 -> more duplicate
        X: range [1, 2,500), size 2,500
        Y: range [1, 250,000), size 50,000
        
        Linear Search: 0.6790709495544434 seconds
        Binary Search: 0.14775705337524414 seconds

    case #4 -> less duplicate   
        X: range [1, 25,000,000), size 2,500 
        Y: range [1, 250,000), size 50,000 
        
        Linear Search: 0.6765408515930176 seconds
        Binary Search: 0.13283991813659668 seconds

4. change the proportion of Y in X
    case #5 -> less duplicate 
        X: range [1, 250,000), size 2,500
        Y: range [240,000, 2,500,000), size 50,000
        
        Linear Search: 0.6927380561828613 seconds
        Binary Search: 0.14849400520324707 seconds

run time complexity analyze:

results summary:
case	X size	    X range	            Y size	    Y range	                Linear Search	vs. base case	Binary Search	vs. base case
0	    2,500	    [1,250,000) 	    50,000	    [1,250,000)	            0.67430	        -	            0.14828	        -
1	    500	        [1,250,000) 	    50,000	    [1,250,000)	            0.14249	        -78.87%	        0.11556	        -22.07%
2	    250	        [1,250,000) 	    50,000	    [1,250,000)	            0.07216	        -89.30%	        0.09877	        -33.39%
3	    25,000	    [1,250,000) 	    50,000	    [1,250,000)	            7.63513	        1032.31%	    0.19053	        28.49%
4	    2,500	    [1,2,500) 	        50,000	    [1,250,000)	            0.67907	        0.71%	        0.14776	        -0.36%
5	    2,500	    [1,25,000,000) 	    50,000	    [1,250,000)	            0.67654	        0.33%	        0.13284	        -10.42%
6	    2,500	    [1,250,000) 	    50,000	    [240,000,2,500,000)	    0.69274	        2.73%	        0.14849	        0.14%

T(linear search) = O(n)
T(binary search) = O(logn)

base on this:
    1. the only factor that will distinctly change the run time of both fuction is the size of X;
    2. the time change of linear search is much bigger than binary search.
which is also true according to the table above

"""