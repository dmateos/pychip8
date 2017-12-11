from random import randint

class CPU(object):
    def __init__(self, mmu):
        #General registers v(0,0xf) (16 bit)
        self.v = [0 for n in range(0, 0xF)]

        #Seperate i register (16bit) 
        self.i = None

        #Stack (should be 16 levels deep) (16bit)
        self.stack = []

        #Program counter
        self.pc = 0x200

        #Delay timer (60hz)
        self.clock = 0

        #Sound timer (60 hz)
        self.sound = 0

        #memory
        self.mmu = mmu

    def inst_cls(self):
        pass

    def inst_return(self):
        self.pc = self.stack.pop()

    def inst_jump(self, address):
        self.pc = address

    def inst_call(self, address):
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

        print(hex(opcode))

        if opcode == 0x0:
            lastbits = self.mmu.getaddr(self.pc+4)
            if lastbits == 0x0E0:
                print "clear"
            elif lastbits == 0x0EE:
                self.inst_return()
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
                self.inst_setreg(self.v[reg], self.v[reg] | self.v[reg2])
            elif lastbit == 0x2:
                self.inst_setreg(self.v[reg], self.v[reg] & self.v[reg2])
            elif lastbit == 0x3:
                self.inst_setreg(self.v[reg], self.v[reg] ^ self.v[reg2])
            elif lastbit == 0x4:
                #TODO set borrow flag
                self.inst_setreg(self.v[reg], self.v[reg] + self.v[reg2])
            elif lastbit == 0x5:
                #TODO set borrow flag
                self.inst_setreg(self.v[reg], self.v[reg] - self.v[reg2])
            elif lastbit == 0x6:
                self.inst_setreg(self.v[reg], self.v[reg2] - self.v[reg])
            elif lastbit == 0x6:
                self.inst_setreg(self.v[reg], self.v[reg2] - self.v[reg])
            elif lastbit == 0x6:
                pass
            elif lastbit == 0x7:
                pass
            elif lastbit == 0xE:
                pass
        elif opcode == 0x9:
            reg = self.mmu.get4bit(self.pc+4)
            reg2 = self.mmu.get4bit(self.pc+8)
            self.inst_notcomp(reg, reg2)
        elif opcode == 0xA:
            value = self.mmu.getaddr(self.pc+4)
            self.i = value
        elif opcode == 0xB:
            value = self.mmu.getaddr(self.pc+4)
            self.inst_jump(value+self.v[0])
        elif opcode == 0xC:
            reg = self.mmu.get4bit(self.pc+4)
            value = self.mmu.get8bit(self.pc+8)
            random = randint(0, 255)
            self.inst_setreg(self.v[reg], random & value)
        elif opcode == 0xD:
            pass
        elif opcode == 0xE:
            reg = self.mmu.get4bit(self.pc+4)
            lastbit = self.mmu.get8bit(self.pc+8)

            if lastbit == 0x9E:
                pass
            elif lastbit == 0xA1:
                pass
        elif opcode == 0xF:
            reg = self.mmu.get4bit(self.pc+4)
            lastbit = self.mmu.get8bit(self.pc+8)

            if lastbit == 0x07:
                pass
            elif lastbit == 0x0A:
                pass
            elif lastbit == 0x15:
                pass
            elif lastbit == 0x18:
                pass
            elif lastbit == 0x1E:
                pass
            elif lastbit == 0x29:
                pass
            elif lastbit == 0x33:
                pass
            elif lastbit == 0x55:
                pass
            elif lastbit == 0x65:
                pass

        self.pc += 16
