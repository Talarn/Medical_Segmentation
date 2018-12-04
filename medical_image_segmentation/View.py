import os
from Controller import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import cv2
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class View(QMainWindow):

  def __init__(self):
    super(View, self).__init__()
    loadUi('view.ui', self)
    self.control = None
    image_1 = cv2.imread("a.jpg")

    height, width, channel = image_1.shape
    bytesPerLine = 3 * width
    qImg = QImage(image_1.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
    self.originalImageDisplay.setPixmap(QPixmap.fromImage(qImg))

    frame = QFrame()
    verticalLayout = QVBoxLayout()
    self.vtkWidget = QVTKRenderWindowInteractor(frame)
    self.vtkWidget.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
    verticalLayout.addWidget(self.vtkWidget)
  
    renderer = vtk.vtkRenderer()
    self.vtkWidget.GetRenderWindow().AddRenderer(renderer)
    rendererInteractor = self.vtkWidget.GetRenderWindow().GetInteractor()

    #Lecture des coupes 2D

    v16 = vtk.vtkDICOMImageReader()
    v16.SetDirectoryName("D:/Projet_3CT/Data_IRM/02-OS/")
    v16.Update()
    print(v16.GetOutputPort())
    arterExtractor = vtk.vtkContourFilter()
    arterExtractor.SetInputConnection(v16.GetOutputPort())
    arterExtractor.SetValue(0, 350)
    arterNormals = vtk.vtkPolyDataNormals()
    arterNormals.SetInputConnection(arterExtractor.GetOutputPort())
    arterNormals.SetFeatureAngle(100.0)
    arterStripper = vtk.vtkStripper()
    arterStripper.SetInputConnection(arterNormals.GetOutputPort())
    arterMapper = vtk.vtkPolyDataMapper()
    arterMapper.SetInputConnection(arterStripper.GetOutputPort())
    arterMapper.ScalarVisibilityOff()
    arter = vtk.vtkActor()
    arter.SetMapper(arterMapper)
    arter.GetProperty().SetDiffuseColor(1, 1, .9412)
  
    outlineData = vtk.vtkOutlineFilter()
    outlineData.SetInputConnection(v16.GetOutputPort())
    mapOutline = vtk.vtkPolyDataMapper()
    mapOutline.SetInputConnection(outlineData.GetOutputPort())
    outline = vtk.vtkActor()
    outline.SetMapper(mapOutline)
    outline.GetProperty().SetColor(1,1,1)

    renderer.AddActor(outline)
    renderer.AddActor(arter)
    renderer.ResetCamera()
    renderer.SetBackground(0,0,0)
    frame.setLayout(verticalLayout)
    self.horizontalLayout_3.addWidget(frame)
 
    self.show()
    rendererInteractor.Initialize()
    self.uiInitialization()

  def setControl(self, c):
    self.control = c

  def uiInitialization(self):
    self.bothViewButton.clicked.connect(self.changeDisplayVisibility)
    self.originalViewButton.clicked.connect(self.changeDisplayVisibility)
    self.renderingViewButton.clicked.connect(self.changeDisplayVisibility)

    self.vtkWidget.hide()
    self.originalViewButton.setChecked(True)

  @pyqtSlot()
  def changeDisplayVisibility(self):
    sender = self.sender()
    radioButtonName = sender.accessibleName()
    if(radioButtonName == 'both'):
      self.vtkWidget.show()
      self.originalImageDisplay.show()
    elif(radioButtonName == 'rendering'):
      self.vtkWidget.show()
      self.originalImageDisplay.hide()
    elif(radioButtonName == 'original'):
      self.vtkWidget.hide()
      self.originalImageDisplay.show()

  def keyPressEvent(self, event):
    if event.key() == Qt.Key_F11:
      if self.isFullScreen():
        self.showNormal()
      else:
        self.showFullScreen()
    elif event.key() == Qt.Key_Escape:
      self.deleteLater()

  @pyqtSlot()
  def getImagePath(self):
    # filename = QFileDialog.getOpenFileName(self, "Charger les images", "./", "Image Files (*.png *.jpg *.bmp)")[0]
    directory = QFileDialog.getExistingDirectory(self, "Choisir un dossier")
    if(os.path.exists(directory)):
      print("ok")
      # self.control.importImage(filename)
  
  def updateScene(self, image):
    height, width, channel = image.shape
    bytesPerLine = 3 * width
    qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
    self.label.setPixmap(QPixmap.fromImage(qImg))


