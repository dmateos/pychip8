class MMU(object):
    def __init__(self, rom_data):
        self.data = rom_data
        for x in range(0, 200):
            self.data.prepend('0b0')
        print self.data

    def get(self, addr, to):
        return self.data[addr:addr+to]

    def getaddr(self, addr):
        return self.get(addr, 12).uint

    def get8bit(self, addr):
        return self.get(addr, 8).uint

    def get4bit(self, addr):
        return self.get(addr, 4).uint
