import sys
import random
from getImagesFromURL import toFolder, toTXT
from PySide6 import QtCore, QtWidgets, QtGui


class getImagesFromURLGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.url = QtWidgets.QLineEdit("url")
        self.saveName = QtWidgets.QLineEdit("file/folder name")
        self.saveName.setText("images")
        self.button = QtWidgets.QPushButton("save images")
        self.toFile = QtWidgets.QRadioButton("file")
        self.toFolder = QtWidgets.QRadioButton("folder")
        self.toFile.setObjectName("toFile")
        self.toFolder.setObjectName("toFolder")
        self.toFolder.setChecked(True)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.url)
        self.layout.addWidget(self.saveName)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.toFile)
        self.layout.addWidget(self.toFolder)
        self.button.clicked.connect(self.getImagesFromURL)

    @QtCore.Slot()
    def getImagesFromURL(self):
        if self.toFile.isChecked():
            toTXT(self.url.text(), self.saveName.text())
        elif self.toFolder.isChecked():
            toFolder(self.url.text(), self.saveName.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = getImagesFromURLGUI()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec())
