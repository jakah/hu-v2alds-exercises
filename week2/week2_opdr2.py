class mystack(list):

    """Summary

    Attributes:
        position (int): The first position were a new item can be placed. 
        stack (list): A list with all elements on the stack.
    """

    def __init__(self):
        """Create a stack with an empty list and the position set to 0.
        """
        self.stack = []

    def push(self, item):
        """Summary

        Args:
            item (any type): The item that will be placed on the stack.
        """
        self.stack.append(item)

    def pop(self):
        """Return the last item placed on the stack. It also removes it from the stack.
        IndexError when trying to pop form empty stack.

        Returns:
            any: Item last placed on the stack. 
        """

        return self.stack.pop()

    def peek(self):
        """Get the last item placed on the stack, without removing it. 
            IndexError when trying to pop form empty stack.
        Returns:
            any: Item last placed on the stack. 
        """
        return self.stack[-1]

    def isEmpty(self):
        """Check if stack is empty

        Returns:
            boolean: True on empty stack, False when stack is not empty.
        """
        return not self.stack


customstack = mystack()

if __name__ == '__main__':
    customstack.push("Q")
    customstack.push("z")
    print(customstack.pop())
    print(customstack.peek())
    customstack.pop()
    customstack.peek()
    print(customstack.isEmpty())
