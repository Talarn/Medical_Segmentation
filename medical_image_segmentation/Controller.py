import cv2

class Controller(object):

  def __init__(self, view):
    self.view = view

  def importImage(self, imagePath):
    image = cv2.imread(imagePath)
    self.view.updateScene(image)
    print(imagePath)