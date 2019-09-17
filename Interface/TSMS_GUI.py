from Interface.TSMS import Ui_Dialog as TSMS_UI
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys
from datetime import datetime

import Interface.TSMS_DB as DB

class POP_TSMS(QDialog):
    def __init__(self, mem=None, TSMS_mem=None, strategy_mem=None):
        super().__init__()

        if mem != None:
            self.mem = mem
            self.TSMS_mem = TSMS_mem
            self.strategy_mem = strategy_mem

        self.TSMS_UI = TSMS_UI()
        self.TSMS_UI.setupUi(self)

        timer = QtCore.QTimer(self)
        for _ in [self.operation_mode, self.alarm_LCO]:
            timer.timeout.connect(_)
        timer.start(600)

        self.step = DB.DB

        self.TSMS_UI.btn_alarm_1.clicked.connect(lambda: self.load_stackwidget(0, 'LCO 3.1.1'))
        self.TSMS_UI.btn_alarm_2.clicked.connect(lambda: self.load_stackwidget(1, 'LCO 3.4.1'))
        self.TSMS_UI.btn_alarm_3.clicked.connect(lambda: self.load_stackwidget(2, 'LCO 3.4.3'))
        self.TSMS_UI.btn_alarm_4.clicked.connect(lambda: self.load_stackwidget(3, 'LCO 3.4.4'))

        self.load_stackcontent()

        # self.operation_mode()
        # self.alarm_LCO()
        # print(self.TSMS_mem['LCO3.1.1']['alarm'])

        self.show()

    def operation_mode(self):

        if self.TSMS_mem['operation_mode'][-1] == 1:
            self.TSMS_UI.btn_mode_1.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.TSMS_UI.btn_mode_2.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_3.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_4.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_5.setStyleSheet("background-color: rgb(229, 229, 229);")
        elif self.TSMS_mem['operation_mode'][-1] == 2:
            self.TSMS_UI.btn_mode_1.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_2.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.TSMS_UI.btn_mode_3.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_4.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_5.setStyleSheet("background-color: rgb(229, 229, 229);")
        elif self.TSMS_mem['operation_mode'][-1] == 3:
            self.TSMS_UI.btn_mode_1.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_2.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_3.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.TSMS_UI.btn_mode_4.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_5.setStyleSheet("background-color: rgb(229, 229, 229);")
        elif self.TSMS_mem['operation_mode'][-1] == 4:
            self.TSMS_UI.btn_mode_1.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_2.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_3.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_4.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.TSMS_UI.btn_mode_5.setStyleSheet("background-color: rgb(229, 229, 229);")
        elif self.TSMS_mem['operation_mode'][-1] == 5:
            self.TSMS_UI.btn_mode_1.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_2.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_3.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_4.setStyleSheet("background-color: rgb(229, 229, 229);")
            self.TSMS_UI.btn_mode_5.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            pass

    def alarm_LCO(self):
        if self.TSMS_mem['LCO3.1.1']['alarm'] !=[]:
            if self.TSMS_mem['LCO3.1.1']['alarm'][-1] == 1:
                self.TSMS_UI.btn_alarm_1.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.TSMS_UI.btn_alarm_1.setText("LCO3.1.1")
        elif self.TSMS_mem['LCO3.4.1']['alarm'] != []:
            if self.TSMS_mem['LCO3.4.1']['alarm'][-1] == 1:
                self.TSMS_UI.btn_alarm_2.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.TSMS_UI.btn_alarm_2.setText("LCO3.4.1")
        elif self.TSMS_mem['LCO3.4.4']['alarm'] !=[]:
            if self.TSMS_mem['LCO3.4.4']['alarm'][-1] == 1:
                self.TSMS_UI.btn_alarm_3.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.TSMS_UI.btn_alarm_3.setText("LCO3.1.1")
        else:
            pass

    def load_stackwidget(self, load_nub, title):
        self.TSMS_UI.stackedWidget.setCurrentIndex(load_nub)
        self.TSMS_UI.label_clicked_alarm.setText(title)

    def load_stackcontent(self):
        for load_nub in range(0, 4):
            cur_scroll_w = self.TSMS_UI.stackedWidget.widget(load_nub).children()[0].widget()
            if load_nub == 0:
                self.step_1_1 = S_Label(self.step[f'{load_nub}'][1], 20, 20, cur_scroll_w)
            else:
                pass



