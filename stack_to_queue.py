"""
Stack to queue converter.
"""

import copy

from arrayqueue import ArrayQueue


def stack_to_queue(stack):
    """
    Convert stack to queue.
    """
    copy_stack = copy.deepcopy(stack)
    queue = ArrayQueue()
    while not copy_stack.isEmpty():
        item = copy_stack.pop()
        queue.add(item)
    return queue
