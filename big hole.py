
#big NOTHING around player without effects
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
#
BlockType=0
rad=50
height=90
deep=10
#
pos=mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x-rad,y-deep,z-rad,x+rad,y+height,z+rad,BlockType)
