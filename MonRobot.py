from numpy.core.fromnumeric import shape
from numpy.lib.function_base import select
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.functions import Color
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys

class RobotiqueArm(object):
    def __init__(self,window,d,r,n,theta,phi,X0,Y0,Z0):
        self.r = r
        self.d = d
        self.n = n
        for i in range(1,n):
            theta[i] = theta[i] + theta[i-1]
            
        for i in range(1,n):
           phi[i] = phi[i] + phi[i-1]
        
        self.Theta = np.asarray(theta)
        self.Phi = np.asarray(phi)
        self.X0 = X0
        self.Y0 = Y0
        self.Z0 = Y0
        self.Xs = [X0+self.d*np.sin(self.Theta[i] * np.pi / 180)*np.sin(self.Phi[i] * np.pi / 180) for i in range(self.n)]
        self.Ys = [Y0-self.d*np.sin(self.Theta[i] * np.pi / 180)*np.cos(self.Phi[i] * np.pi / 180) for i in range(self.n)]
        self.Zs = [Z0+ self.d*np.cos(self.Theta[i] * np.pi / 180) for i in range(self.n)]
        self.elements = []
        for i in range(n):
            c = gl.MeshData.cylinder(10,10,radius=[self.r,self.r], length=self.d)
            c = gl.GLMeshItem(vertexes=c.vertexes(),
            faces=c.faces())
            s = gl.MeshData.sphere(10, 10, self.r + self.r*0.3)
            s = gl.GLMeshItem(
            vertexes=s.vertexes(),
            faces=s.faces(), 
            color=(255, 0., 0., 0.))
            X = np.sum(self.Xs[0:i]) 
            Y = np.sum(self.Ys[0:i]) 
            Z = np.sum(self.Zs[0:i]) 
            self.elements.append(Cysphere(window,[c,s], X, Y ,Z,self.Theta[i],self.Phi[i]))
        
        self.c = gl.MeshData.sphere(5, 5, self.r + self.r*0.3)
        self.c = gl.GLMeshItem(vertexes=self.c.vertexes(),
            faces=self.c.faces())
        self.c.translate(X+self.d*np.sin(self.Theta[-1] * np.pi / 180)*np.sin(self.Phi[-1] * np.pi / 180),Y - self.d*np.sin(self.Theta[-1] * np.pi / 180)*np.cos(self.Phi[-1] * np.pi / 180),Z + self.d*np.cos(self.Theta[-1] * np.pi / 180))
        window.addItem(self.c)
        

    def take_position(self,window,theta,phi):
                
    
                self.Xs = [self.X0+self.d*np.sin(theta[i] * np.pi / 180)*np.sin(phi[i] * np.pi / 180) for i in range(self.n)]
                self.Ys = [self.Y0-self.d*np.sin(theta[i] * np.pi / 180)*np.cos(phi[i] * np.pi / 180) for i in range(self.n)]
                self.Zs = [self.Z0+ self.d*np.cos(theta[i] * np.pi / 180) for i in range(self.n)]
                # self.elements = []
                for i in range(self.n):
                    window.removeItem(self.elements[i].Shapes[0])
                    window.removeItem(self.elements[i].Shapes[1])
                    c = gl.MeshData.cylinder(10,10,radius=[self.r,self.r], length=self.d)
                    c = gl.GLMeshItem(vertexes=c.vertexes(),
                    faces=c.faces())
                    s = gl.MeshData.sphere(10, 10, self.r + self.r*0.3)
                    s = gl.GLMeshItem(
                    vertexes=s.vertexes(),
                    faces=s.faces(), 
                    color=(255, 0., 0., 0.))
                    X = np.sum(self.Xs[0:i]) 
                    Y = np.sum(self.Ys[0:i]) 
                    Z = np.sum(self.Zs[0:i]) 
                    self.elements[i] = Cysphere(window,[c,s], X, Y ,Z,theta[i],phi[i])
                window.removeItem(self.c)
                self.c = gl.MeshData.sphere(10, 10, self.r + self.r*0.3)
                self.c = gl.GLMeshItem(vertexes=self.c.vertexes(),
                    faces=self.c.faces())
                self.c.translate(X+self.d*np.sin(theta[-1] * np.pi / 180)*np.sin(phi[-1] * np.pi / 180),Y - self.d*np.sin(theta[-1] * np.pi / 180)*np.cos(phi[-1] * np.pi / 180),Z + self.d*np.cos(theta[-1] * np.pi / 180))
                window.addItem(self.c)
                self.Theta = np.asarray(theta)
                self.Phi = np.asarray(phi)

        # for i in range(len(self.elements)):
        #     directionTheta =theta[i] - self.elements[i].Theta
        #     directionPhi =phi[i] - self.elements[i].Theta

        #     if directionTheta != 0:
        #         self.elements[i].Shapes[0].rotate(directionTheta/abs(directionTheta),1,0,0)
        #         self.elements[i].Shapes[0].translate(0,self.elements[i].Zg*np.sin(directionTheta/abs(directionTheta)*np.pi/180),self.elements[i].Zg*(1-np.cos(directionTheta/abs(directionTheta)*np.pi/180)))
        #         self.elements[i].Theta += directionTheta/abs(directionTheta)
              
        #         self.Xs = [self.X0+self.d*np.sin(self.elements[i].Theta* np.pi / 180)*np.sin(self.elements[i].Phi * np.pi / 180) for i in range(self.n)]
        #         self.Ys = [self.Y0-self.d*np.sin(self.elements[i].Theta * np.pi / 180)*np.cos(self.elements[i].Phi * np.pi / 180) for i in range(self.n)]
        #         self.Zs = [self.Z0+ self.d*np.cos(self.elements[i].Theta * np.pi / 180) for i in range(self.n)]

        #         for i in range(self.n):
        #             X = np.sum(self.Xs[0:i]) 
        #             Y = np.sum(self.Ys[0:i]) 
        #             Z = np.sum(self.Zs[0:i])
        #             self.elements[i].Shapes[0].translate(X - self.elements[i].Xg ,Y - self.elements[i].Yg ,Z - self.elements[i].Zg)
        #             self.elements[i].Shapes[1].translate(X - self.elements[i].Xg ,Y - self.elements[i].Yg ,Z - self.elements[i].Zg)
        #             self.elements[i].Xg = X
        #             self.elements[i].Yg = Y
        #             self.elements[i].Zg = Z

                
            # elif self.elements[i].Phi != phi[i]:
            #     self.elements[i].Shapes[0].rotate(directionPhi/abs(directionPhi),0,0,1)
            #     self.elements[i].Phi != directionPhi/abs(directionPhi)

            
               
                
           

            # self.z = 3*self.d*(1-np.cos(self.pos*np.pi/180))
            # self.x = 3*self.d*np.sin(self.pos*np.pi/180)
            # self.pos += self.direction 
            # if self.pos >= 90:
            #     self.direction = -1
            #     self.pos = 90
            # if self.pos <= -90:
            #     self.direction = 1
            #     self.pos = -90

