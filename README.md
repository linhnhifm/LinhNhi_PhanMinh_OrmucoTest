# LinhNhi_PhanMinh_OrmucoTest

The language used for all 3 questions is Python.
Comments have been used for two purposes:
* To clarify code and list down assumptions used to solve the question.
* To help read code more easily by explaining what the code is doing

## Question A
The main function used to answer the question is called "do_lines_overlap".
There are two helper functions used to check the validity of inputs.

Please note the assumptions used for answering this question (also included as a comment in the code):
1. A line (x1, x2) is only valid if the left endpoint x1 is less than or equal to the right endpoint x2. 
For example, (1,5) is a valid line because x1 = 1 is less than x2 = 5.
On the other hand, (5,1) is not a valid line because x1 = 5 is greater than x1 = 1.

2. Adjacent lines that share a same endpoint are considered overlapping lines. 
For example, (1,5) and (5,6) are overlapping lines because they both touch 5.

3. Lines with the same left and right endpoints are considered overlapping lines.
For example, (1,5) and (1,5) are two lines with the same left and right endpoints. They are considered overlapping lines.

4. A line (x1, x2) where x1 = x2 is also considered a line.
For example, (1,1) is a line. 

5. Lines can have negative endpoints. 
For example, (-5, -1) is a valid line.

## Question B
The library is named "checkversionstringlib".
The folder "checkversionstringlib" includes the file functions.py that contains the main function and helper functions used to solve this problem.
The main function is called "compare_version_strings".
There is a helper function to help validate that the input version strings are of the correct format.

The folder "tests" contain the unit tests written for this problem.

Please note the assumption used in this question is that a valid version string must contain only numbers (digits 0-9) separated by periods and no letters (also included as a comment in the code).

## Question C
The library is named "geo_dis_lru_cache".
The folder of the same name includes these 3 code files with the solution: node.py, lru_cache.py, and geo_distributed_cache_manager.py.
* node.py defines the class Node used to create the LRU cache
* lru_cache.py defines the different methods used to create the LRU cache. A doubly-linked list and hash map is used to construct the LRU cache. Please note, the left-most node is the Least Recently Used and the right-most node is the Most Recently Used (also included this comment in the code).
* geo_distributed_cache_manager.py defines the GeoDistributedCacheManager class that is used to handle a user's request for data by:
  * Determining the closest server to the user's IP address using a haversine formula calculation, or assign a default server if the user's location cannot be found
  * Fetch data from the data store if there is no data in cache
  * If data store also doesn't have data, then generate some data for the specific key

The folder "tests" contain 2 tests written for this problem. One test is for the LRU cache and the other test is for the GeoDistributedCacheManager.
