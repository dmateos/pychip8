class CPU(object):
    def __init__(self, mmu):
        #General v (16 bit) 0-F
        self.v = [0 for n in range(0, 0xF)]

        #16 bit I register
        self.i = None

        #Stack (should be 16 levels deep) 16bit
        self.stack = []

        #Program counter
        #self.pc = 0x200
        self.pc = 0x00

        #memory
        self.mmu = mmu

    def inst_cls(self):
        pass

    def inst_return(self):
        print "return"
        self.pc = self.stack.pop()

    def inst_jump(self, address):
        self.pc = address

    def inst_call(self, address):
        print "call"
        self.stack.append(self.pc)
        self.pc = address

    def inst_comp(self, valone, valtwo):
        if valone == valtwo:
            self.pc += 16

    def inst_notcomp(self, valone, valtwo):
        if valone != valtwo:
            self.pc += 16

    def inst_setreg(self, register, value):
        self.v[register] = value

    def step(self):
        opcode = self.mmu.get4bit(self.pc)

        print opcode

        if opcode == 0x0:
            pass
        elif opcode == 0x1:
            address = self.mmu.getaddr(self.pc+4)
            self.inst_jump(address)
        elif opcode == 0x2:
            address = self.mmu.getaddr(self.pc+4)
            self.inst_call(address)
        elif opcode == 0x3:
            register = self.mmu.get4bit(self.pc+4)
            compare = self.mmu.get8bit(self.pc+8)
            self.inst_comp(register, compare)
        elif opcode == 0x4:
            register = self.mmu.get4bit(self.pc+4)
            compare = self.mmu.get8bit(self.pc+8)
            self.inst_notcomp(register, compare)
        elif opcode == 0x5:
            register = self.mmu.get4bit(self.pc+4)
            register2 = self.mmu.get4bit(self.pc+8)
            self.inst_comp(register, register2)
        elif opcode == 0x6:
            register = self.mmu.get4bit(self.pc+4)
            value = self.mmu.get8bit(self.pc+8)
            self.inst_setreg(register, value)
        elif opcode == 0x7:
            register = self.mmu.get4bit(self.pc+4)
            value = self.mmu.get8bit(self.pc+8)
            self.v[register] += value
        elif opcode == 0x8:
            reg = self.mmu.get4bit(self.pc+4)
            reg2 = self.mmu.get4bit(self.pc+8)
            lastbit = self.mmu.get4bit(self.pc+12)

            if lastbit == 0x0:
                self.inst_setreg(reg, reg2)
            elif lastbit == 0x1:
                self.inst_setreg(self.v[reg] or self.v[reg2])
            elif lastbit == 0x2:
                self.inst_setreg(self.v[reg] and self.v[reg2])
            elif lastbit == 0x3:
                self.inst_setreg(self.v[reg] ^ self.v[reg2])
            elif lastbit == 0x4:
                pass
            elif lastbit == 0x5:
                pass
            elif lastbit == 0x6:
                pass
            elif lastbit == 0x6:
                pass
            elif lastbit == 0x6:
                pass
            elif lastbit == 0x7:
                pass
            elif lastbit == 0xE:
                pass
        elif opcode == 0x9:
            pass
        elif opcode == 0xA:
            pass
        elif opcode == 0xB:
            pass
        elif opcode == 0xC:
            pass
        elif opcode == 0xD:
            pass
        elif opcode == 0xE:
            pass
        elif opcode == 0xF:
            pass

        self.pc += 16
