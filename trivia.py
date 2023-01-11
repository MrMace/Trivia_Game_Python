import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Who wants to play Trivia?!?")
window.setFixedWidth(1000)
window.move(2700, 200)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

#display the logo
image = QPixmap("logo.png")
logo = QLabel()
logo.setPixmap(image)
logo.setAlignment(QtCore.Qt.AlignCenter)
logo.setStyleSheet("margin: 100px 0")

#Button Widget
button = QPushButton("PLAY")
button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
button.setStyleSheet("*{border: 4px solid '#BF40BF';" +
                     "border-radius: 45px;" +
                     "font-size:35px;" +
                     "color: '#fff'; " +
                     "padding: 25px 0;" +
                     "margin: 100px 200px;}" +
                     "*:hover{background: '#BF40BF';}"
                     ) 

grid.addWidget(logo, 0, 0)
grid.addWidget(button, 1, 0)

window.setLayout(grid)
window.show()
sys.exit(app.exec())