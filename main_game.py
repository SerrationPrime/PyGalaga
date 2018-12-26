import sys
import styles
import keyboard
import time

from threading import Thread
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow
from entities import Player, Projectile, Enemy
from game_enums import Factions


class SimMoveDemo(QMainWindow):

    def __init__(self):
        super().__init__()

        self.pix1 = QPixmap('sprites/m_play_char.png')
        self.player1 = Player(QLabel(self))

        self.xlimit = 600
        self.ylimit = 1000

        self.projectiles = []

        self.setFixedSize(self.xlimit, self.ylimit)
        self.level = 1

        self.__init_ui__()

        self.updateThread = Thread(target=self.__update_state__, daemon=True)
        self.updateThread.start()

    def __init_ui__(self):

        self.player1.label.setPixmap(self.pix1)
        self.player1.label.setGeometry(100, 850, 50, 50)
        self.player1.label.setAlignment(Qt.AlignCenter)

        self.setStyleSheet(styles.stylesheet)

        self.level_display = QLabel(self)
        self.level_display.setText("Level %d" % self.level)
        self.level_display.setGeometry(self.xlimit/2-75 ,0, 150, 50)
        self.level_display.setStyleSheet(styles.stylesheet)
        self.level_display.setAlignment(Qt.AlignCenter)

        self.p1score_display = QLabel(self)
        self.p1score_display.setText("Score: %d" % self.player1.score)
        self.p1score_display.setGeometry(20, 0, 200, 50)
        self.p1score_display.setStyleSheet(styles.stylesheet)
        self.p1score_display.setAlignment(Qt.AlignLeft)

        self.setWindowTitle('Really crappy Galaga')
        self.show()

    def __update_state__(self):
        while True:
            rec1 = self.player1.label.geometry()

            if keyboard.is_pressed('d'):
                if (rec1.x() + 5 + rec1.width()) <= self.xlimit:
                    self.player1.label.setGeometry(rec1.x() + 5, rec1.y(), rec1.width(), rec1.height())
                    rec1 = self.player1.label.geometry()
            if keyboard.is_pressed('s'):
                if (rec1.y() + 5 + rec1.height()) <= self.ylimit:
                    self.player1.label.setGeometry(rec1.x(), rec1.y() + 5, rec1.width(), rec1.height())
                    rec1 = self.player1.label.geometry()
            if keyboard.is_pressed('w'):
                if (rec1.y() - 5) >= 0:
                    self.player1.label.setGeometry(rec1.x(), rec1.y() - 5, rec1.width(), rec1.height())
                    rec1 = self.player1.label.geometry()
            if keyboard.is_pressed('a'):
                if (rec1.x() - 5) >= 0:
                    self.player1.label.setGeometry(rec1.x() - 5, rec1.y(), rec1.width(), rec1.height())

            self.__update_projectiles()
            time.sleep(1 / 60)

    def __create_projectile(self, player):
        lab = QLabel(self)
        pix = QPixmap('sprites/m_projectile_plasma1.png')
        lab.setPixmap(pix)
        lab.setGeometry(player.label.geometry().center().x()-5, player.label.geometry().top(), 12, 25)
        lab.setAlignment(Qt.AlignCenter)

        lab.show()
        proj = Projectile(lab, Factions.Player, 0, -20)
        return proj

    def __update_projectiles(self):
        if keyboard.is_pressed('space') and self.player1.reload == 0:
            self.projectiles.append(self.__create_projectile(self.player1))
            self.player1.reload=60/self.player1.fire_rate
        else:
            if self.player1.reload > 0:
                self.player1.reload -= 1

        for proj in self.projectiles:
            curr_pos = proj.label.geometry()
            proj.label.setGeometry(curr_pos.x() + proj.xspeed, curr_pos.y() + proj.yspeed, curr_pos.width(), curr_pos.height())
            if curr_pos.x()>self.xlimit or curr_pos.x()<0 or curr_pos.y()>self.ylimit or curr_pos.y()<0:
                self.projectiles.remove(proj)
                del proj


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimMoveDemo()
    sys.exit(app.exec_())