class Cysphere(object):
    def __init__(self,window, Mesh, Xg, Yg, Zg, Theta, Phi):
        self.Shapes = Mesh
        self.Xg = Xg
        self.Yg = Yg
        self.Zg = Zg
        self.Theta = Theta
        self.Phi = Phi
        self.shapes_init(window)

    def shapes_init(self,window):
            self.Shapes[0].rotate(self.Theta,1,0,0)
            self.Shapes[0].rotate(self.Phi,0,0,1)
            self.Shapes[0].translate(self.Xg,self.Yg,self.Zg)
            self.Shapes[1].translate(self.Xg,self.Yg,self.Zg)
            window.addItem(self.Shapes[0])
            window.addItem(self.Shapes[1])

    # def rotate(self,window,theta,phi):
    #     self.Shapes[0].rotate(theta,np.sin(phi),np.cos(phi),0)
    #     self.Shapes[0].rotate(phi,0,0,1)
    #     self.Shapes[0].translate(self.Xg,self.Yg,self.Zg)
    #     self.Shapes[1].translate(self.Xg,self.Yg,self.Zg)
    #     window.addItem(self.Shapes[0])
    #     window.addItem(self.Shapes[1])
    
    def relative_correction():
        pass


class Visualizer(object):
    def __init__(self,d,r,x0,y0,n):
        self.app = QtGui.QApplication(sys.argv)
        self.ww = QtGui.QWidget()
        self.ww.resize(1920,1080)

        ## Create some widgets to be placed inside
        self.btn = QtGui.QPushButton('Animate')
        self.nameLabel0 = QtGui.QLabel("Theta0")
        self.nameLabel1 = QtGui.QLabel("Theta1")
        self.nameLabel2 = QtGui.QLabel("Theta2")
        self.nameLabel3 = QtGui.QLabel("Theta3")
        self.nameLabel4 = QtGui.QLabel("Phi0")
        self.nameLabel5 = QtGui.QLabel("Phi1")
        self.nameLabel6 = QtGui.QLabel("Phi2")
        self.nameLabel7 = QtGui.QLabel("Phi3")
        self.Theta0 = QtGui.QLineEdit('0')
        self.Theta1 = QtGui.QLineEdit('0')
        self.Theta2 = QtGui.QLineEdit('0')
        self.Theta3 = QtGui.QLineEdit('0')
        self.Phi0 = QtGui.QLineEdit('0')
        self.Phi1 = QtGui.QLineEdit('0')
        self.Phi2 = QtGui.QLineEdit('0')
        self.Phi3 = QtGui.QLineEdit('0')
        self.w = gl.GLViewWidget()
        self.w.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
 
        ## Create a grid layout to manage the widgets size and position
        layout = QtGui.QGridLayout()
        self.ww.setLayout(layout)
        layout.setColumnStretch (1, 2)
        self.w.opts['distance'] = 40
        self.w.setWindowTitle('6 degres of freedom ROBOT')
        self.w.setGeometry(0, 110, 1920, 1080)
        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(-10, 0, 0)
        self.w.addItem(gx)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)
        gy.translate(0, -10, 0)
        self.w.addItem(gy)
        gz = gl.GLGridItem()
        gz.translate(0, 0, -10)
        self.w.addItem(gz)
        layout.addWidget(self.nameLabel0, 0, 0)   # text edit goes in middle-left
        layout.addWidget(self.Theta0, 1, 0)   # text edit goes in middle-left
        layout.addWidget(self.nameLabel1, 2, 0)   # text edit goes in middle-left
        layout.addWidget(self.Theta1, 3, 0)   # text edit goes in middle-left
        layout.addWidget(self.nameLabel2, 4, 0)   # text edit goes in middle-left
        layout.addWidget(self.Theta2, 5, 0)   # text edit goes in middle-left
        layout.addWidget(self.nameLabel3, 6, 0)   # text edit goes in middle-left
        layout.addWidget(self.Theta3, 7, 0)   # text edit goes in middle-left
        layout.addWidget(self.nameLabel4, 8, 0)   # text edit goes in middle-left
        layout.addWidget(self.Phi0, 9, 0)   # text edit goes in middle-left
        layout.addWidget(self.nameLabel5, 10, 0)   # text edit goes in middle-left
        layout.addWidget(self.Phi1, 11, 0)   # text edit goes in middle-left
        layout.addWidget(self.nameLabel6, 12, 0)   # text edit goes in middle-left
        layout.addWidget(self.Phi2, 13, 0)   # text edit goes in middle-left
        layout.addWidget(self.nameLabel7, 14, 0)   # text edit goes in middle-left
        layout.addWidget(self.Phi3, 15, 0)  
        layout.addWidget(self.w, 0, 1, 16, 1)  # plot goes on right side, spanning 3 rows
        self.ww.show()
        self.r = r
        self.d = d
        self.x0 = x0
        self.y0 = y0
        self.n = n
        self.C = []
        self.S = [] 
        self.RobotParts = []
        self.pos= 0
        self.x=0
        self.z=3*d
        self.direction = 1
        self.MonRobot = RobotiqueArm(self.w,self.d,self.r,4,[0,0,0,0],[0,0,0,0],0,0,0)
    
    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

    def set_plotdata(self, name, points, color, width):
        self.traces[name].setData(pos=points, color=color, width=width)
    
    def animateTransfer(self, TargetTheta, TargetPhi, resolution = 1):
        for i in range(1,len(TargetPhi)):
            TargetPhi[i] = TargetPhi[i] + TargetPhi[i-1]
        for i in range(1,len(TargetTheta)):
            TargetTheta[i] = TargetTheta[i] + TargetTheta[i-1]
        DeltaTheta = np.asarray(TargetTheta) - self.MonRobot.Theta
        DeltaPhi = np.asarray(TargetPhi) - self.MonRobot.Phi
        if np.sum(abs(DeltaTheta)) != 0 or np.sum(abs(DeltaPhi)) != 0:
            directionTheta = []
            directionPhi = []
            for i in range(len(DeltaTheta)):
                if DeltaTheta[i] == 0:
                    dtheta = 0 
                else:
                    dtheta =DeltaTheta[i]/abs(DeltaTheta[i])

                if DeltaPhi[i] == 0:
                    dphi = 0 
                else:
                    dphi = DeltaPhi[i]/abs(DeltaPhi[i])
                directionTheta.append(dtheta) 
                directionPhi.append(dphi)
            self.MonRobot.take_position(self.w, self.MonRobot.Theta + np.asarray(directionTheta), self.MonRobot.Phi + np.asarray(directionPhi))

            

    def update(self):
        
        self.animateTransfer([int(self.Theta0.text()),int(self.Theta1.text()),int(self.Theta2.text()),int(self.Theta3.text())],[int(self.Phi0.text()),int(self.Phi1.text()),int(self.Phi2.text()),int(self.Phi3.text())])
        

    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(5)
        self.start()


# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    v = Visualizer(1.5,0.15,0,0,4)
    v.animation()