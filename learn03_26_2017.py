class letter(object):
    """docstring for letter"""
    def __init__(self):
        super(letter, self).__init__()
        self.current ='a'
    def __next__(self):
        if self.current > 'z':     
            raise StopIteration
        result = self.current
        # print(ord(result))
        self.current = chr(ord(result)+1)
        return result
    def __iter__(self):
        return self
letters = letter()
for x in letters:
    print(x)