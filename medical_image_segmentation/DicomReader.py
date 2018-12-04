######################################
# A METTRE DANS UNE CLASSE DicomReader
    # Chargement des coupes
    # self.vtkImageReader = vtk.vtkDICOMImageReader()
    # self.vtkImageReader.SetDirectoryName("D:/Projet_3CT/Data_IRM/02-OS/")
    # self.vtkImageReader.Update()
######################################

from vtk import vtkDICOMImageReader
import pydicom
import glob
import time
import os

class DicomReader(vtkDICOMImageReader):

  def __init__(self):
    vtkDICOMImageReader.__init__(self)
  
  def loadDataset(self, folderName):
    self.SetDirectoryName(folderName)
    self.Update()

  def readDicomDatasets(self, folderName):
    """ Rajouter des sécurités """
    dicomDatasetArray = []
    for path in sorted(glob.glob(folderName + "/*")): #Image à trier dans le bon ordre
      # print(path)
      dicom = pydicom.dcmread(path)
      dicomDatasetArray.append(dicom.pixel_array)
    return dicomDatasetArray


if __name__ == '__main__':
  a = DicomReader()
  start = time.time()
  dicomdatasets = a.readDicomDatasets("D:/Projet_3CT/Data_IRM/02-OS/")
  end = time.time()
  print(end - start)
  print(dicomdatasets[0].shape)
  print(len(dicomdatasets))