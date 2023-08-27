import sys
import easygui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget, \
    QMessageBox


class ChatRoomWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    easygui.abouteasygui()
    e.abouteasygui()
    def init_ui(self):
        self.setWindowTitle("希望聊天室By23m8d27")
        self.setGeometry(100, 100, 600, 400)

        # 创建聊天展示框
        self.chat_display = QTextEdit(self)
        self.chat_display.setGeometry(10, 10, 580, 300)
        self.chat_display.setReadOnly(True)

        # 创建消息输入框
        self.message_input = QLineEdit(self)
        self.message_input.setGeometry(50, 50, 200, 30)
        self.message_input.setFixedSize(600, 50)

        # 设置回车键事件过滤器
        self.message_input.installEventFilter(self)

        # 创建发送按钮
        self.send_button = QPushButton("发送", self)
        self.send_button.setGeometry(420, 320, 80, 30)
        self.send_button.setFixedSize(120, 40)
        self.send_button.clicked.connect(self.send_message)

        # 创建退出按钮
        self.exit_button = QPushButton("退出", self)
        self.exit_button.setGeometry(510, 320, 80, 30)
        self.exit_button.setFixedSize(120, 40)
        self.exit_button.clicked.connect(self.quit)

        # 创建布局并添加控件
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.chat_display)
        self.layout.addWidget(self.message_input)
        self.layout.addWidget(self.send_button)
        self.layout.addWidget(self.exit_button)

        # 创建窗口并设置布局
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    # 发送消息的槽函数
    def send_message(self):
        message = self.message_input.text()
        self.message_input.clear()
        self.chat_display.append(f"你: {message}")

    # 按下回车键的事件过滤器
    def eventFilter(self, obj, event):
        if obj is self.message_input and event.type() == event.KeyPress and event.key() == Qt.Key_Return:
            self.send_message()
            return True
        return super().eventFilter(obj, event)

    # 在窗口显示事件触发时显示版权信息
    def showEvent(self, event):
        QMessageBox.information(self, "声明", "本聊天室基于PyQt5，由希望工作室Beta开发者打造。")

    # 退出程序的槽函数
    def quit(self):
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_room = ChatRoomWindow()
    chat_room.show()
    sys.exit(app.exec_())
