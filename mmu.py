class MMU(object):
    def __init__(self, rom_data):
        self.data = rom_data

    def get(self, addr, to):
        return self.data[addr:addr+to]

    def getaddr(self, addr):
        return self.get(addr, 12).uint

    def get8bit(self, addr):
        return self.get(addr, 8).uint

    def get4bit(self, addr):
        return self.get(addr, 4).uint
