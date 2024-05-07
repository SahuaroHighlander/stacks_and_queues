# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         Tara Haller
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty

def count_longest(q):
    leng = 0
    max_list = []
    if q.is_empty() or q.size() == 1:
        return q.size()
    prev=q.deq()
    leng = 1
    max = 0
    while(q.is_empty()==False):
        if prev == q.front():
            leng +=1
            prev = q.deq()
            if leng > max:
                max = leng
        else:
            prev = q.deq()
            leng = 1
        
    leng = max
    return leng

def main():
    print(Queue([l for l in "m" * 5]))
    print("out 2:", count_longest(Queue([l for l in "hello"])))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee" ])))


# Don't run main on import
if __name__ == "__main__":
    main()

