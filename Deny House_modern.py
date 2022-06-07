#denis(my son) house modernize
#With big thanks for John Uits and his code jonuitts_house.py 

# Connect to MineCraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


# Get our current position
x, y, z = mc.player.getPos()

# define our blocks we will be using
stone = 1
brick = 5#wood
air = 0
wood_plank = 5
glass_pane = 102
roof = 67#stone steps 67
roof_flat=1#stone
wood_step=53

# Now we build our house!
# first clear the area
mc.setBlocks(x-1, y, z-1, x+10, y+10, z+10, air)
# now lay a foundation
mc.setBlocks(x, y-1, z, x+8, y-3, z+8, stone)
# now make our house block
mc.setBlocks(x+1, y, z+1, x+7, y+5, z+7, brick)
# and hollow it ground floor
mc.setBlocks(x+2, y, z+2, x+6, y+3, z+6, air)
# and hollow it first floor
mc.setBlocks(x+2, y+5, z+2, x+6, y+5, z+6, air)
#and doors
mc.setBlock(x+1,y,z+3,64,0)
mc.setBlock(x+1,y+1,z+3,64,8)


mc.setBlock(x+2,y,z+1,64,0)
mc.setBlock(x+2,y+1,z+1,64,8)
#set windows
mc.setBlocks(x+3,y+6,z+1,x+5,y+7,z+1,glass_pane)

# Now lets add a roof
# First the pitches
for i in range(5):
    mc.setBlocks(x-1+i, y+5+i, z, x-1+i, y+5+i, z+8, roof)
    mc.setBlocks(x+9-i, y+5+i, z, x+9-i, y+5+i, z+8, roof, 1)
# Now the top
mc.setBlocks(x+4, y+10, z, x+4, y+10, z+8, roof_flat)

# Now the brick sides
for i in range(4): 
    mc.setBlocks(x+4-i, y+9-i, z+1, x+4+i, y+9-i, z+1, brick)
for i in range(4):
    mc.setBlocks(x+4-i, y+9-i, z+7, x+4+i, y+9-i, z+7, brick)
#and doors
mc.setBlock(x+1,y,z+3,64,0)
mc.setBlock(x+1,y+1,z+3,64,8)


mc.setBlock(x+2,y,z+1,64,0)
mc.setBlock(x+2,y+1,z+1,64,8)
#set windows
mc.setBlocks(x+3,y+6,z+1,x+5,y+7,z+1,glass_pane)
#set steps
mc.setBlock(x+6,y,z+2,wood_step)
for i in range(3):
    mc.setBlock(x+6,y+1+i,z+3+i,wood_step,2)
    mc.setBlock(x+6,y+4,z+3+i,0)

    

