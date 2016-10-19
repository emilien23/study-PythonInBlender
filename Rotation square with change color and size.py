import os
os.system('cls')
import Blender
from Blender import Draw 
from Blender.BGL import *
import time
from Blender.Mathutils import *
import math
from math import sin,cos
pt0=Vector(100,100)
pt1=Vector(100,200)
pt2=Vector(200,200)
pt3=Vector(200,100)
mddl=(pt0+pt2)*0.5
pt0s=pt0-mddl
pt1s=pt1-mddl
pt2s=pt2-mddl
pt3s=pt3-mddl
a = 0
ac= 0
c = 0
i = 0
def changeA():
	global a, ac, i
	a +=.2
	ac+=.2
	if ac > 6:
		i += 1
		ac = 0
	time.sleep(0.1)	
	Draw.Redraw(1)
	
def rotMatr(ang):
	mtr=Matrix([cos(ang),-sin(ang)],[sin(ang),cos(ang)])				
	return mtr	

def ChoiceColor(ac):
	if ac > 0 and ac < 1.5:
		glColor3f(1,0,0)
	elif ac > 1.5 and ac < 3:
		glColor3f(0,1,0)
	elif ac > 3 and ac < 4.5:
		glColor3f(0,0,1)
	elif ac > 4.5 and ac < 6:
		glColor3f(0,1,1)
	else:
		glColor3f(1,0,0)
	return ac

def event(evt, val):    
 
  if evt == Draw.ESCKEY :	
    Draw.Exit()         
    return

def gui():
	global a, ac, c      
	glClearColor(0,0,0,1)
 	glClear(GL_COLOR_BUFFER_BIT)
	glLineWidth(5)
	ChoiceColor(ac)
	mtr1=rotMatr(a)
	if i % 2 == 0:
		c += 0.025
	else:
		c -= 0.025
	rpt0=mtr1*pt0s * (1 + c)
	rpt1=mtr1*pt1s * (1 + c)
	rpt2=mtr1*pt2s * (1 + c)
	rpt3=mtr1*pt3s * (1 + c)
	pt0t=rpt0+mddl
	pt1t=rpt1+mddl
	pt2t=rpt2+mddl
	pt3t=rpt3+mddl
	glBegin(GL_QUADS)
	glVertex2f(*pt0t)
	glVertex2f(*pt1t)
	glVertex2f(*pt2t)	
	glVertex2f(*pt3t)
	glEnd()	
	
	changeA()
	
Draw.Register(gui, event,None)