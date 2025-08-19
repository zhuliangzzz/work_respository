#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:ZipDir.py
   @author:zl
   @time: 2025/7/17 10:15
   @software:PyCharm
   @desc:
"""
import datetime
import shutil
import sys
import qtawesome
import pyzipper
import os
import base64

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

import ZipDirUI as ui
import res_rc

log = 'encrypt.log'


def base64_encode(str):
    encoded_bytes = base64.b64encode(str.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str


def encrypt_folder(folder_path, output_zip, password=None):
    """
    使用AES-256加密整个文件夹到ZIP文件
    :param folder_path: 要加密的文件夹路径
    :param output_zip: 输出的ZIP文件路径
    :param password: 加密密码
    """
    encryption = pyzipper.WZ_AES if password else None
    # 判断是压缩文件还是压缩文件夹
    if os.path.isfile(folder_path):
        output_zip = '%s.zip' % os.path.splitext(output_zip.rsplit('.zip')[0])[0]
        try:
            with pyzipper.AESZipFile(output_zip, 'w', encryption=encryption) as zf:
                if password:
                    zf.setpassword(password.encode('utf-8'))
                    with open(log, 'a') as f:
                        f.write("[%s]%s encrypt >> %s\n" % (
                        datetime.datetime.now().strftime('%y%m%d%H%M%S'), folder_path, base64_encode(password)))
                zf.write(folder_path, arcname=os.path.basename(folder_path))
            print(f"加密成功：{output_zip}")
            return True
        except Exception as e:
            print(f"加密失败：{str(e)}")
            return False
    else:
        try:
            with pyzipper.AESZipFile(
                    output_zip,
                    'w',
                    compression=pyzipper.ZIP_DEFLATED,
                    encryption=encryption
            ) as zipf:
                if password:
                    zipf.setpassword(password.encode('utf-8'))
                    with open(log, 'a') as f:
                        f.write("[%s]%s encrypt >> %s\n" % (
                        datetime.datetime.now().strftime('%y%m%d%H%M%S'), folder_path, base64_encode(password)))
                for root, _, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, arcname)
            print(f"加密成功：{output_zip}")
            return True
        except Exception as e:
            print(f"加密失败：{str(e)}")
            return False


def decrypt_zip(zip_path, output_folder, password=None):
    """
    解密AES-256加密的ZIP文件
    :param zip_path: ZIP文件路径
    :param output_folder: 解压目录
    :param password: 解密密码
    """
    try:
        with pyzipper.AESZipFile(zip_path, 'r') as zipf:
            if password:
                zipf.setpassword(password.encode('utf-8'))
            zipf.extractall(output_folder)
        print(f"解密成功：{output_folder}")
        return True
    except Exception as e:
        print(f"解密失败：{str(e)}")
        return False


class ZipDir(QWidget, ui.Ui_Form):
    def __init__(self):
        super(ZipDir, self).__init__()
        self.setupUi(self)
        self.render()

    def render(self):
        self.pushButton_select_dir.setIcon(qtawesome.icon('fa.folder-open', color='white'))
        self.pushButton_select_zip.setIcon(qtawesome.icon('fa.file', color='white'))
        self.pushButton_compression.setIcon(qtawesome.icon('mdi.vector-union', color='white'))
        self.pushButton_decompression.setIcon(qtawesome.icon('mdi.source-merge', color='white'))
        self.pushButton_exit.setIcon(qtawesome.icon('fa.sign-out', color='white'))
        self.pushButton_select_dir.clicked.connect(self.select_dir)
        self.pushButton_select_zip.clicked.connect(self.select_zip)
        self.pushButton_compression.clicked.connect(self.compression)
        self.pushButton_decompression.clicked.connect(self.decompression)
        self.pushButton_exit.clicked.connect(lambda: sys.exit())
        self.setStyleSheet('''QPushButton{font:10pt;background-color:#459B81;color:white;} QPushButton:hover{background:#333;}
                ''')

        self.move(int((app.desktop().width() - self.geometry().width()) / 2),
                  int((app.desktop().height() - self.geometry().height()) / 2))

    def select_dir(self):
        dir = QFileDialog.getExistingDirectory(self, '选择文件夹', '*')
        print(dir)
        if dir:
            self.lineEdit_dir.setText(dir)

    def select_zip(self):
        file, _ = QFileDialog.getOpenFileName(self, '选择文件', '*')
        print(file)
        if file:
            self.lineEdit_dir.setText(file)

    def compression(self):
        folder_path = self.lineEdit_dir.text().strip()
        password = self.lineEdit_pwd.text()
        if not folder_path:
            QMessageBox.warning(self, 'warning', '请选择文件/文件夹进行压缩!')
            return
        res = encrypt_folder(folder_path, '%s.zip' % folder_path, password)
        if res:
            QMessageBox.information(self, 'tips', '压缩成功！压缩文件为%s.zip' % folder_path)
            if self.checkBox.isChecked():
                shutil.rmtree(folder_path)
        else:
            QMessageBox.warning(self, 'warning', '压缩失败!')

    def decompression(self):
        zip = self.lineEdit_dir.text().strip()
        password = self.lineEdit_pwd.text()
        if not zip:
            QMessageBox.warning(self, 'warning', '请先选择zip文件!')
            return
        if not zip.endswith('.zip'):
            QMessageBox.warning(self, 'tips', '请选择zip格式文件解压缩!')
            return
        suffix = datetime.datetime.now().strftime('%y%m%d%H%M%S')
        res = decrypt_zip(zip, os.path.join(os.path.dirname(zip), '%s%s' % (os.path.basename(zip).replace('.zip', ''), suffix)), password)
        if res:
            QMessageBox.information(self, 'tips', '解压缩成功！解压缩文件夹为%s' % os.path.join(os.path.dirname(zip), '%s%s' % (os.path.basename(zip).replace('.zip', ''), suffix)))
            if self.checkBox.isChecked():
                os.unlink(zip)
        else:
            shutil.rmtree(
                os.path.join(os.path.dirname(zip), '%s%s' % (os.path.basename(zip).replace('.zip', ''), suffix)))
            QMessageBox.warning(self, 'warning', '解压缩失败!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    app.setWindowIcon(QIcon(':/res/tian.jpg'))
    win = ZipDir()
    win.show()
    sys.exit(app.exec_())
