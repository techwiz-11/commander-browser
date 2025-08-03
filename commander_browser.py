from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Commander Browser")
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://localhost:8000/commander_home.html"))

        self.setCentralWidget(self.browser)
        self.browser.loadFinished.connect(self.page_loaded)

        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        home_btn = QAction("🏠 Home", self)
        home_btn.triggered.connect(self.go_home)
        navtb.addAction(home_btn)

    def go_home(self):
        self.browser.setUrl(QUrl("http://localhost:8000/commander_home.html"))

    def page_loaded(self, ok):
        if ok:
            print("✅ Commander homepage loaded.")
        else:
            print("❌ Commander homepage failed to load.")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
