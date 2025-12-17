from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
                               QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(392, 131)
        icon = QIcon()
        icon.addFile(u"SimplConvert/SimplConvertIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.AboutTitle = QLabel(Dialog)
        self.AboutTitle.setObjectName(u"AboutTitle")
        self.AboutTitle.setGeometry(QRect(10, 10, 381, 51))
        font = QFont()
        font.setPointSize(40)
        self.AboutTitle.setFont(font)
        self.Version = QLabel(Dialog)
        self.Version.setObjectName(u"Version")
        self.Version.setGeometry(QRect(10, 40, 371, 81))
        font1 = QFont()
        font1.setPointSize(20)
        self.Version.setFont(font1)
        self.Creator = QLabel(Dialog)
        self.Creator.setObjectName(u"Creator")
        self.Creator.setGeometry(QRect(10, 90, 241, 41))
        self.Creator.setFont(font1)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 93, 88, 31))
        self.pushButton.clicked.connect(Dialog.accept)
        self.Icon = QLabel(Dialog)
        self.Icon.setObjectName(u"Icon")
        self.Icon.setGeometry(QRect(277, 7, 101, 81))
        self.Icon.setScaledContents(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"About SimplConvert", None))
        self.AboutTitle.setText(QCoreApplication.translate("Dialog", u"About", None))
        self.Version.setText(QCoreApplication.translate("Dialog", u"SimplConvert v1.0", None))
        self.Creator.setText(QCoreApplication.translate("Dialog", u"By Master", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.Icon.setText("")
    # retranslateUi