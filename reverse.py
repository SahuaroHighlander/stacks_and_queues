# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Tara Haller
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue
from Stack import Stack
def flip(stack):
    rev_stack = Stack([])
    while stack.is_empty() == False:
        item = stack.pop()
        rev_stack.push(item)
    return rev_stack

#flip(Stack([1,2,3,4])).print()

# Return a new queue in reverse order
# Hint: can use a stack to help
def reverse(q_orig):
    q_new = Queue([])
    n_stack = Stack([])
    
    if q_orig.size() == 0 or q_orig.size() == 1:
        return q_orig
    
    while q_orig.is_empty() == False:
        n_stack.push(q_orig.deq())
        
    q_new=flip(n_stack)
    return q_new

def main():
    q = Queue(list(range(1, 5)))
    q.print()
    print("reverse: ", end="")
    reverse(q).print()

# Don't run main on import
if __name__ == "__main__":
    main()
