from View import *
from Controller import *
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
  app = QApplication(sys.argv)
  a = View()
  b = Controller(a)
  a.setControl(b)
  a.show()
  sys.exit(app.exec_())