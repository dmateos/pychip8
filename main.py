import loader
import cpu
import mmu
import video

class Main(object):
    def __init__(self):
        load = loader.Loader("TETRIS")
        load.read()

        memory = mmu.MMU(load.data)
        processor = cpu.CPU(memory)
        display = video.Video()

        display.mainloop(processor.step)

if __name__ == "__main__":
    main = Main()