class S_Label(QWidget):
    def __init__(self, step_info, x, y, parent=None):
        QWidget.__init__(self)
        self.par = parent
        self.x = x
        self.y = y
        self.max_y = 0

        self.step_info = step_info
        self.content = self.step_info[0]
        self.T_boll = self.step_info[1]
        self.detail_contents = self.step_info[2]

        self.dis_boll()
        self.dis_content()

        self.dis_bottom()
        self.dis_detail()
        self.dis_check_time()

        self.bottom.clicked.connect(self.click_bottom)

    def dis_boll(self):
        # 수행 여부 확인
        if self.T_boll:
            self.boll = QLabel('●', self.par)
        else:
            self.boll = QLabel('○', self.par)

        self.boll.setGeometry(self.x, self.y, 35, 35)
        self.boll.setStyleSheet('border-top: 1px solid black; border-bottom: 1px solid black; ' \
                      'border-left: 1px solid black; font: 13pt \"HY견고딕\"; background-color: rgb(234, 234, 234);')
        self.boll.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        self.boll.show()

    def dis_content(self):

        self.content = QLabel(self.content, self.par)
        self.content.setGeometry(self.x+35, self.y, 410, 35)
        self.content.setStyleSheet('border-top: 1px solid black; border-bottom: 1px solid black; border-left: 1px solid black;' \
                        'font: 10pt \"HY견고딕\"; background-color: rgb(234, 234, 234);')
        self.content.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.content.show()

    def dis_bottom(self):
        self.bottom = QPushButton('확인', self.par)
        self.bottom.setGeometry(self.x + 520, self.y, 35, 35)
        self.bottom.setStyleSheet('font: 9pt \"HY견고딕\"; background-color: rgb(234, 234, 234);')
        self.bottom.show()

    def dis_detail(self):
        line_nub = len(self.detail_contents.split('\n'))
        if not self.detail_contents == '':
            self.detail_out = QLabel('', self.par)
            self.detail_out.setGeometry(self.x + 35, self.y + 35, 480, line_nub * 16 + 15)
            self.detail_out.setStyleSheet('border-right: 1px solid black; border-bottom: 1px solid black; ' \
                        'border-left: 1px solid black; font: 10pt \"HY견고딕\"; background-color: rgb(234, 234, 234);')

            self.detail = QLabel(self.detail_contents, self.par)
            self.detail.setGeometry(self.x + 40, self.y + 40, 460, line_nub * 16 + 5)
            self.detail.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.detail.setStyleSheet('font: none; background-color: rgb(234, 234, 234);')

            self.detail_out.show()
            self.max_y = self.y + 35 + line_nub * 16 + 15
        else:
            self.max_y = self.y + 35

    def dis_check_time(self):
        self.ch_time = QLabel('00:00:00', self.par)
        self.ch_time.setGeometry(self.x + 445, self.y, 70, 35)
        self.ch_time.setStyleSheet('border-top: 1px solid black; border-bottom: 1px solid black; ' \
                        'border-right: 1px solid black; font: 8pt \"HY견고딕\"; background-color: rgb(234, 234, 234);')
        self.ch_time.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        self.ch_time.show()

    def click_bottom(self):
        print(self.T_boll)
        if self.T_boll:
            self.T_boll = False
            print('여기')
            self.boll.setText('○')
            self.boll.setStyleSheet('border-top: 1px solid black; border-bottom: 1px solid black; ' \
                      'border-left: 1px solid black; font: 13pt \"HY견고딕\"; background-color: rgb(234, 234, 234);')
            self.content.setStyleSheet('border-top: 1px solid black; border-bottom: 1px solid black; ' \
                        'font: 10pt \"HY견고딕\"; background-color: rgb(234, 234, 234);')
            self.ch_time.setStyleSheet('border-top: 1px solid black; border-bottom: 1px solid black; ' \
                        'border-right: 1px solid black; font: 8pt \"HY견고딕\"; background-color: rgb(234, 234, 234);')
            self.ch_time.setText('00:00:00')
            # self.detail_out.setStyleSheet(self.ST.L_d_bord)
        else:
            print('zlzl')
            self.T_boll = True
            self.boll.setText('●')
            print('a')
            self.boll.setStyleSheet('border-top: 1px solid black; border-bottom: 1px solid black; ' \
                        'border-left: 1px solid black; font: 13pt \"HY견고딕\"; background-color: #2b90d9;')
            print('a2')
            self.content.setStyleSheet('border-top: 1px solid black; border-bottom: 1px solid black; ' \
                         'font: 10pt \"HY견고딕\"; background-color: #2b90d9;')
            print('a3')
            self.ch_time.setStyleSheet('border-top: 1px solid black; border-bottom: 1px solid black; ' \
                         'border-right: 1px solid black; font: 8pt \"HY견고딕\"; background-color: #2b90d9;')
            print('a4')
            now = datetime.now()
            self.ch_time.setText(f'{now.hour % 12:02}:{now.minute:02}:{now.second:02}')




