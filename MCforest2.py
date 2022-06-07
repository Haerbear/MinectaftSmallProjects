#MC forest
'''
make trees in random places nearly player with time delay
'''
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

import time
import random

count=10 #amount of trees
dz=0
dx=0
delay=1

def grow_Tree(x,y,z):#the tree with random leaves and random high
    height=random.randint(3,7)
    for i in range(height):
        mc.setBlock(x,y,z,17,2)#birch trunk
        y+=1

    xs=x-2
    zs=z-2
    ys=y-2
    xf=x+2
    zf=z+2
    yf=y+4
    
    for i in range(73):  #blocks of leaves from 125
        xl=random.randint(xs,xf)
        zl=random.randint(zs,zf)
        yl=random.randint(ys,yf)
        mc.setBlock(xl,yl,zl,161)#leaves
        
        
    
        
    
    

while count>0:
    
    pos=mc.player.getTilePos()
    #set variables 
    dx=random.randint(-5,5)
    dz=random.randint(-5,5)
    x = pos.x+dx
    y = pos.y
    z = pos.z+dz
    delay=random.randint(1,2)
    time.sleep(delay)
    grow_Tree(x,y,z)
    
    count-=1
    

quit()
