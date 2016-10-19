import os
os.system('cls')
from Blender import Draw,BGL
from Blender.BGL import *
import random
def event(evt,vall):    
 
  if evt == Draw.ESCKEY :	
    Draw.Exit()         
    return

def gui():             
	x0 = random.randint(50,700)
	y0 = random.randint(50,200)
	x1 = random.randint(50,1000)
	y1 = random.randint(50,1000)
	print 'x0', x0
	print 'y0', y0
	print 'x1', x1
	print 'y1', y1
	glClearColor(0,0,0,1)
	glColor3f(1.0,0,0)
	er = 0
	glBegin(GL_POINTS)
	glVertex2i(x0,y0)
	if (x0 > x1):
			x0,x1 = x1,x0
			y0,y1 = y1,y0
	x0 += 1
	while (x0 != x1):
			er += (float)(y1-y0)/(float)(x1-x0)
			if (y0 > y1):
				if (er < 0.5):
					er += 1
					y0 -= 1
			else:
				if (er > 0.5):
						er -= 1
						y0 += 1
			x0+=1
			glVertex2i(x0,y0)
	glEnd()
Draw.Register(gui,event,None)