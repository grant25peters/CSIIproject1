from PyQt6.QtWidgets import *
from gui_ballot import *

class Logic(QMainWindow, Ui_MainWindow):
    '''
    Class for controlling the variables involved with a ballot
    '''
    def __init__(self) -> None:
        '''
        Method for setting up the voting menu
        '''
        super().__init__()
        self.setupUi(self)

        self.votes_red = 0
        self.votes_blue = 0
        self.votes_green = 0

        self.cast_vote_button.clicked.connect(lambda:self.cast_vote())
        self.end_button.clicked.connect(lambda:self.end_vote())


    def cast_vote(self) -> None:
        '''
        Method when user wants to lock in their vote
        '''
        if self.red_radio_button.isChecked():
            self.votes_red += 1
        elif self.blue_radio_button.isChecked():
            self.votes_blue += 1
        elif self.green_radio_button.isChecked():
            self.votes_green += 1


        self.radio_group.setExclusive(False)
        self.red_radio_button.setChecked(False)
        self.blue_radio_button.setChecked(False)
        self.green_radio_button.setChecked(False)
        self.radio_group.setExclusive(True)

    def end_vote(self) -> None:
        '''
        Method to display results
        '''
        self.results_label.setText(
                                    f'\nBlue = {self.votes_blue}'
                                    f'\nRed = {self.votes_red}'
                                    f'\nGreen = {self.votes_green}'
        )