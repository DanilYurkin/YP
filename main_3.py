import sys
from random import randint
from PyQt5.QtCore import Qt
from data import spisoc
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit, \
    QMessageBox, QPushButton

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


class Input(QWidget):
    def __init__(self):
        super().__init__()

        self.text_label = QLabel('Ваш ответ: ', self)
        self.text_box = QLineEdit(self)
        self.button = QPushButton('Отправить', self)
        self.button.clicked.connect(self.on_click)

        horizontal_box = QVBoxLayout(self)
        horizontal_box.addWidget(self.text_label)
        horizontal_box.addWidget(self.text_box)
        horizontal_box.addWidget(self.button)

        self.setLayout(horizontal_box)

    def on_click(self):
        text_box_value = self.text_box.text()
        self.text_label.setText(f'Ваш ответ: {text_box_value}')
        self.text_box.setText('')


class Tablo(QWidget):
    def __init__(self):
        super().__init__()

        horizontal_box = QHBoxLayout(self)
        for i in range(len(word)):
            self.letter = Letter(word[i], self)
            # self.letter = Letter('', self)
            horizontal_box.addWidget(self.letter)
        self.setLayout(horizontal_box)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        tablo = Tablo()
        input_text = Input()

        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addWidget(tablo)
        main_layout.addWidget(input_text)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())
