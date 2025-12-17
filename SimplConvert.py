from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QCursor, QFont, QIcon
from PySide6.QtWidgets import (
    QApplication, QComboBox, QLabel, QLineEdit, QMainWindow, QPushButton,
    QTabWidget, QWidget, QDialog
)
from pint import UnitRegistry
from AboutSimplConvert import Ui_Dialog

# Tab-specific units (labels only)
TAB_UNITS = {
    "Length": ["mm", "cm", "dm", "m", "km", "mi", "in", "ft"],
    "Time": ["ms", "s", "min", "h"],
    "Speed": ["m/s", "km/h", "mph"],
    "Acceleration": ["m/s²", "km/h²", "ft/s²"],
    "Surface": ["m²", "cm²", "ft²", "km²", "ha", "a"],
    "Volume": ["L", "mL", "m³", "gal"],
    "Density": ["kg/m³", "g/cm³", "lb/ft³"],
    "Force": ["N", "kN", "lbf"],
    "Storage": ["B", "KiB", "MiB", "GiB"],
    "Angle": ["°", "rad", "grad", "arcminute", "arcsecond"],
    "Temperature": ["degC", "degF", "degK"]
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(401, 825)
        self.setFixedSize(401, 825)
        self.setWindowIcon(QIcon("SimplConvertIcon.png"))

        # --- MENU BAR ---
        menu_bar = self.menuBar()
        info_menu = menu_bar.addMenu("Info")
        about_action = info_menu.addAction("About")
        about_action.triggered.connect(self.openaboutmenu)

        # --- CENTRAL WIDGET ---
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Tabs
        self.Tabs = QTabWidget(self.centralwidget)
        self.Tabs.setGeometry(0, 0, 401, 31)
        self.Tabs.setObjectName("Tabs")
        self.ureg = UnitRegistry()

        # Create tabs
        self.Length = QWidget(); self.Length.setObjectName("Length")
        self.Time = QWidget(); self.Time.setObjectName("Time")
        self.Speed = QWidget(); self.Speed.setObjectName("Speed")
        self.Acceleration = QWidget(); self.Acceleration.setObjectName("Acceleration")
        self.Surface = QWidget(); self.Surface.setObjectName("Surface")
        self.Volume = QWidget(); self.Volume.setObjectName("Volume")
        self.Density = QWidget(); self.Density.setObjectName("Density")
        self.Force = QWidget(); self.Force.setObjectName("Force")
        self.Storage = QWidget(); self.Storage.setObjectName("Storage")
        self.Angle = QWidget(); self.Angle.setObjectName("Angle")
        self.Temperature = QWidget(); self.Temperature.setObjectName("Temperature")

        for tab in [self.Length, self.Time, self.Speed, self.Acceleration,
                    self.Surface, self.Volume, self.Density, self.Force,
                    self.Storage, self.Angle, self.Temperature]:
            self.Tabs.addTab(tab, "")

        # Entry + combo boxes
        self.Entry = QLineEdit(self.centralwidget)
        self.Entry.setGeometry(130, 40, 261, 32)

        self.From = QComboBox(self.centralwidget)
        self.From.setGeometry(10, 40, 111, 32)
        self.From.setCursor(QCursor(Qt.PointingHandCursor))

        self.To = QComboBox(self.centralwidget)
        self.To.setGeometry(10, 80, 111, 32)
        self.To.setCursor(QCursor(Qt.PointingHandCursor))

        # Result label
        self.Result = QLabel("Result", self.centralwidget)
        self.Result.setGeometry(130, 90, 500, 18)

        # --- NUMBER BUTTONS ---
        font = QFont()
        font.setPointSize(40)
        self.Buttons = {}

        positions = [
            ("Button1", 10, 120), ("Button2", 140, 120), ("Button3", 270, 120),
            ("Button4", 10, 250), ("Button5", 140, 250), ("Button6", 270, 250),
            ("Button7", 10, 380), ("Button8", 140, 380), ("Button9", 270, 380),
            ("Button0", 140, 510)
        ]

        for name, x, y in positions:
            digit = name[-1]  # "Button1" -> "1"
            btn = QPushButton(digit, self.centralwidget)
            btn.setGeometry(x, y, 121, 121)
            btn.setFont(font)
            btn.setCursor(QCursor(Qt.PointingHandCursor))
            btn.clicked.connect(lambda checked, d=digit: self.append_text(d))
            self.Buttons[name] = btn

        # Decimal button
        self.ButtonDecimal = QPushButton(".", self.centralwidget)
        self.ButtonDecimal.setGeometry(10, 510, 121, 121)
        self.ButtonDecimal.setFont(font)
        self.ButtonDecimal.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonDecimal.clicked.connect(lambda: self.append_text("."))

        # Convert button
        self.Convert = QPushButton("Convert", self.centralwidget)
        self.Convert.setGeometry(10, 640, 381, 121)
        self.Convert.setFont(font)
        self.Convert.setCursor(QCursor(Qt.PointingHandCursor))
        self.Convert.clicked.connect(self.convertfunction)

        # Tab handling
        self.Tabs.currentChanged.connect(self.update_combo_boxes)
        self.update_combo_boxes(0)
        self.set_tab_names()

    def openaboutmenu(self):
        dialog = QDialog(self)  # Create a QDialog instance
        ui = Ui_Dialog()        # Create the UI instance
        ui.setupUi(dialog)      # Set up the UI inside the dialog
        dialog.exec()

    def convertfunction(self):
        try:
            value = float(self.Entry.text())
            from_unit = self.From.currentText()
            to_unit = self.To.currentText()
            quantity = value * self.ureg(from_unit)
            result = quantity.to(to_unit)
            self.Result.setText(str(result))
        except ValueError:
            self.Result.setText("THAT GOTTA BE FAKE NUMBER 💀")

    def append_text(self, text):
        self.Entry.setText(self.Entry.text() + text)

    @Slot(int)
    def update_combo_boxes(self, index):
        tab_name = self.Tabs.tabText(index)
        units = TAB_UNITS.get(tab_name, [])
        self.From.clear()
        self.To.clear()
        self.From.addItems(units)
        self.To.addItems(units)

    def set_tab_names(self):
        tab_names = ["Length", "Time", "Speed", "Acceleration", "Surface",
                     "Volume", "Density", "Force", "Storage", "Angle", "Temperature"]
        for i, name in enumerate(tab_names):
            self.Tabs.setTabText(i, name)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
