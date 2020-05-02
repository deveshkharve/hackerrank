"""
solution
https://www.hackerrank.com/challenges/crush/problem
difficulty: Hard, section: data structues

PROBLEM STATEMENT: Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value
to each of the array element between two given indices, inclusive. Once all operations have been performed,
return the maximum value in your array.

For example, the length of your array of zeros . Your list of queries is as follows:
    a b k
    1 5 3
    4 8 7
    6 9 1

Add the values of  between the indices  and  inclusive:
index->	 1 2 3  4  5 6 7 8 9 10
	    [0,0,0, 0, 0,0,0,0,0, 0]
	    [3,3,3, 3, 3,0,0,0,0, 0]
	    [3,3,3,10,10,7,7,7,0, 0]
	    [3,3,3,10,10,8,8,8,1, 0]
The largest value is  after all operations are performed.
"""


"""
Explaination:
In the classical approach we can manipulate the array by adding the query value k for all the elements between index [a,b].
After performing all the queries, we can then check the max value of the resultant array.
Above can be done in following way: 
    for query in queries:
        arr[query[0]-1: query[1]] = [ i + query[2] for i in arr[query[0]-1: query[1]] ]
    return max(arr)

however, the above logic fails for large values of n and queries

Alternate solution:
instead of updating all the values between the query range [a,b]. what we can do is save O(b-a) steps 
by maintaining a step and a fall value. i.e add the query value k to the base array value at the lower bound.
and a fall value at the upper bound of the query range.

          7|
 3|        |    
  |        |   -1|
  1--2--3--4--5--6--7--8--9--10
              |        |  |
            -3|        |  -1
                     -7|
   

 sum at the given position
    3  3  3  10 10 8  8  8  1  0           
    |  |  |  |  |  |  |  |  |  |
    1--2--3--4--5--6--7--8--9--10 
 
 max sum = 10

the above is a representation of how this process works.

"""

def arrayManipulation(n, queries):
    """
    manipulate the base array using the queries provided

    :param n: length of the base array
    :param queries: array of query
    :return: max value after all queries are executed
    """
    arr = [0] * n
    for i in queries:
        # add step value from where the query upper bound
        arr[i[0] - 1] += i[2]
        # handle the corner case, as for the last value, there is no point in reducing back the step value
        if i[1] != len(arr):
            # subtract the step value at the query lower bound
            arr[i[1]] -= i[2]

    max_sum = 0
    current_step_value = 0

    for q in arr:
        # check the step value at the index, considering both step and fall.
        current_step_value += q
        if current_step_value > max_sum:
            # update max sum if the new step value is greater than the old step
            max_sum = current_step_value

    return max_sum

length = 5
my_queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
arrayManipulation(length, my_queries)
