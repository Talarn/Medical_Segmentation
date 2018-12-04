import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
#création fenêtre

# vtkWidget = QVTKRenderWindowInteractor()
# layout.addWidget(vtkWidget)
# ren = vtk.vtkRenderer()
# vtkWidget.GetRenderWindow().AddRenderer(ren)
# iren = vtkWidget.GetRenderWindow().GetInteractor()

aRenderer = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(aRenderer)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

#Lecture des coupes 2D

v16 = vtk.vtkDICOMImageReader()
v16.SetDirectoryName("C:/Users/thoma/Desktop/ESME/scannerFolder")
v16.Update()

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
#arter.GetProperty().SetSpecular(.3)
#arter.GetProperty().SetSpecularPower(20)

outlineData = vtk.vtkOutlineFilter()
outlineData.SetInputConnection(v16.GetOutputPort())
mapOutline = vtk.vtkPolyDataMapper()
mapOutline.SetInputConnection(outlineData.GetOutputPort())
outline = vtk.vtkActor()
outline.SetMapper(mapOutline)
outline.GetProperty().SetColor(1,1,1)

#camera
aCamera = vtk.vtkCamera()
aCamera.SetViewUp(0,1,0)
aCamera.SetPosition(0,0,1)
aCamera.SetFocalPoint(0,0,0)
aCamera.ComputeViewPlaneNormal()

###

aRenderer.AddActor(outline)
aRenderer.AddActor(arter)
aRenderer.SetActiveCamera(aCamera)
aRenderer.ResetCamera()
aCamera.Dolly(1)

aRenderer.SetBackground(0,0,0)
renWin.SetSize(640,640)

iren.Initialize()
renWin.Render()
iren.Start()
