import sys
from getImagesFromURL import toFolder, toFile, getImages
from PySide6 import QtCore, QtWidgets


class getImagesFromURLGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.url = QtWidgets.QLineEdit("https://github.com/DogukanUrker")
        self.saveName = QtWidgets.QLineEdit()
        self.saveName.setText("Images")
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
        self.layoutRadioButtons = QtWidgets.QHBoxLayout()
        self.layoutRadioButtons.addWidget(self.toFile)
        self.layoutRadioButtons.addWidget(self.toFolder)
        self.layout.addLayout(self.layoutRadioButtons)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.getImagesFromURL)

    @QtCore.Slot()
    def getImagesFromURL(self):
        if self.toFile.isChecked():
            toFile(self.url.text(), self.saveName.text())
            fileName = self.saveName.text().replace(".txt", "")
            self.button.setText(
                f'{len(getImages(self.url.text()))} images saved to "{fileName}.txt" 📄'
            )
        elif self.toFolder.isChecked():
            toFolder(self.url.text(), self.saveName.text())
            self.button.setText(
                f"{len(getImages(self.url.text()))} images saved to /{self.saveName.text()} 📂"
            )


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyleSheet(
        ".QLabel,.QRadioButton,.QPushButton { font-size: 12pt;} QLineEdit { font-size: 11pt;}"
    )
    widget = getImagesFromURLGUI()
    widget.resize(450, 220)
    widget.setWindowTitle("getImagesFromURL")
    widget.show()
    sys.exit(app.exec())
