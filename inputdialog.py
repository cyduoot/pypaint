from PySide2.QtWidgets import QLineEdit, QDialogButtonBox, QDialog, QFormLayout, QApplication


class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.first = QLineEdit(self)
        self.second = QLineEdit(self)
        self.setWindowTitle("Size of the paintboard")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Width", self.first)
        layout.addRow("Height", self.second)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return (self.first.text(), self.second.text())


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    dialog = InputDialog()
    if dialog.exec():
        print(dialog.getInputs())
    exit(0)
