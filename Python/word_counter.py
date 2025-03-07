"""
Made by Squirrel on 3/6/2025 at 7:04 PM
no license or copyright
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QLabel, QPushButton

class WordCounter(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle('Word counter ig')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()


        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Enter your text here...")
        self.layout.addWidget(self.text_edit)


        self.word_count_label = QLabel("Words: 0", self)
        self.layout.addWidget(self.word_count_label)


        self.char_count_label = QLabel("Characters: 0", self)
        self.layout.addWidget(self.char_count_label)


        self.count_button = QPushButton("Count Words", self)
        self.count_button.clicked.connect(self.count_words)
        self.layout.addWidget(self.count_button)


        self.setLayout(self.layout)

    def count_words(self):
        text = self.text_edit.toPlainText()
        words = text.split()
        num_words = len(words)
        num_characters = len(text.replace(" ", ""))

 
        self.word_count_label.setText(f"Words: {num_words}")
        self.char_count_label.setText(f"Characters: {num_characters}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WordCounter()
    window.show()

    sys.exit(app.exec())
