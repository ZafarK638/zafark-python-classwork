import _collections_abc

class natural(_collections_abc.Iterable):
    def __init__(self):
        self.val=0
    def __next__(self):
        self.val += 1
        return self.val
    