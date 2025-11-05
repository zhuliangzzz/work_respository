#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:VNC_Management.py
   @author:zl
   @time: 2025/10/30 10:15
   @software:PyCharm
   @desc:
"""
import datetime
import json
import os.path
import sys
import time

import qtawesome
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import VNC_ManagementUI as ui
import AssignUserUI as assign_user_ui
import AddUserUI as add_user_ui
import res_rc


class VNC_Management(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.isChanged = False
        self.setupUi(self)
        self.render()

    def render(self):
        self.loaded_dict = {}
        self.json_file = 'ip_dictionary.json'
        with open(self.json_file, 'r', encoding='utf-8') as f:
            self.loaded_dict = json.load(f)
        print(self.loaded_dict)
        self.comboBox_query.addItems(['工号', '姓名'])
        header = ['ip', '工号', '姓名']
        self.tableWidget.setColumnCount(len(header))
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        # self.tableWidget.setSortingEnabled(True)
        self.lineEdit.returnPressed.connect(self.search)
        self.comboBox_ip.addItem('全部显示')
        self.comboBox_ip.addItems(self.loaded_dict.keys())
        self.comboBox_ip.currentIndexChanged.connect(self.loadTable)
        self.loadTable()
        self.action_add.setIcon(qtawesome.icon('ri.user-add-line', color='#dc3545'))
        self.action_mv.setIcon(qtawesome.icon('mdi.distribute-vertical-center', color='#dc3545'))
        self.action_del.setIcon(qtawesome.icon('mdi.delete-circle-outline', color='#dc3545'))
        self.action_save.setIcon(qtawesome.icon('mdi.content-save', color='#dc3545'))
        self.action_flush.setIcon(qtawesome.icon('mdi.reload', color='#dc3545'))
        self.action_json.setIcon(qtawesome.icon('mdi.json', color='#dc3545'))
        self.action_xlsx.setIcon(qtawesome.icon('mdi.file-excel', color='#dc3545'))
        self.menuFile.triggered.connect(self.pressAction)
        self.menuOutput.triggered.connect(self.pressAction)
        header_style = """
                        QHeaderView {
                            background-color: #464646;
                            color: white;
                            font-weight: bold;
                            font-size: 14px;
                        }
                        """
        self.tableWidget.horizontalHeader().setStyleSheet(header_style)

        self.setStyleSheet(
            """
            QTableWidget::Item:selected{background:#dc3545;color:white;}
            QComboBox{background-color:#464646;color:white;}
            QComboBox QAbstractItemView {
                background-color: #464646;
                border: 1px solid #ccc;
                selection-background-color: white;
                selection-color: #464646;
                outline: none;
            }
            QPushButton {
                background-color: #464646;
                color: white;
                border-radius: 8px;
                font-weight: bold;
                font-size: 11px;
                min-height: 18px;
                min-width: 50px;
            }
            QStatusBar {color:green;}
            QMessageBox{font:10pt;}""")

    def pressAction(self, act):
        print(act.text())
        if act.text() == '添加人员':
            self.add_data()
            # self.add_user()
        elif act.text() == '分配所选':
            self.assign_sel_data()
            # self.update_table()
        elif act.text() == '删除所选':
            self.del_sel_data()
        elif act.text() == '保存':
            self.save_data()
            # self.reset_data()
        elif act.text() == '刷新':
            with open(self.json_file, 'r', encoding='utf-8') as f:
                self.loaded_dict = json.load(f)
            self.flush()
        elif act.text() == '导出json':
            self.export('json')
        elif act.text() == '导出xlsx':
            self.export('xlsx')

    def add_data(self):
        _dialog = AddUserDialog(self.loaded_dict, self)
        _dialog.user_return_signal.connect(self.add_user)
        _dialog.exec_()

    def assign_sel_data(self):
        selected_indexs = self.tableWidget.selectedIndexes()
        print(selected_indexs)
        if not selected_indexs:
            QMessageBox.information(self, "提示", "请先选择要分配的行！")
            return
        selected_rows = set()
        for index in selected_indexs:
            selected_rows.add(index.row())
        selected_rows = sorted(selected_rows)
        dict_data = {}
        for row in selected_rows:
            ip_data = self.tableWidget.item(row, 0).text()
            id_data = int(self.tableWidget.item(row, 1).text())
            name_data = self.tableWidget.item(row, 2).text()
            target = {'id': id_data, 'name': name_data}
            if ip_data not in dict_data:
                dict_data[ip_data] = []
            dict_data[ip_data].append(target)
        assign_dialog = AssignDialog(self.loaded_dict, dict_data, self)
        assign_dialog.ip_return_signal.connect(self.assign_ip)
        assign_dialog.exec_()

    def assign_ip(self, ip):
        selected_indexs = self.tableWidget.selectedIndexes()
        selected_rows = set()
        for index in selected_indexs:
            selected_rows.add(index.row())
        selected_rows = sorted(selected_rows)
        dict_data = {}
        for row in selected_rows:
            ip_data = self.tableWidget.item(row, 0).text()
            id_data = int(self.tableWidget.item(row, 1).text())
            name_data = self.tableWidget.item(row, 2).text()
            target = {'id': id_data, 'name': name_data}
            if ip not in dict_data:
                dict_data[ip] = []
            dict_data[ip].append(target)
            # 清除选择的数据
            remain = [item for item in self.loaded_dict[ip_data] if item != target]
            if not remain:
                del self.loaded_dict[ip_data]
            else:
                self.loaded_dict[ip_data] = remain
        for key, val in dict_data.items():
            if key not in self.loaded_dict:
                self.loaded_dict[key] = []
            self.loaded_dict[key].extend(val)
        self.statusbar.showMessage('已将选择的用户更新到IP：192.168.39.%s' % ip)
        self.tableWidget.clearSelection()
        self.isChanged = True
        self.flush()

    def add_user(self, *user):
        print(user)
        self.isChanged = True
        ip_data, id_data, name_data = user[0]
        data = {'id': id_data, 'name': name_data}
        if ip_data not in self.loaded_dict:
            self.loaded_dict[ip_data] = []
        self.loaded_dict[ip_data].append(data)
        self.statusbar.showMessage('已添加用户%s更新到IP：192.168.39.%s' % (id_data, ip_data))
        self.flush()

    def del_sel_data(self):
        selected_indexs = self.tableWidget.selectedIndexes()
        if not selected_indexs:
            QMessageBox.information(self, "提示", "请先选择要删除的行！")
            return
        # 获取所有选中的行索引（去重并排序）
        selected_rows = set()
        for index in selected_indexs:
            selected_rows.add(index.row())
        selected_rows = sorted(selected_rows, reverse=True)  # 从后往前删除
        for row in selected_rows:
            self.tableWidget.removeRow(row)
        #
        ip = self.comboBox_ip.currentText()
        dict_data = {}
        for row in range(self.tableWidget.rowCount()):
            ip_data = self.tableWidget.item(row, 0).text()
            id_data = int(self.tableWidget.item(row, 1).text())
            name_data = self.tableWidget.item(row, 2).text()
            if ip_data not in dict_data:
                dict_data[ip_data] = []
            dict_data[ip_data].append({'id': id_data, 'name': name_data})
        if ip == '全部显示':
            del_iplist = list(filter(lambda key: key not in dict_data, self.loaded_dict.keys()))
            if del_iplist:
                for del_ip in del_iplist:
                    del self.loaded_dict[del_ip]
        else:
            if not dict_data:
                del self.loaded_dict[ip]
        self.loaded_dict.update(dict_data)
        self.isChanged = True
        self.flush()

    def save_data(self):
        print(self.loaded_dict)
        if not self.isChanged:
            QMessageBox.information(self, "提示", "未修改不需要保存！")
            return
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(self.loaded_dict, f, ensure_ascii=False, indent=2)
        app.processEvents()
        self.statusbar.showMessage("已保存！！！")
        self.isChanged = False
        app.processEvents()
        time.sleep(2)
        self.flush()

    def flush(self):
        self.lineEdit.clear()
        ip = self.comboBox_ip.currentText()
        self.comboBox_ip.currentIndexChanged.disconnect(self.loadTable)
        self.comboBox_ip.clear()
        self.comboBox_ip.addItem('全部显示')
        self.comboBox_ip.addItems(self.loaded_dict.keys())
        self.comboBox_ip.currentIndexChanged.connect(self.loadTable)
        if ip not in self.loaded_dict:
            self.comboBox_ip.setCurrentIndex(0)
        else:
            self.comboBox_ip.setCurrentText(ip)
        self.loadTable()

    def loadTable(self):
        # self.comboBox_ip.currentIndexChanged.disconnect(self.loadTable)
        # self.comboBox_ip.clear()
        # self.comboBox_ip.addItem('全部显示')
        # self.comboBox_ip.addItems(self.loaded_dict.keys())
        # self.comboBox_ip.currentIndexChanged.connect(self.loadTable)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        data_count = 0
        ip = self.comboBox_ip.currentText()
        # if ip not in self.loaded_dict:
        #     self.comboBox_ip.setCurrentIndex(0)
        if ip == '全部显示':
            for k, users in self.loaded_dict.items():
                data_count += len(users)
            self.tableWidget.setRowCount(data_count)
            row = 0
            for k, users in self.loaded_dict.items():
                for user in users:
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(k))
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(str(user.get('id'))))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(user.get('name')))
                    row += 1
            self.statusbar.showMessage('人员数量：%s' % row)
        else:
            data_count = len(self.loaded_dict.get(ip))
            self.tableWidget.setRowCount(data_count)
            for row, user in enumerate(self.loaded_dict.get(ip)):
                self.tableWidget.setItem(row, 0, QTableWidgetItem(ip))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(user.get('id'))))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(user.get('name')))
            self.statusbar.showMessage('人员数量：%s' % len(self.loaded_dict.get(ip)))

    def search(self):
        self.tableWidget.clearSelection()
        keyword = self.lineEdit.text().strip()
        search_column = 1 if self.comboBox_query.currentIndex() == 0 else 2
        search_row = None
        for row in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row, search_column).text() == keyword:
                search_row = row
                break
        if search_row is None:
            QMessageBox.information(self, 'tips', '未查询到%s' % keyword)
        else:
            self.tableWidget.selectRow(self.tableWidget.item(search_row, search_column).row())
            self.tableWidget.scrollToItem(self.tableWidget.item(search_row, search_column),
                                          QTableWidget.PositionAtCenter)

    def export(self, type):
        directory = QFileDialog.getExistingDirectory(
            self,
            "选择文件夹",
            "./",
            QFileDialog.ShowDirsOnly  # 只显示文件夹
        )
        if directory:
            print(directory)
            filename = os.path.join(directory,"vnc_managment_" + datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
            if type == 'json':
                with open(f'{filename}.json', 'w', encoding='utf-8') as f:
                    json.dump(self.loaded_dict, f, ensure_ascii=False, indent=2)
                self.statusbar.showMessage(f'已保存至{filename}.json')
            else:
                export_data = []
                for k, users in self.loaded_dict.items():
                    for user in users:
                        export_data.append([k, user.get('id'), user.get('name')])
                df = pd.DataFrame(export_data)
                df.to_excel(f'{filename}.xlsx', index=False, header=['IP', '工号', '姓名'])
                self.statusbar.showMessage(f'已保存至{filename}.xlsx')
        else:
            QMessageBox.information(self, "提示", "未选择任何文件夹")



class AssignDialog(QDialog, assign_user_ui.Ui_Dialog):
    ip_return_signal = pyqtSignal(str)
    def __init__(self, loaded_dict, assign_data, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.loaded_dict = loaded_dict
        self.assign_data = assign_data
        self.render()

    def render(self):
        self.setWindowTitle('分配ip')
        header = ['ip', '工号', '姓名']
        self.tableWidget.setColumnCount(len(header))
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        # self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.comboBox.addItems(self.loaded_dict.keys())
        self.buttonBox.accepted.connect(self.assign_ip)
        self.loadTable()
        self.comboBox.setStyleSheet('''
        QComboBox {background-color: #464646;
        color:white;}
        QAbstractItemView {
                background-color: #464646;
                color:white;
                border: 1px solid #ccc;
                selection-background-color: white;
                selection-color: #464646;
                outline: none;
            }''')
        header_style = """
                QHeaderView::section {
                    background-color: #464646;
                    color: white;
                    font-weight: bold;
                    font-size: 12px;
                }
                """
        self.tableWidget.horizontalHeader().setStyleSheet(header_style)

        self.buttonBox.setStyleSheet("""
         QPushButton {
                background-color: #27ae60;
                color: white;
                border: 2px solid #219653;
                border-radius: 8px;
                padding: 12px 24px;
                font-weight: bold;
                font-size: 14px;
                min-height: 20px;
            }""")
        self.setStyleSheet("""*{font-family: 微软雅黑;font-size:10pt;} 
        
        """)

    def loadTable(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        print(self.assign_data)
        data_count = 0
        for users in self.assign_data.values():
            data_count += len(users)
        self.tableWidget.setRowCount(data_count)
        row = 0
        for k, users in self.assign_data.items():
            for user in users:
                self.tableWidget.setItem(row, 0, QTableWidgetItem(k))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(user.get('id'))))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(user.get('name')))
                row += 1

    def assign_ip(self):
        ip = self.comboBox.currentText()
        self.ip_return_signal.emit(ip)


class AddUserDialog(QDialog, add_user_ui.Ui_Dialog):
    user_return_signal = pyqtSignal(list)

    def __init__(self, loaded_dict,parent=None):
        super().__init__(parent)
        self.loaded_dict = loaded_dict
        self.setupUi(self)
        self.render()

    def render(self):
        self.comboBox.addItems(self.loaded_dict.keys())
        self.lineEdit.setValidator(QIntValidator())
        # self.buttonBox.accepted.connect(self.accept)
        self.comboBox.setStyleSheet('''
        QComboBox {background-color: #464646;
        color:white;}
        QAbstractItemView {
                background-color: #464646;
                color:white;
                border: 1px solid #ccc;
                selection-background-color: white;
                selection-color: #464646;
                outline: none;
            }''')
        self.buttonBox.setStyleSheet("""
         QPushButton {
                background-color: #27ae60;
                color: white;
                border: 2px solid #219653;
                border-radius: 8px;
                padding: 12px 24px;
                font-weight: bold;
                font-size: 14px;
                min-height: 20px;
            }""")
        self.setStyleSheet("""*{font-family: 微软雅黑;font-size:9pt !important;}
        """)

    def accept(self):
        """重写accept方法，在对话框关闭前进行验证"""
        if not self.validate_data():
            return  # 验证失败，不关闭对话框
        super().accept()

    def validate_data(self):
        """验证并允许关闭"""
        id_text = self.lineEdit.text().strip()
        if not id_text:
            self.show_error_message('ID不能为空')
            return False
        try:
            id = int(id_text)
        except ValueError:
            self.show_error_message('ID必须是整数')
            return False
        flag = False
        for ip, users in self.loaded_dict.items():
            for user in users:
                if id == user.get('id'):
                    flag = True
                    break
            if flag:
                self.show_error_message('%s已存在' % id)
                return False
        name = self.lineEdit_2.text().strip()
        if not name:
            self.show_error_message('名称不能为空')
            return False
        ip = self.comboBox.currentText()
        self.user_return_signal.emit([ip, id, name])
        return True


    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("tips")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    app.setWindowIcon(QIcon(':res/demo.png'))
    win = VNC_Management()
    win.show()
    sys.exit(app.exec_())
