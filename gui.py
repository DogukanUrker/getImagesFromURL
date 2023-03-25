import sys
from getImagesFromURL import toFolder, toTXT
from PySide6 import QtCore, QtWidgets, QtGui


class getImagesFromURLGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.url = QtWidgets.QLineEdit(
            "https://en.wikipedia.org/wiki/Mustafa_Kemal_Atat%C3%BCrk"
        )
        self.saveName = QtWidgets.QLineEdit()
        self.saveName.setText("images")
        self.button = QtWidgets.QPushButton("Save 💾")
        self.radioLabel = QtWidgets.QLabel("Save images to ...")
        self.saveNameLabel = QtWidgets.QLabel("File/Folder name:")
        self.toFile = QtWidgets.QRadioButton("File 📄")
        self.toFolder = QtWidgets.QRadioButton("Folder 📂")
        self.toFile.setObjectName("toFile")
        self.toFolder.setObjectName("toFolder")
        self.toFolder.setChecked(True)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.url)
        self.layout.addWidget(self.saveNameLabel)
        self.layout.addWidget(self.saveName)
        self.layout.addWidget(self.radioLabel)
        self.layoutRadioButtons = QtWidgets.QHBoxLayout(self)
        self.layoutRadioButtons.addWidget(self.toFile)
        self.layoutRadioButtons.addWidget(self.toFolder)
        self.layout.addLayout(self.layoutRadioButtons)
        self.layout.addWidget(self.button)
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
    widget.resize(400, 0)
    widget.show()

    sys.exit(app.exec())
