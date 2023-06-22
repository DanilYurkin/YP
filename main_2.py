import sys
from random import randint
from PyQt5.QtCore import Qt
from data import spisoc
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel

spisoc_el = len(spisoc)  # посчитаем количество элементов в списке spisoc
random_number = randint(0, spisoc_el - 1)

task = list(spisoc.values())[random_number]
word = list(spisoc.keys())[random_number]

print(task)
print(word)


class Letter(QLabel):
    def __init__(self, text, parent=None):
        super(Letter, self).__init__(text, parent)
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet('''  background-color: #ddd; 
                                border: 2px solid #444; 
                                margin: 10px; 
                                padding: 15px; 
                                font: bold 20px;''')


class Tablo(QWidget):
    def __init__(self):
        super().__init__()
        self.letter = None
        self.initUI()

    def initUI(self):
        horizontal_box = QHBoxLayout(self)
        for i in range(len(word)):
            self.letter = Letter(word[i], self)
            # self.letter = Letter('', self)
            horizontal_box.addWidget(self.letter)
        self.setLayout(horizontal_box)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = Tablo()
        self.setCentralWidget(self.widget)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())
