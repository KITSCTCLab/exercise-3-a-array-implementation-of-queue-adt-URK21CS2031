class Solution:
    """This class implements a linear queue.
    Attributes:
       stack: A list which maintains the content of stack.
       queue: A list which maintains the content of queue.
       top: An integer which denotes the index of the element at the top of the stack.
       front: An integer which denotes the index of the element at the front of the queue.
       rear: An integer which denotes the index of the element at the rear of the queue.
       size: An integer which represents the size of stack and queue.
"""

# Write your code here
def __init__(self, size):

    """Inits Solution with stack, queue, size, top, front and rear.
    Arguments:
    size: An integer to set the size of stack and queue.
"""
    self.stack = [None]*size
    self.queue = [None]*size
    self.size = size
    self.top = -1
    self.rear = -1
    self.front = -1

def is__stack__empty(self):
"""
    Check whether the stack is empty.
    Returns:
    True if it is empty, else returns False.
"""
return self.top==-1

def is__queue__empty(self):
"""
    Check whether the queue is empty.
    Returns:
    True if it is empty, else returns False.
"""
return self.rear<self.front

def is__stack__full(self):
"""
    Check whether the stack is full.
    Returns:
    True if it is full, else returns False.
"""
return self.top==(self.size-1)

def is__queue__full(self):
"""
    Check whether the queue is full.
    Returns:
    True if it is full, else returns False.
"""
return self.rear==(self.size-1)

def push__character(self, character):
"""
    Push the character to stack, if stack is not full.
    Arguments:
    character: A character that will be pushed to the stack.
"""
    if self.is__stack__full()==False:

    self.top+=1
    self.stack[self.top]=character

def enqueue__character(self, character):
"""
    Enqueue the character to queue, if queue is not full.
    Arguments:
    character: A character that will be enqueued to queue.
"""
    if self.is__queue__full()==False:
    if self.front==-1:
    self.front=0
    self.rear+=1
    self.queue[self.rear]=character

def pop__character(self):
"""
    Do pop operations if the stack is not empty.
    Returns:
    The data that is popped out if the stack is not empty.
"""
    if self.is__stack__empty()==False:
    x=self.stack[self.top]
    self.top-=1
    return x

def dequeue__character(self):
"""
    Do dequeue operations if the queue is not empty.
    Returns:
    The data that is dequeued if the queue is not empty.
"""
    if self.is__queue__empty()==False:
    x=self.queue[self.front]
    if self.front==self.rear:
    self.front=-1
    self.rear=-1
    else:
    self.front+=1
    return x
    # read the string text
    text = input()

    # find the length of text
    length__of__text = len(text)

    # Create the Solution class object
    solution = Solution(length__of__text)

    # push/enqueue all the characters of string text to stack
    for index in range(length__of__text):
    solution.push_character(text[index])
    solution.enqueue_character(text[index])

    is_palindrome = True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both characters
    If the comparison fails, set is_palindrome as False.
    '''

    for i in range(int(length__of__text/2)):
    if(solution.pop_character()!=solution.dequeue_character()):
    is_palindrome=False

    # finally print whether string text is palindrome or not.
    if is__palindrome:
    print("The word, " + text + ", is a palindrome.")
    else:
    print("The word, " + text + ", is not a palindrome.")
