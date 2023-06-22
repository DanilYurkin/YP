import sys
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit
from PyQt5.QtWidgets import QPushButton, QPlainTextEdit
from data import spisoc

spisoc_el = len(spisoc)
random_number = randint(0, spisoc_el - 1)

task = list(spisoc.values())[random_number]
word = list(spisoc.keys())[random_number]

letters_dictionary = {}
for el in range(len(word)):
    letters_dictionary[el] = [f'{word[el]}', '0']

print(task)
print(word)
print(letters_dictionary)
print('=' * 60)


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

    if index:
        for i in range(len(word)):
            if i == index:
                letter = create_letter(word[i])
                tablo_words_layout.addWidget(letter)
            else:
                letter = create_letter('')
                tablo_words_layout.addWidget(letter)

    tablo_words_box.setLayout(tablo_words_layout)
    return tablo_words_box


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tablo = QVBoxLayout()
        self.tablo.addWidget(create_tablo(index=None))

        self.input_box = QVBoxLayout()
        self.question_label = QLabel(f'Вопрос: {task}', self)
        self.answer_label = QLabel('Ваш ответ: ', self)
        self.answer_field = QLineEdit(self)
        self.answer_button = QPushButton('Отправить', self)
        self.answer_button.clicked.connect(self.enter_click)
        self.log_box = QPlainTextEdit()
        self.log_box.setStyleSheet('min-height: 100px')
        self.log_box.setReadOnly(True)
        self.input_box.addStretch()
        self.input_box.addWidget(self.question_label)
        self.input_box.addWidget(self.answer_label)
        self.input_box.addWidget(self.answer_field)
        self.input_box.addWidget(self.answer_button)
        self.input_box.addWidget(self.log_box)

        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addLayout(self.tablo)
        main_layout.addLayout(self.input_box)

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
            letter_position = []
            for i in range(int(len(word))):
                if answer == word[i]:
                    letter_position.append(i)
                    c = c + 1
                    for ob in reversed(range(self.tablo.count())):
                        item = self.tablo.itemAt(ob)
                        self.tablo.removeItem(item)
                    self.tablo.addWidget(create_tablo(i))
                    print(f'индекс буквы: {i}')
                    letter_name = list(letters_dictionary.values())[i][0]
                    print(f'название буквы: {letter_name}')
                    letter_status = list(letters_dictionary.values())[i][1]
                    print(f'статус буквы: {letter_status}')
                    print('=' * 60)
                    if letter_status == '0':
                        letters_dictionary[i] = [f'{letter_name}', '1']
                    # self.tablo.addWidget(create_tablo(letters_dictionary))
                i += 1
            self.log_box.insertPlainText(f'Буква "{answer}"!\nКоличество букв в слове - {c}\nРасположение: {letter_position}\n')
            print(letters_dictionary)
            print(letter_position)
            # self.tablo.addWidget(create_tablo(letters_dictionary))

        self.answer_field.setText('')


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # window.showMaximized()
    sys.exit(application.exec_())
