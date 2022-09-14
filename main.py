import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import loadUiType
import os

from PySide6 import QtCore, QtGui, QtWidgets

import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(current_dir, "UIs/main.ui"))


class Main(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('theme/icon.png'))
        self.setWindowTitle("FFmpeg GUI")
        self.setFixedSize(320, 140)

        self.InputEdit = self.InputField.itemAt(1).widget()
        self.InputEditButton = self.InputField.itemAt(2).widget()
        self.InputDialog = QtWidgets.QFileDialog(self)

        self.ConvertEdit = self.ConvertField.itemAt(0).widget()
        
        self.ConvertButton.clicked.connect(self.Convert)
        self.InputEditButton.clicked.connect(self.SetDirectory)

    def Convert(self, Input):
        subprocess.Popen(["ffmpeg/ffmpeg.exe", "-i", f"{self.InputEdit.text()}", f"{os.path.splitext(self.InputEdit.text())[0]}{self.ConvertEdit.text()}"])

    def SetDirectory(self):
        SelectedDirectory = self.InputDialog.getOpenFileName()
        self.InputEdit.setText(SelectedDirectory[0])

if __name__ == "__main__":
    app = QApplication([])
    widget = Main()

    widget.setStyleSheet(open("theme/style.qss").read())
    widget.show()

    sys.exit(app.exec())