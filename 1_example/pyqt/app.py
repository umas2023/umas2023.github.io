import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("hello world")
        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(800, 600))
        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
# Start the event loop.
app.exec()