import bitstring

class Loader(object):
    def __init__(self, path):
        self.path = path
        self.data = None

    def read(self):
        with open(self.path, "r") as tfile:
            self.data = bitstring.BitArray(tfile)

