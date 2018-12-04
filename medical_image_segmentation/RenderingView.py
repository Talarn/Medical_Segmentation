import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class RenderingView(QFrame):

  def __init__(self):
    QFrame.__init__(self)
  
  def windowInitialization(self):
    self.verticalLayout = QVBoxLayout()
    self.vtkWidget = QVTKRenderWindowInteractor(self)
    self.vtkWidget.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred))
    self.verticalLayout.addWidget(self.vtkWidget)
    self.renderer = vtk.vtkRenderer()
    self.vtkWidget.GetRenderWindow().AddRenderer(self.renderer)
    self.rendererInteractor = self.vtkWidget.GetRenderWindow().GetInteractor()

    # self.renderer.AddActor(outline)
    # self.renderer.AddActor(arter)
    self.renderer.ResetCamera()
    self.renderer.SetBackground(0,0,0)

    self.setLayout(self.verticalLayout)
    # self.horizontalLayout_2.addWidget(self)
 
    self.rendererInteractor.Initialize()