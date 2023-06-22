import sys
from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit, \
    QPushButton, QPlainTextEdit

from data import spisoc

spisoc_el = len(spisoc)  # посчитаем количество элементов в списке spisoc
random_number = randint(0, spisoc_el - 1)

task = list(spisoc.values())[random_number]
word = list(spisoc.keys())[random_number]

print(task)
print(word)


class InputText(QWidget):
    def __init__(self):
        super().__init__()

        self.text_label = QLabel('Ваш ответ: ', self)
        self.text_field = QLineEdit(self)
        self.button = QPushButton('Отправить', self)
        self.button.clicked.connect(self.on_click)
        self.text_box = QPlainTextEdit()
        self.text_box.setStyleSheet('min-height: 100px')
        self.text_box.setReadOnly(True)

        horizontal_box = QVBoxLayout(self)
        horizontal_box.addWidget(self.text_label)
        horizontal_box.addWidget(self.text_field)
        horizontal_box.addWidget(self.button)
        horizontal_box.addWidget(self.text_box)

        self.setLayout(horizontal_box)

    def on_click(self):
        text_field_value = self.text_field.text()
        self.text_label.setText(f'Ваш ответ: {text_field_value}')

        answer = text_field_value
        if len(answer) > 1:
            if answer == word:
                self.text_box.setPlainText('вы выграли')
            else:
                self.text_box.setPlainText('вы проиграли')
        else:
            c = 0
            word_position = []
            for i in range(int(len(word))):
                if answer == word[i]:
                    word_position.append(f'{i + 1} по счету')
                    c = c + 1
                i += 1
            self.text_box.insertPlainText(f'Буква "{answer}"!\nКоличество штук в слове - {c}\n{word_position}\n')

        self.text_field.setText('')


class Tablo(QWidget):
    def __init__(self):
        super().__init__()

        horizontal_box = QHBoxLayout(self)
        for i in range(len(word)):
            self.letter = Letter(word[i], self)
            # self.letter = Letter('', self)
            horizontal_box.addWidget(self.letter)
        self.setLayout(horizontal_box)


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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        tablo = Tablo()
        input_text = InputText()

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
