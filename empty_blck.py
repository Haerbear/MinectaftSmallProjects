#empty block

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

class Building(object):
    def __init__(self, x, y, z, width, height, depth):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth
    def build(self):
        mc.setBlocks(self.x, self.y, self.z,self.x + self.width, self.y + self.height,self.z + self.depth, material)
        mc.setBlocks(self.x + 1, self.y + 1, self.z + 1,self.x + self.width - 1, self.y + self.height - 1,self.z + self.depth - 1, 0)


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

material=4
w=int(input('Width :\n'))
height=int(input('height :\n'))
d=int(input('depth:\n'))
      
ghostHouse = Building(x, y, z, w, height, d)
ghostHouse.build()
