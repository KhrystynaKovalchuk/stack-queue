"""
Queue to stack converter.
"""


import copy

from arraystack import ArrayStack


def queue_to_stack(queue):
    """
    Convert queue to stack.
    """
    copy_queue = copy.deepcopy(queue)
    staack = []
    while not copy_queue.isEmpty():
        staack.append(copy_queue.pop())
    while len(staack) != 0:
        copy_queue.add(staack[-1])
        del staack[-1]
    stack = ArrayStack()
    while not copy_queue.isEmpty():
        item = copy_queue.pop()
        stack.push(item)
    return stack
