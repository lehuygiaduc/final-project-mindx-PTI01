import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QListWidget, QListWidgetItem, QLabel, QVBoxLayout, QWidget, QScrollArea, QDialog, QComboBox, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import Qt
import json

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui", self)

    # Bắt sự kiện click chuột vào nút login
        self.pushButton_3.clicked.connect(self.check_login)
    #Bắt sự kiện click chuột vào nút sign up
        self.pushButton.clicked.connect(self.showRegister)

    def check_login(self):
        # Lấy thông tin email và mật khẩu từ người dùng
        email = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        
        # Kiểm tra email và mật khẩu có được nhập hay không
        if not email: 
            msg_box.setText("Please enter your email or phone number!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Please enter a password!")
            msg_box.exec()
            return
    
    # Kiểm tra email và mật khẩu có khớp với tài khoản admin hay không
        if email == "admin@example.com" and password == "admin":
            # Nếu đăng nhập thành công, chuyển sang giao diện chính (Main)
            self.close()
            mainPage.show()
        else:
            # Nếu đăng nhập không thành công, hiển thị thông báo lỗi
            msg_box.setText("Incorrect email or password!")
            msg_box.exec()

    def showRegister(self):
        registerPage.show()
        self.close()

# Lớp chứa giao diện đăng ký
class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/signin.ui", self)
        self.name = ""
        
        # Bắt sự kiện click chuột vào nút đăng ký
        self.pushButton.clicked.connect(self.Register)

        #Bắt sự kiện "đã có tài khoản" và chuyển sag trang đăng nhập
        self.pushButton_2.clicked.connect(self.showLoginPage)
    
    def Register(self):
        # Lấy thông tin email, username và mật khẩu từ người dùng
        self.name = self.lineEdit_3.text()
        email = self.lineEdit_2.text()
        password = self.lineEdit_4.text()
        
        # Kiểm tra các trường thông tin có được nhập hay không
        if not self.name:
            msg_box.setText("Please enter your name!")
            msg_box.exec()
            return
        if not email: 
            msg_box.setText("Please enter your email or phone number!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Please enter a password!")
            msg_box.exec()
            return
        if not self.checkBox.isChecked():
            msg_box.setText("Please read and agree to the terms and conditions of ỨNG DỤNG QUẢN LÍ CẦU THỦ BÓNG ĐÁ!")
            msg_box.exec()
            return

       # Đóng giao diện đăng ký và chuyển sang giao diện chính
        mainPage = mainwindowPage.stackedWidget.currentWidget()
        mainPage.label2.setText(self.name)
        mainPage.show()
        self.close()
    
    def showLoginPage(self):
        loginPage.show()
        self.close()
    
    # Lớp chứa giao diện chính
class ItemLoader:
    def __init__(self, json_file):
       with open(json_file,"r") as file:
           self.data = json.load(file)

    def get_item(self):
        items = []
        for item in self.data:
            id = item['id']
            name = item['name']
            quantity = item['quantity']
            list = item['list']
            mentor = item['mentor']
            matches = item['matches']
            information = item['ìnormation']
            image = item['image']
            items.append((id, name, quantity, list, mentor, matches, information, image))
        return items        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        self.loadUiFiles()
        self.displays()
        self.resize(800,500)

    def loadUiFiles(self):
        ui_files = ['ui/main.ui', 'ui/list.ui', 'ui/search.ui', 'ui/contact.ui']

        for ui_file in ui_files:
            widget = uic.loadUi(ui_file)
            self.stackedWidget.addWidget(widget)

            self.showMainPage()
            self.showItems()

    def displays(self):
        main_widget = self.stackedWidget.widget(0)
        main_widget.pushButton_3.clicked.connect(self.showListPage)
        main_widget.pushButton.clicked.connect(self.showSearchPage)
        main_widget.pushButton_4.clicked.connect(self.showContactPage)

        list_widget = self.stackedWidget.widget(1)
        list_widget.pushButton_2.clicked.connect(self.showMainPage)
        list_widget.pushButton.clicked.connect(self.showSearchPage)
        list_widget.pushButton_4.clicked.connect(self.showContactPage)

        search_widget = self.stackedWidget.widget(2)
        search_widget.pushButton_2.clicked.connect(self.showMainPage)
        search_widget.pushButton_3.clicked.connect(self.showListPage)
        search_widget.pushButton_4.clicked.connect(self.showContactPage)

        contact_widget = self.stackedWidget.widget(3)
        contact_widget.pushButton_2.clicked.connect(self.showMainPage)
        contact_widget.pushButton.clicked.connect(self.showSearchPage)
        contact_widget.pushButton_4.clicked.connect(self.showContactPage)

    def showMainPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def showListPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def showSearchPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def showContactPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def showItems(self):
        list_widget = self.stackedWidget.widget(1)
        scroll_area = list_widget.scrollArea
        scroll_content_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_content_widget)

        self.item_loader = ItemLoader('data.json')
        items = self.item_loader.get_items()

        for item in items:
            detail_widget = DetailWidget(item)
            scroll_layout.addWidget(detail_widget)

        scroll_area.setWidget(scroll_content_widget)

class DetailWidget(QWidget):
    def __init__(self, item):
        super().__init__()

        self.item = item
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label_id = QLabel(f"ID: {item[0]}")
        self.label_name = QLabel(f"Name: {item[1]}")
        self.label_matches = QLabel(f"matches: {item[5]}")
        pixmap = QPixmap(item[7])
        self.label_image = QLabel()
        self.label_image.setPixmap(pixmap)

        self.label_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_matches.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.label_image)
        layout.addWidget(self.label_id)
        layout.addWidget(self.label_name)
        layout.addWidget(self.label_matches)

        self.button_show_detail = QPushButton("Show Detail")
        layout.addWidget(self.button_show_detail)

        self.button_show_detail.clicked.connect(self.showDetail)

    def showDetail(self):
        list_widget = QListWidget()
        list_widget.addItem(f"ID: {self.item[0]}")
        list_widget.addItem(f"Name: {self.item[1]}")
        list_widget.addItem(f"Quantity: {self.item[2]}")
        list_widget.addItem(f"List: {self.item[3]}")
        list_widget.addItem(f"Mentor: {self.item[4]}")
        list_widget.addItem(f"Matches: {self.item[5]}")
        list_widget.addItem(f"Information: {self.item[6]}")
        

        detail_dialog = QDialog(self)
        detail_dialog.setWindowTitle("Item Detail")
        detail_dialog.setFixedSize(300, 200)

        layout = QVBoxLayout(detail_dialog)
        layout.addWidget(list_widget)

        detail_dialog.exec()

if __name__ == '__main__':
    app = QApplication([])
    #Tạo các đối tượng tương ứng với các trang giao diện
    loginPage = Login()
    loginPage.show()
    registerPage = Register()
    mainwindowPage = MainWindow()
    # Thiết lập hộp thoại thông báo lỗi
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Error")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
    
    app.exec()

                                            