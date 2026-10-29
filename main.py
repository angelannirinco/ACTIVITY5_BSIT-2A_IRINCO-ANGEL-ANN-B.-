from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue

def test_balanced():
    print("\n--- Balanced Parentheses Checker ---")
    s = input("Enter ex: ({[]}): ")
    stack = ArrayStack(len(s))
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or stack.pop() != mapping[char]:
                print(f"Result: {s} is NOT BALANCED")
                return
    print(f"Result: {s} is {'BALANCED' if stack.is_empty() else 'NOT BALANCED'}")

def test_print_queue():
    print("\n--- Print Queue Simulation ---")
    q = LinkedQueue()
    q.enqueue("Job1-5pages")
    q.enqueue("Job2-2pages")
    q.enqueue("Job3-10pages")
    q.display()
    while not q.is_empty():
        print(f"Printing {q.dequeue()}")
    q.display()


print("1.ArrayStack 2.LinkedStack 3.ArrayQueue 4.LinkedQueue 5.Applications 6.Overflow/Underflow test")
choice = input("Enter choice: ")

if choice == '1':
    st = ArrayStack(3)
    st.push("A"); st.push("B"); st.display()
    print("pop:", st.pop()); st.display()
elif choice == '3':
    q = ArrayQueue(3)
    q.enqueue("A"); q.enqueue("B"); q.enqueue("C"); q.display()
    print("dequeue:", q.dequeue()); q.display()
    q.enqueue("D"); q.display() # wrap-around demo
    print("Overflow test:")
    try: q.enqueue("E")
    except Exception as e: print(e)
elif choice == '5':
    test_balanced()
    test_print_queue()
elif choice == '6':
    st = ArrayStack(2)
    try: st.pop()
    except Exception as e: print("Caught Underflow:", e)
    try: st.push(1); st.push(2); st.push(3)
    except Exception as e: print("Caught Overflow:", e)
else:
    print("Run main.py again and choose")
