class MyArray:
    collection = [None] * 15

    def main_func(self, lst):
        if len(lst) > len(self.collection):
            for i in range(round(0.3 * len(self.collection))):
                self.collection.extend([None])

    def c_append(self, data):
        count = 0
        for i in self.collection:
            if i is not None:
                count += 1
        if count == len(self.collection):
            self.collection.extend([None])
        self.collection.pop(count)
        self.collection.insert(count, data)
        self.main_func(data)
        return self.collection

    def c_extend(self, cll):
        to_append = [cll]
        self.collection += to_append
        self.main_func(cll)
        return self.collection

    def c_remove(self, element):
        for i in self.collection:
            if i == element:
                self.collection.remove(i)
                break

    def c_clear(self):
        for i in range(len(self.collection)):
            self.collection[i] = None

    def c_count(self, string):
        amount = 0
        for i in range(len(self.collection)):
            if string == self.collection[i]:
                amount += 1
        if amount != 0:
            return amount
        else:
            return "Error in list!"

    def c_copy(self):
        copied = self.collection
        return copied

    def c_reverse(self):
        temp = [None]*len(self.collection)
        for i in range(len(self.collection)):
            temp[(len(self.collection)-1) - i] = self.collection[i]
        return temp

    def __init__(self, lst):
        self.main_func(lst)
        for i in range(len(lst)):
            self.collection[i] = lst[i]


a = MyArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
a.c_append("ggg")
a.c_extend([1, 2, 3])
a.c_extend([1, 2, 3])
a.c_remove([1, 2, 3])
print(a.c_reverse())
