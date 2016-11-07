import os
os.system('cls')
import Blender
from Blender import Draw 
from Blender.BGL import *
import time
from Blender.Mathutils import *
import math
from math import sin,cos
r1 = 0
x2 = 0
y2 = 0
x = 0
y = 0
r = 0
i = 0
def changeI():
	global i
	if i < 10: 
		i += 1
		time.sleep(0.1)	
		Draw.Redraw(1)
def event(evt, val):    
	if evt == Draw.ESCKEY :	
		Draw.Exit()         
def button_event(evt):  
	global x2,y2,r1
  	if evt == 1:			
		x=Draw.Create(x2) 
		y=Draw.Create(y2)
		r=Draw.Create(r1)	
		block=[]			
		block.append(("X= ",x,0,400))
		block.append(("Y= ",y,0,600))
		block.append(("R= ",r,0,600))
		retVal=Draw.PupBlock("Line coords and radius",block) 
		x2 = x.val
		y2 = y.val
		r1 = r.val
		Draw.Redraw(1)
		return

def gui():
	global x2,y2,r1, i     
	Draw.PushButton("Add point",1,1,10,100,70,"Add point to polygon")
	if (x2 > 0 and y2 > 0):
		maincircle(x2,y2,r1)
		LittlecircleOne(x2,y2,r1, i)
		LittlecircleTwo(x2,y2,r1, i)
		changeI()
def maincircle(x1,y1,r1):
	glColor3f(0,0,1)
	glBegin(GL_LINE_LOOP)
	j = 0
	for j in range (51):
		angle = 2.0 * 3.1415926 * float(j) / float(51)
		dx = r1 * cos(angle)
		dy = r1 * sin(angle)
		glVertex2f(x1 + dx, y1 + dy)
	glEnd()
def LittlecircleOne(x1,y1,r1, i):
	angle = 2.0 * 3.1415926 * float(i) / float(51)
	dx = r1 * 1.5 * cos(angle)
	dy = r1 * 1.5 * sin(angle)
	maincircle(x1 + dx, y1 + dy, r1/2)
def LittlecircleTwo(x1,y1,r1, i):
	angle = 2.0 * 3.1415926 * float(51 - i) / float(51)
	dx = r1 * 1.5 * cos(angle)
	dy = r1 * 1.5 * sin(angle)
	maincircle(x1 - dx, y1 - dy, r1/2)
Draw.Register(gui, event, button_event)