IRINCO, ANGEL ANN B. BSIT-2A 

Analysis - Activity 5: Stacks and Queues


 1. Stack Implementations Comparison

a. Array Stack
• Advantage:Simple, cache-friendly, O(1) push/pop.
• Disadvantage: Fixed capacity, needs resizing, can cause Overflow.
• Time Complexity: Push/Pop/Peek = O(1)

b. Linked Stack
• Advantage: Dynamic size, never full (unless memory full), no overflow.
• Disadvantage: Extra memory for pointers, not cache-friendly.
• Why push at head? 
  Answer: Because inserting at head is O(1). If we push at tail, we need to traverse O(n) to find the tail (if no tail pointer). So head insertion is the most efficient for Stack (LIFO).

 2. Queue Implementations Comparison

a. Array Queue (Circular Queue)
• Why Circular? 
  Answer: A normal linear array queue suffers from false overflow. Example: front is at index 2, rear is at last index, queue looks full but there is free space at 0 and 1. Circular queue solves this by using modulo `(rear+1) % capacity` to wrap around and reuse space. This is efficient O(1).

b. Linked Queue
• Advantage: Dynamic size, no false overflow.
• Why enqueue at tail and dequeue at head?
  Answer: Queue is FIFO. The first inserted should be first removed. So we maintain both head and tail pointers: enqueue at tail O(1) and dequeue at head O(1).

 3. Applications

a. Balanced Parentheses Checker
• Uses Stack. When we see opening brackets `({[`, we push. When we see closing `)}]`, we pop and check if it matches. If stack is empty at the end, it is balanced. This works because of LIFO nature of Stack.

b. Print Queue Simulation
• Uses Queue. Print jobs should be printed in order they arrived (First Come First Serve). So Queue (FIFO) is the correct data structure.

c. Conclusion
• Use Array implementation if max size is known and speed is priority.
• Use Linked implementation if size is unknown and flexibility is needed.
