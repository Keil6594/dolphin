import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class TabbedBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.add_tab_btn = QPushButton(" + Новая вкладка ")
        self.add_tab_btn.clicked.connect(self.add_new_tab)

        layout = QVBoxLayout()
        layout.addWidget(self.add_tab_btn)
        layout.addWidget(self.tabs)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.add_new_tab()

    def add_new_tab(self):
        browser = QWebEngineView()
        browser.setUrl(QUrl("https://search.brave.com/"))
        
        i = self.tabs.addTab(browser, "Новая страница")
        self.tabs.setCurrentIndex(i)

    def close_tab(self, i):
        if self.tabs.count() > 1:
            self.tabs.removeTab(i)

app = QApplication(sys.argv)
window = TabbedBrowser()
window.show()
sys.exit(app.exec())
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLineEdit, 
                             QVBoxLayout, QWidget, QHBoxLayout, 
                             QPushButton, QComboBox)