if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = POP_TSMS()
    w.exec()
    sys.exit(app.exec_())





# class sub_tren_window(QDialog):
#     def __init__(self, mem=None, auto_mem = None, strage_mem=None):
#         super().__init__()
#         # ===============================================================
#         # 메모리 호출 부분 없으면 Test
#         if mem != None:
#             self.mem = mem
#             self.auto_mem = auto_mem
#             self.strage_mem = strage_mem
#         else:
#             print('TEST_interface')
#         # ===============================================================
#         # CNS 정보 읽기
#         with open('pro.txt', 'r') as f:
#             self.cns_ip, self.cns_port = f.read().split('\t') # [cns ip],[cns port]
#         self.CNS_udp = CNS_Send_UDP.CNS_Send_Signal(self.cns_ip, int(self.cns_port))
#         # ===============================================================
#         self.Trend_ui = Rod_UI()
#         self.Trend_ui.setupUi(self)
#         # ===============================================================
#         # rod gp
#         self.draw_rod_his_gp()
#         # ===============================================================
#         # rod control
#         self.Trend_ui.rodup.clicked.connect(self.rod_up)
#         self.Trend_ui.roddown.clicked.connect(self.rod_down)
#         # ===============================================================
#
#         timer = QtCore.QTimer(self)
#         for _ in [self.update_window, self.update_rod_his_gp]:
#             timer.timeout.connect(_)
#         timer.start(600)
#
#         self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint)
#         self.show()
#
#     def rod_up(self):
#         self.CNS_udp._send_control_signal(['KSWO33', 'KSWO32'], [1, 0])
#
#     def rod_down(self):
#         self.CNS_udp._send_control_signal(['KSWO33', 'KSWO32'], [0, 1])
#
#     def update_window(self):
#         self.Trend_ui.Rod_1.setGeometry(10, 70, 41, abs(self.mem['KBCDO10']['V'] - 228))
#         self.Trend_ui.Rod_2.setGeometry(70, 70, 41, abs(self.mem['KBCDO9']['V'] - 228))
#         self.Trend_ui.Rod_3.setGeometry(130, 70, 41, abs(self.mem['KBCDO8']['V'] - 228))
#         self.Trend_ui.Rod_4.setGeometry(190, 70, 41, abs(self.mem['KBCDO7']['V'] - 228))
#         self.Trend_ui.Dis_Rod_4.setText(str(self.mem['KBCDO7']['V']))
#         self.Trend_ui.Dis_Rod_3.setText(str(self.mem['KBCDO8']['V']))
#         self.Trend_ui.Dis_Rod_2.setText(str(self.mem['KBCDO9']['V']))
#         self.Trend_ui.Dis_Rod_1.setText(str(self.mem['KBCDO10']['V']))
#
#         # 아래 자율/수동 패널
#         if self.strage_mem['strategy'][-1] == 'NA':
#             self.Trend_ui.label_5.setStyleSheet('background-color: rgb(255, 144, 146);'
#                                                 'border-style: outset;'
#                                                 'border-width: 0.5px;'
#                                                 'border-color: black;'
#                                                 'font: bold 14px;')
#             self.Trend_ui.label_3.setStyleSheet('background-color: rgb(255, 255, 255);'
#                                                 'border-style: outset;'
#                                                 'border-width: 0.5px;'
#                                                 'border-color: black;'
#                                                 'font: bold 14px;')
#         else:
#             self.Trend_ui.label_5.setStyleSheet('background-color: rgb(255, 255, 255);'
#                                                 'border-style: outset;'
#                                                 'border-width: 0.5px;'
#                                                 'border-color: black;'
#                                                 'font: bold 14px;')
#             self.Trend_ui.label_3.setStyleSheet('background-color: rgb(255, 144, 146);'
#                                                 'border-style: outset;'
#                                                 'border-width: 0.5px;'
#                                                 'border-color: black;'
#                                                 'font: bold 14px;')
#
#
#     def draw_rod_his_gp(self):
#         # 위 그래프
#         self.rod_cond = plt.figure()
#         self.rod_cond_ax = self.rod_cond.add_subplot(111)
#         self.rod_cond_canv = FigureCanvasQTAgg(self.rod_cond)
#         self.Trend_ui.Rod_his_cond.addWidget(self.rod_cond_canv)
#
#         # 아래 제어신호
#         self.rod_fig = plt.figure()
#         self.rod_ax = self.rod_fig.add_subplot(111)
#         self.rod_canvas = FigureCanvasQTAgg(self.rod_fig)
#         self.Trend_ui.Rod_his.addWidget(self.rod_canvas)
#
#     def update_rod_his_gp(self):
#         try:
#             self.rod_ax.clear()
#             temp = []
#             cns_time = []
#             for _ in range(len(self.mem['KSWO33']['D'])):
#                 if self.mem['KSWO33']['D'][_] == 0 and self.mem['KSWO32']['D'][_] == 0:
#                     temp.append(0)
#                     cns_time.append(self.mem['KCNTOMS']['D'][_]/5)
#                 elif self.mem['KSWO33']['D'][_] == 1 and self.mem['KSWO32']['D'][_] == 0:
#                     temp.append(1)
#                     cns_time.append(self.mem['KCNTOMS']['D'][_] / 5)
#                 elif self.mem['KSWO33']['D'][_] == 0 and self.mem['KSWO32']['D'][_] == 1:
#                     temp.append(-1)
#                     cns_time.append(self.mem['KCNTOMS']['D'][_] / 5)
#             self.rod_ax.plot(cns_time, temp)
#             self.rod_ax.set_ylim(-1.2, 1.2)
#             # self.rod_ax.set_xlim(0, 50)
#             self.rod_ax.set_yticks([-1, 0, 1])
#             self.rod_ax.set_yticklabels(['Down', 'Stay', 'UP'])
#             self.rod_ax.grid()
#             self.rod_canvas.draw()
#
#             self.rod_cond_ax.clear()
#             rod_cond_time = self.auto_mem['Start_up_operation_his']['time']
#             self.rod_cond_ax.plot(rod_cond_time, self.auto_mem['Start_up_operation_his']['power'])
#             self.rod_cond_ax.plot(rod_cond_time, self.auto_mem['Start_up_operation_his']['up_cond'])
#             self.rod_cond_ax.plot(rod_cond_time, self.auto_mem['Start_up_operation_his']['low_cond'])
#             self.rod_cond_ax.grid()
#             self.rod_cond_canv.draw()
#         except Exception as e:
#             print(self, e)
