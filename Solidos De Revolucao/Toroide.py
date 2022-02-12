from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

density = 50
rotation_speed = 2
global_radius = 2
hole_radius = 1
color = 0.001

def setColor(i, j): 
    
    if i < density//2: 
        r = (i) / (density/2 - 1)
        g = (i) / (density/2 - 1)
        b = (i) / (density/2 - 1)
    else:
        r = ((density - i) / (density/2 - 1)) - 0.08
        g = ((density - i) / (density/2 - 1)) - 0.08
        b = ((density - i) / (density/2 - 1)) - 0.08
    
    glColor3f(r, g, b)

def donut(u, v):
    theta = ( u * 2 * pi) / (density - 1)
    phi = (v * 2 * pi) / (density - 1)
    x = (global_radius + hole_radius * cos(theta)) * cos(phi)
    y = (global_radius + hole_radius * cos(theta)) * sin(phi)
    z = (hole_radius * sin(theta))

    return x, y, z

def draw_donut_points():
    glTranslatef(4,0,0)
    glRotatef(angle,0,1,0)

    glColor3f(1, 1, 1)

    glBegin(GL_POINTS)
    for i in range(density):
        for j in range(density):
            glVertex3fv(donut(i,j))
    glEnd()

angle = 0


def draw_filled_donut():
    glTranslatef(-4,0,0)
    glRotatef(angle,0,1,0)

    for i in range(density):    
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(density):
            setColor(i,j)
            glVertex3fv(donut(i,j))
            glVertex3fv(donut(i - 1,j))
        glEnd()

angle = 0

def draw():
    global angle
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()    
    draw_filled_donut()    
    glPopMatrix()

    glPushMatrix()    
    draw_donut_points()    
    glPopMatrix()
    
    glutSwapBuffers()
    
    angle += rotation_speed
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Donut")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()
