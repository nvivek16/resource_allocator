# resource_allocator

1) Clone the repository

2) You can modify test.py to change the input params and to look out at few examples

3) For option 1, print combination of servers that have minimum X CPUS. Output will be a list of dict that has minimum X cpus sorted based on total cost in asc order 

4) For option 2, print combination of servers that doesnot sum up above the given price cap. Output will have additional param <b> total cpus </b> for giving better insights. It will be sorted based on total cpus in desc order

5) For option 3(Combination 1 and 2). Output will have additional param <b> total cpus </b> and will be sorted in <b> asc order based on total price </b>

6) For option 2 and 3, output will contain as many possible servers that is <= given price cap. The output will not contain two server combinations with same prefix combination

For eg.,

If there is possible combination (server 1, server 2, server 3) that is less than or equal to the given price cap, (server 1, server 2) combination will not be added to the output list
