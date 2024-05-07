# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Tara Haller
# ASSIGNMENT:   Project 2: Stacks & Queues

from Stack import Stack
from Queue import Queue

# Returns True if the braces match,
# & False otherwise
def matcher(word):
#create an empty stack
    grab = Stack([])
    check = Stack([])
    matched = ["()", "{}", "[]"]
    open = ['[', '(']
    closed = [']',')']
    #if everything is a letter
    for letter in word:
        if letter in '[({})]':
            grab.push(letter)
    if grab.is_empty() == True:
        return True
    while grab.is_empty() == False:
        while grab.peek() in closed:
            check.push(grab.pop())
        if check.is_empty():
            return False
        if grab.peek() in open:
            one = check.pop()
            two = grab.pop()
            if two + one not in matched:
                return False
    return True

def main():
    print("matcher: ", matcher("[("))
    print("matcher: ", matcher("[()]"))
    print("matcher: ", matcher("hello"))
# Don't run main on import
if __name__ == "__main__":
    main()

