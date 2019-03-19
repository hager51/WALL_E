from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
import numpy as np
from math import  *

def draw_cir (r=0.5, xc=0, yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2*pi, .01):
        x =xc + r*cos(theta)
        y =yc + r*sin(theta)
        glVertex(x, y)
    glEnd()

def draw():
    
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    
    
    glBegin(GL_QUADS) #Body
    
    glColor3f(1,.9,0)
    
    glVertex(.25, .35, -.5)
    glVertex(-.25, .35, -.5)
    glVertex(-.25, -.25, -.5)
    glVertex(.25, -.25, -.5)

    glColor3f(0.3,0.5,0.5)
    
    glVertex(.05, .35, -.5)
    glVertex(-.05, .35, -.5)
    glVertex(-.05, .42, -.5)
    glVertex(.05, .42, -.5)

    glVertex(.025, .42, -.5)
    glVertex(-.025, .42, -.5)
    glVertex(-.025, .47, -.5)
    glVertex(.025, .47, -.5)

    glVertex(.025, .47, -.5)
    glVertex(-.025, .47, -.5)
    glVertex(-.07, .55, -.5)
    glVertex(.07, .55, -.5)

    glColor3f(.4,.6,1)

    glVertex(0, .33, -.5)
    glVertex(0, .28, -.5)
    glVertex(-.12, .28, -.5)
    glVertex(-.12, .33, -.5)

    glEnd()

    
    glColor3f(.3,.4,.4)
    draw_cir(.07,.1,.55)
    draw_cir(.07,-.1,.55)


    glColor3f(0,0,0)
    draw_cir(.03,.1,.55)
    draw_cir(.03,-.1,.55)


    glColor3f(.7,.2,.7)
    draw_cir(.025,.08,.3)


    glBegin(GL_LINES) #Body Frame

    glColor3f(0,0,1)

    glVertex(.25, .35, -.5)
    glVertex(-.25, .35, -.5)
    glVertex(-.25, -.25, -.5)
    glVertex(.25, -.25, -.5)
    glVertex(.25, .35, -.5)
    glVertex(.25, -.25, -.5)
    glVertex(-.25, -.25, -.5)
    glVertex(-.25, .35, -.5)
    glVertex(-.25, .25, -.5)
    glVertex(.25, .25, -.5)

    glEnd()

   
    
    glBegin(GL_QUADS)  #Right_Hands

    glColor3f(.2,.8,.8)

    glVertex(.1, .23, -.5)
    glVertex(.1, .26, -.5)
    glVertex(.22, .275, -.5)
    glVertex(.22, .23, -.5)

    glVertex(.22, .23, -.5)
    glVertex(.32, .23, -.5)
    glVertex(.32, .275, -.5)
    glVertex(.22, .275, -.5)

    glVertex(.1, .205, -.5)
    glVertex(.1, .175, -.5)
    glVertex(.22, .16, -.5)
    glVertex(.22, .205, -.5)

    glVertex(.22, .205, -.5)
    glVertex(.32, .205, -.5)
    glVertex(.32, .16, -.5)
    glVertex(.22, .16, -.5)

    glVertex(.28, .25, -.5)
    glVertex(.28, .185, -.5)
    glVertex(.32, .185, -.5)
    glVertex(.32, .25, -.5)

    glColor3f(.3,.5,.5)
    glVertex(.14, .205, -.5)
    glVertex(.28, .205, -.5)
    glVertex(.28, .23, -.5)
    glVertex(.14, .23, -.5)

    glEnd()


    glBegin(GL_LINES)

    glColor3f(0, 0, 1)

    glVertex(.1, .23, -.5)
    glVertex(.1, .26, -.5)
    glVertex(.1, .205, -.5)
    glVertex(.1, .175, -.5)
    glVertex(.22, .275, -.5)
    glVertex(.22, .23, -.5)
    glVertex(.22, .205, -.5)
    glVertex(.22, .16, -.5)
    glVertex(.32, .275, -.5)
    glVertex(.32, .16, -.5)
    glVertex(.32, .275, -.5)
    glVertex(.22, .275, -.5)
    glVertex(.32, .16, -.5)
    glVertex(.22, .16, -.5)
    glVertex(.1, .26, -.5)
    glVertex(.22, .275, -.5)
    glVertex(.1, .23, -.5)
    glVertex(.22, .23, -.5)
    glVertex(.1, .205, -.5)
    glVertex(.22, .205, -.5)
    glVertex(.1, .175, -.5)
    glVertex(.22, .16, -.5)
    glVertex(.28, .25, -.5)
    glVertex(.28, .185, -.5)
    glVertex(.32, .25, -.5)
    glVertex(.28, .25, -.5)
    glVertex(.28, .185, -.5)
    glVertex(.32, .185, -.5)
    glVertex(.28, .25, -.5)
    glVertex(.28, .25, -.5)
    glVertex(.28, .25, -.5)
    glVertex(.28, .25, -.5)
    
    glEnd()
    

    glBegin(GL_QUADS)  #Left_Hands

    glColor3f(.2,.8,.8)

    glVertex(-.1, .23, -.5)
    glVertex(-.1, .26, -.5)
    glVertex(-.22, .275, -.5)
    glVertex(-.22, .23, -.5)

    glVertex(-.22, .23, -.5)
    glVertex(-.32, .23, -.5)
    glVertex(-.32, .275, -.5)
    glVertex(-.22, .275, -.5)

    glVertex(-.1, .205, -.5)
    glVertex(-.1, .175, -.5)
    glVertex(-.22, .16, -.5)
    glVertex(-.22, .205, -.5)

    glVertex(-.22, .205, -.5)
    glVertex(-.32, .205, -.5)
    glVertex(-.32, .16, -.5)
    glVertex(-.22, .16, -.5)

    glVertex(-.28, .25, -.5)
    glVertex(-.28, .185, -.5)
    glVertex(-.32, .185, -.5)
    glVertex(-.32, .25, -.5)

    glColor3f(.3,.5,.5)
    glVertex(-.14, .205, -.5)
    glVertex(-.28, .205, -.5)
    glVertex(-.28, .23, -.5)
    glVertex(-.14, .23, -.5)

    glEnd()


    glBegin(GL_LINES)

    glColor3f(0, 0, 1)

    glVertex(-.1, .23, -.5)
    glVertex(-.1, .26, -.5)
    glVertex(-.1, .205, -.5)
    glVertex(-.1, .175, -.5)
    glVertex(-.22, .275, -.5)
    glVertex(-.22, .23, -.5)
    glVertex(-.22, .205, -.5)
    glVertex(-.22, .16, -.5)
    glVertex(-.32, .275, -.5)
    glVertex(-.32, .16, -.5)
    glVertex(-.32, .275, -.5)
    glVertex(-.22, .275, -.5)
    glVertex(-.32, .16, -.5)
    glVertex(-.22, .16, -.5)
    glVertex(-.1, .26, -.5)
    glVertex(-.22, .275, -.5)
    glVertex(-.1, .23, -.5)
    glVertex(-.22, .23, -.5)
    glVertex(-.1, .205, -.5)
    glVertex(-.22, .205, -.5)
    glVertex(-.1, .175, -.5)
    glVertex(-.22, .16, -.5)
    glVertex(-.28, .25, -.5)
    glVertex(-.28, .185, -.5)
    glVertex(-.32, .25, -.5)
    glVertex(-.28, .25, -.5)
    glVertex(-.28, .185, -.5)
    glVertex(-.32, .185, -.5)
    glVertex(-.28, .25, -.5)
    glVertex(-.28, .25, -.5)
    glVertex(-.28, .25, -.5)
    glVertex(-.28, .25, -.5)
    
    glEnd()
    
    

    glBegin(GL_QUADS)  #Right_Weels
    
    glColor3f(.3,.5,.5)
    
    glVertex(.3, -.125, -.5)
    glVertex(.42, -.125, -.5)
    glVertex(.42, -.375, -.5)
    glVertex(.3, -.375, -.5)

    glEnd()

    glBegin(GL_LINES) #Right_Weels Frame

    glColor3f(0,0,1)

    glVertex(.3, -.125, -.5)
    glVertex(.42, -.125, -.5)
    glVertex(.3, -.175, -.5)
    glVertex(.42, -.175, -.5)
    glVertex(.3, -.225, -.5)
    glVertex(.42, -.225, -.5)
    glVertex(.3, -.275, -.5)
    glVertex(.42, -.275, -.5)
    glVertex(.3, -.325, -.5)
    glVertex(.42, -.325, -.5)
    glVertex(.3, -.375, -.5)
    glVertex(.42, -.375, -.5)
    glVertex(.3, -.125, -.5)
    glVertex(.3, -.375, -.5)
    glVertex(.42, -.125, -.5)
    glVertex(.42, -.375, -.5)
    
    glEnd()


    glBegin(GL_QUADS)  #left_Weels
    
    glColor3f(.3,.5,.5)
    
    glVertex(-.3, -.125, -.5)
    glVertex(-.42, -.125, -.5)
    glVertex(-.42, -.375, -.5)
    glVertex(-.3, -.375, -.5)

    glEnd()

    glBegin(GL_LINES)  #left_Weels Frame  

    glColor3f(0,0,1)

    glVertex(-.3, -.125, -.5)
    glVertex(-.42, -.125, -.5)
    glVertex(-.3, -.175, -.5)
    glVertex(-.42, -.175, -.5)
    glVertex(-.3, -.225, -.5)
    glVertex(-.42, -.225, -.5)
    glVertex(-.3, -.275, -.5)
    glVertex(-.42, -.275, -.5)
    glVertex(-.3, -.325, -.5)
    glVertex(-.42, -.325, -.5)
    glVertex(-.3, -.375, -.5)
    glVertex(-.42, -.375, -.5)
    glVertex(-.3, -.125, -.5)
    glVertex(-.3, -.375, -.5)
    glVertex(-.42, -.125, -.5)
    glVertex(-.42, -.375, -.5)
    
    glEnd()

    glBegin(GL_LINES)
    
    glColor3f(0.3,0.5,0.5)
    
    glVertex(-.25, -.28, -.5)
    glVertex(-.3, -.25, -.5)
    glVertex(-.3, -.2, -.5)
    glVertex(-.25, -.2, -.5)
    glVertex(-.25, -.28, -.5)
    glVertex(-.18, -.28, -.5)
    glVertex(-.18, -.28, -.5)
    glVertex(-.18, -.25, -.5)
    glVertex(-.18, -.28, -.5)
    glVertex(-.21, -.31, -.5)
    glVertex(-.21, -.31, -.5)
    glVertex(-.25, -.31, -.5)
    glVertex(-.25, -.31, -.5)
    glVertex(-.25, -.28, -.5)
    glVertex(-.25, -.29, -.5)
    glVertex(-.3, -.29, -.5)
    glVertex(-.3, -.3, -.5)
    glVertex(-.25, -.3, -.5)
    glVertex(-.22, -.3, -.5)
    glVertex(-.22, -.29, -.5)
    

    glEnd()



    glBegin(GL_LINES)
    
    glColor3f(0.3,0.5,0.5)
    
    glVertex(.25, -.28, -.5)
    glVertex(.3, -.25, -.5)
    glVertex(.3, -.2, -.5)
    glVertex(.25, -.2, -.5)
    glVertex(.25, -.28, -.5)
    glVertex(.18, -.28, -.5)
    glVertex(.18, -.28, -.5)
    glVertex(.18, -1/4, -.5)
    glVertex(.18, -.28, -.5)
    glVertex(.21, -.31, -.5)
    glVertex(.21, -.31, -.5)
    glVertex(.25, -.31, -.5)
    glVertex(.25, -.31, -.5)
    glVertex(.25, -.28, -.5)
    glVertex(.25, -.29, -.5)
    glVertex(.3, -.29, -.5)
    glVertex(.3, -.3, -.5)
    glVertex(.25, -.3, -.5)
    glVertex(.22, -.3, -.5)
    glVertex(.22, -.29, -.5)

    glEnd()

    
    glFlush() 

def main():
    
    glutInit("")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    window = glutCreateWindow(b"WALL_E")
    glutDisplayFunc(draw)                              
    glutMainLoop()                                  

main()
