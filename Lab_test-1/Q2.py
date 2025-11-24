import collections

class Queue:
    """
    A simple Queue class implementation using collections.deque for efficiency.
    Provides enqueue, dequeue, and peek operations.
    """
    def __init__(self):
        """Initializes an empty queue."""
        self._items = collections.deque()

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise."""
        return not self._items

    def enqueue(self, item):
        """Adds an item to the end of the queue."""
        self._items.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        item = self._items.popleft()
        return item

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek into an empty queue.")
        return self._items[0]

    def __str__(self):
        """String representation of the queue."""
        return f"Queue: {list(self._items)}"

# --- Testing Scenarios ---
def run_queue_tests():
    """
    Tests the Queue class with multiple scenarios, including edge cases.
    """
    print("--- Starting Queue Tests ---")
    q = Queue()
    
    # 1. Test basic enqueue and peek
    print("\n--- Scenario 1: Basic Enqueue and Peek ---")
    q.enqueue(10)
    print(f"Enqueued: 10")
    q.enqueue(20)
    print(f"Enqueued: 20")
    print(q)
    print(f"Peek: {q.peek()}") # Should be 10

    # 2. Test dequeue
    print("\n--- Scenario 2: Dequeue ---")
    item = q.dequeue()
    print(f"Item returned from dequeue: {item}")
    print(q)
    print(f"Peek after dequeue: {q.peek()}") # Should be 20

    # 3. Test dequeuing until empty
    print("\n--- Scenario 3: Dequeue until empty ---")
    q.dequeue() # Dequeues 20
    print(f"Dequeued item. Is queue empty? {q.is_empty()}")

    # 4. Test edge cases: dequeue and peek on an empty queue
    print("\n--- Scenario 4: Edge Cases (Empty Queue) ---")
    try:
        q.dequeue()
    except IndexError as e:
        print(f"Successfully caught expected error: {e}")
    try:
        q.peek()
    except IndexError as e:
        print(f"Successfully caught expected error: {e}")

    print("\n--- All tests completed. ---")

if __name__ == "__main__":
    run_queue_tests()
