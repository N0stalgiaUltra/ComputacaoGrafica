from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

def esfera():
    
    glRotatef(1,1,0,0)
    glBegin(GL_POINTS)
    raio = 1
    n = 50
    for i in range(0,n):
        theta = (i*pi/n) - pi/2
        for j in range(0,n):
            phi = (j*2*pi)/n
            x = raio * cos(theta) * cos(phi)
            y = raio * sin(theta)
            z = raio * cos(theta) * sin(phi)
            #glColor3fv(1,1,1)
            glVertex3f(x,y,z)
    glEnd()
        
def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    esfera()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CIRCULO")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45.0,  800.0/600.0,  0.1,       100.0)
glTranslatef(0.0,0.0,-5.0)
glutTimerFunc(10,timer,1)
glutMainLoop()