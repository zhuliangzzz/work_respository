#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:test.py
   @author:zl
   @time: 2025/8/18 10:56
   @software:PyCharm
   @desc:
"""
from PIL import Image, ImageDraw

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QPushButton, QDialog, QLineEdit,
                             QMessageBox, QLabel, QDialogButtonBox)


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        layout = QVBoxLayout()

        self.btn = QPushButton("打开对话框")
        self.btn.clicked.connect(self.show_dialog)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def show_dialog(self):
        dialog = MyDialog(self)
        dialog.exec_()


class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("验证对话框")
        layout = QVBoxLayout()

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        # 使用标准按钮盒
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.validate_input)  # 连接到验证函数
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)

        self.setLayout(layout)

    def validate_input(self):
        text = self.line_edit.text()
        if not text:
            QMessageBox.warning(self, "警告", "输入不能为空!")
            return  # 不执行后续代码

        # 验证通过后的处理
        self.accept()


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWidget()
    widget.show()
    app.exec_()