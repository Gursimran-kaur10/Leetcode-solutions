class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = [0] * k
        self.k = k
        self.front = 0
        self.rear = 0
        self.size = 0

    def enQueue(self, value):
        # Queue is full
        if self.isFull():
            return False

        # Insert at rear
        self.queue[self.rear] = value

        # Move rear circularly
        self.rear = (self.rear + 1) % self.k

        self.size += 1

        return True

    def deQueue(self):
        # Queue is empty
        if self.isEmpty():
            return False

        # Remove front element
        self.front = (self.front + 1) % self.k

        self.size -= 1

        return True

    def Front(self):
        if self.isEmpty():
            return -1

        return self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1

        # rear points to next empty position,
        # so actual last element is one position behind
        index = (self.rear - 1) % self.k
        return self.queue[index]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k
