# PyQt5 introduction
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("defjoy's GUI")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("files/picture.jpeg"))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()












# boilplate window:

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()