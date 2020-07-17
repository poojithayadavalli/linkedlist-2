# Linkedlist

Raghav is a trader and he buys and sells products. He buys two consecutive products at a time from the available products.

He is provided with the list of profits that he gain after buying an item in that position.He doesn't want to buy products that gives loss.

You are given with the linked-list of prices of products. So you have to repeatedly delete consecutive sequences of nodes that sum to value less than or equal to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer

Example 1:

Input: 
1 2 -3 3 1

Output:
3 1

Example 2:

Input:
1 2 3 -3 4

Output: 
1 2 4

Example 3:

Input:
1 2 3 -3 -2

Output: 
1
