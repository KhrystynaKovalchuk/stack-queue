# stack-queue
Modules to convert Stack to Queue and vice versa.
## usage
```python
>>> queue = ArrayQueue()
>>> for i in range(10):
        queue.add(i)
>>> stack = queue_to_stack(queue)
>>> print(queue)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(stack)
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> print(stack.pop())
0
>>> print(queue.pop())
0
>>> stack.add(11)
>>> queue.add(11)
>>> print(queue)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
>>> print(stack)
[9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
```
```python 
>>> stack = ArrayStack()
>>> for i in range(10):
        stack.add(i)
>>> queue = stack_to_queue(stack)
>>> print(queue)
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> print(stack)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(stack.pop())
9
>>> print(queue.pop())
9
>>> stack.add(11)
>>> queue.add(11)
>>> print(queue)
[8, 7, 6, 5, 4, 3, 2, 1, 0, 11]
>>> print(stack)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 11]
```
