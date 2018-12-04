
# ######################################
# # A METTRE DANS UNE CLASSE VolumeRendering
#     arterExtractor = vtk.vtkContourFilter()
#     arterExtractor.SetInputConnection(self.vtkImageReader.GetOutputPort())
#     arterExtractor.SetValue(0, 350)
#     arterNormals = vtk.vtkPolyDataNormals() #Passage de la matrice de pixels à des coordonées géométriques / 3D
#     arterNormals.SetInputConnection(arterExtractor.GetOutputPort())
#     arterNormals.SetFeatureAngle(100.0)
#     arterStripper = vtk.vtkStripper() #Génération d'un ensemble de polygone à partir des coordonées calculées précédemment
#     arterStripper.SetInputConnection(arterNormals.GetOutputPort())
#     arterMapper = vtk.vtkPolyDataMapper() #Permet de passer des polygones à des formes géométriques graphiques
#     arterMapper.SetInputConnection(arterStripper.GetOutputPort())
#     arterMapper.ScalarVisibilityOff()
#     arter = vtk.vtkActor() #Objet dans un scène de rendu (comprends l'objet + éclairage + texture)
#     arter.SetMapper(arterMapper)
#     arter.GetProperty().SetDiffuseColor(1, 1, .9412)
  
#     outlineData = vtk.vtkOutlineFilter()
#     outlineData.SetInputConnection(self.vtkImageReader.GetOutputPort())
#     mapOutline = vtk.vtkPolyDataMapper()
#     mapOutline.SetInputConnection(outlineData.GetOutputPort())
#     outline = vtk.vtkActor()
#     outline.SetMapper(mapOutline)
#     outline.GetProperty().SetColor(1,1,1)
# ######################################