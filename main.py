import sys
from PyQt6.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene,
                             QMainWindow, QMessageBox, QStatusBar, QToolBar)
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Set up the application's GUI."""
        self.setMinimumSize(800, 600)
        self.setWindowTitle('PyGraphics')

        self.set_up_main_window()
        self.create_actions()
        self.create_menu()
        self.create_tool_bar()
        self.setStatusBar(QStatusBar())

        self.show()

    def set_up_main_window(self):
        """Create and arrange widgets in the main window."""

        self.graphics_scene = GraphicsScene()
        self.setCentralWidget(self.graphics_scene)

    def create_actions(self):
        """Create the application's menu actions."""

        # Create actions for File menu
        self.quit_act = QAction(QIcon('images/exit.png'), self.tr('&Quit'))
        self.quit_act.setShortcut('Ctrl+Q')
        self.quit_act.setStatusTip(self.tr('Quit program'))
        self.quit_act.triggered.connect(self.close)

        # Create actions for View menu
        self.full_screen_act = QAction(self.tr('&Full Screen'), checkable=True)
        self.full_screen_act.setStatusTip(self.tr('Switch to full screen mode'))
        self.full_screen_act.triggered.connect(self.switch_to_full_screen)

        # Create actions for Help menu
        self.about_act = QAction(self.tr('&About'))
        self.about_act.setStatusTip(self.tr('Get info about program'))
        self.about_act.triggered.connect(self.show_about_dialog)

    def create_menu(self):
        """Create the application's menu bar."""
        self.menuBar().setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = self.menuBar().addMenu(self.tr('&File'))
        file_menu.addAction(self.quit_act)

        # Create View menu, Appearance submenu and add actions
        view_menu = self.menuBar().addMenu(self.tr('&View'))
        appearance_submenu = view_menu.addMenu(self.tr('&Appearance'))
        appearance_submenu.addAction(self.full_screen_act)

        # Create Help menu and add actions
        help_menu = self.menuBar().addMenu(self.tr('&Help'))
        help_menu.addAction(self.about_act)

    def create_tool_bar(self):
        """Create the application's toolbar."""
        toolbar = QToolBar(self)
        toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(toolbar)

        # Add actions to the toolbar
        toolbar.addAction(self.quit_act)

    def switch_to_full_screen(self, state):
        """If state is True, display the main window in full screen.
        Otherwise, return the window to normal."""
        self.showFullScreen() if state else self.showNormal()

    def show_about_dialog(self):
        """Display the About dialog."""
        QMessageBox.about(self,
                          "About PyGraphics",
                          """<p>Practice in computer graphics</p>
                          <p>Student: Andrey Kurlin SE-20-2</p>""")


class GraphicsScene(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Create the graphics scene and add Objects instances to the scene."""
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
