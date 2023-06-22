import sys
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit
from PyQt5.QtWidgets import QPushButton, QPlainTextEdit
from data import spisoc

spisoc_el = len(spisoc)  # посчитаем количество элементов в списке spisoc
random_number = randint(0, spisoc_el - 1)

task = list(spisoc.values())[random_number]
word = list(spisoc.keys())[random_number]

print(task)
print(word)


# class InputText(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.question_label = QLabel(f'Вопрос: {task}', self)
#         self.answer_label = QLabel('Ваш ответ: ', self)
#         self.answer_field = QLineEdit(self)
#         self.answer_button = QPushButton('Отправить', self)
#         self.answer_button.clicked.connect(self.on_click)
#         self.log_box = QPlainTextEdit()
#         self.log_box.setStyleSheet('min-height: 100px')
#         self.log_box.setReadOnly(True)
#
#         input_box = QVBoxLayout(self)
#         input_box.addStretch()
#         input_box.addWidget(self.question_label)
#         input_box.addWidget(self.answer_label)
#         input_box.addWidget(self.answer_field)
#         input_box.addWidget(self.answer_button)
#         input_box.addWidget(self.log_box)
#
#         self.setLayout(input_box)
#
#     def on_click(self):
#         answer_field_value = self.answer_field.text()
#         self.answer_label.setText(f'Ваш ответ: {answer_field_value}')
#
#         answer = answer_field_value
#         if len(answer) > 1:
#             if answer == word:
#                 self.log_box.setPlainText('вы выиграли')
#             else:
#                 self.log_box.setPlainText('вы проиграли')
#         else:
#             c = 0
#             word_position = []
#             for i in range(int(len(word))):
#                 if answer == word[i]:
#                     word_position.append(f'по счёту №{i + 1}')
#                     c = c + 1
#                     Tablo(i)
#                 i += 1
#             self.log_box.insertPlainText(f'Буква "{answer}"!\nКоличество штук в слове - {c}\n{word_position}\n')
#
#         self.answer_field.setText('')


def create_letter(text):
    letter = QLabel()
    letter.setText(text)
    letter.setAlignment(Qt.AlignCenter)
    letter.setStyleSheet('''    background-color: #ddd; 
                                border: 2px solid #444; 
                                margin: 10px; 
                                padding: 15px; 
                                font: bold 20px;''')
    return letter


def create_tablo(index):
    tablo_words_box = QWidget()
    tablo_words_layout = QHBoxLayout()

    if index is None:
        for i in range(len(word)):
            letter = create_letter('')
            tablo_words_layout.addWidget(letter)
    else:
        for i in range(len(word)):
            if i == index:
                letter = create_letter(word[i])
                tablo_words_layout.addWidget(letter)
            else:
                letter = create_letter('')
                tablo_words_layout.addWidget(letter)

    tablo_words_box.setLayout(tablo_words_layout)
    return tablo_words_box


# class Tablo(QVBoxLayout):
#     def __init__(self, index=None):
#         super().__init__()
#
#         self.addStretch()
#
#         if index is None:
#             tablo = create_tablo(index)
#             self.addWidget(tablo)
#
#             print(f'число вложенных объектов: {self.count()}')
#             for i in reversed(range(self.count())):
#                 print(f'элемент №{i}')
#                 print(self.itemAt(i).widget())
#
#         if index:
#             new_tablo = create_tablo(index)
#             self.addWidget(new_tablo)
#
#             print(f'число вложенных объектов: {self.count()}')
#             for i in reversed(range(self.count())):
#                 print(f'элемент №{i}')
#                 print(self.itemAt(i).widget())
#                 # self.itemAt(i).widget().setParent(None)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # tablo = Tablo(2)
        self.tablo = QVBoxLayout()
        self.tablo.addWidget(create_tablo(index=None))

        # input_text = InputText()
        input_box = QVBoxLayout()
        self.question_label = QLabel(f'Вопрос: {task}', self)
        self.answer_label = QLabel('Ваш ответ: ', self)
        self.answer_field = QLineEdit(self)
        self.answer_button = QPushButton('Отправить', self)
        self.answer_button.clicked.connect(self.enter_click)
        self.log_box = QPlainTextEdit()
        self.log_box.setStyleSheet('min-height: 100px')
        self.log_box.setReadOnly(True)
        input_box.addStretch()
        input_box.addWidget(self.question_label)
        input_box.addWidget(self.answer_label)
        input_box.addWidget(self.answer_field)
        input_box.addWidget(self.answer_button)
        input_box.addWidget(self.log_box)

        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addLayout(self.tablo)
        main_layout.addLayout(input_box)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

    def enter_click(self):
        answer_field_value = self.answer_field.text()
        self.answer_label.setText(f'Ваш ответ: {answer_field_value}')

        answer = answer_field_value
        if len(answer) > 1:
            if answer == word:
                self.log_box.setPlainText('вы выиграли')
            else:
                self.log_box.setPlainText('вы проиграли')
        else:
            c = 0
            word_position = []
            for i in range(int(len(word))):
                if answer == word[i]:
                    word_position.append(f'по счёту №{i + 1}')
                    c = c + 1
                    for ob in reversed(range(self.tablo.count())):
                        item = self.tablo.itemAt(ob)
                        self.tablo.removeItem(item)
                    self.tablo.addWidget(create_tablo(i))
                i += 1
            self.log_box.insertPlainText(f'Буква "{answer}"!\nКоличество штук в слове - {c}\n{word_position}\n')

        self.answer_field.setText('')


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # window.showMaximized()
    sys.exit(application.exec_())
