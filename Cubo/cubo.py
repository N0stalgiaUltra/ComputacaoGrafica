from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

vertices = (
    ( 1,-1,-1),
    ( 1, 1,-1),
    (-1, 1,-1),
    (-1,-1,-1),
    ( 1,-1, 1),
    ( 1, 1, 1),
    (-1,-1, 1),
    (-1, 1, 1),
    )

linhas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5))

def Cubo():
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glColor3fv(cores[i])
        for vertex in face:
           #glColor3fv(cores[i])
           glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glColor3f(0,0.5,0)
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def CuboVerde():
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glColor3fv((0,1,0))
        for vertex in face:
           #glColor3fv(cores[i])
           glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glColor3f(0,0.5,0)
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def CuboVermelho():
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glColor3fv((1,0,0))
        for vertex in face:
           #glColor3fv(cores[i])
           glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glColor3f(0,0.5,0)
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def CuboVazado():
    glColor3f(0,0.5,0)
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()


a = 0

### Desenho dos Cubos ###
def desenhaCubo():
    # Cubo da Esquerda
    glPushMatrix()
    glTranslatef(-2,0,0)
    glRotatef(-a,0,0,1)
    CuboVazado()
    glPopMatrix()

def desenhaDoisCubos():
    # Cubo da Esquerda
    glPushMatrix()
    glTranslatef(-2,0,0)
    glRotatef(-a,0,0,1)
    CuboVazado()
    glPopMatrix()
    # Cubo da Direita
    glPushMatrix()
    glTranslatef(2,0,0)
    glRotatef(a,0,1,0)
    Cubo()
    glPopMatrix()

def desenhaTresCubos():
    # Cubo da Esquerda
    glPushMatrix()
    glTranslatef(-2,0,0)
    glRotatef(a,0,1,0)
    CuboVerde()
    glPopMatrix()
    # Cubo da Direita
    glPushMatrix()
    glTranslatef(2,0,0)
    glRotatef(a,0,1,0)
    CuboVermelho()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(6,0,0)
    glRotatef(a,0,1,0)
    Cubo()
    glPopMatrix()

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(0,-2,0)
    desenhaCubo()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,2,0)
    desenhaTresCubos()
    glPopMatrix()
    glutSwapBuffers()
    a += 1
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def mouse(botao, estado, x, y):
    print(botao, estado, x, y)

def mouseMove(x, y):
    print("-->", x, y)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CUBO")
glutDisplayFunc(desenha)
#glutMotionFunc(mouseMove)
glutPassiveMotionFunc(mouseMove)
glutMouseFunc(mouse)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-20)
glutTimerFunc(50,timer,1)
glutMainLoop()
