class ListQueue:
    def __init__(self):
        self.queue_list = []

    def enqueue(self, new_value):
        self.queue_list.append(new_value)

    def dequeue(self):
        return self.queue_list.pop(0)

    def get_size(self):
        return len(self.queue_list)