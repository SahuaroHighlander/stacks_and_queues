# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         Tara Haller
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue
import math

# generate & return a queue of binary number strings from 1 to N
# front of queue begins @ '1', returns empty Queue otherwise
def generate_binary_numbers(N):
    numbers = Queue([])
    ret_numbers = Queue([])
    numbers.enq("1")
    
    while N > 0:
        N -= 1
        first = numbers.deq()
        ret_numbers.enq(first)
        second = first
        numbers.enq(first + "0")
        numbers.enq(second+ "1")
        
        
    return ret_numbers




def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()


# Don't run main on import
if __name__ == "__main__":
    main()

