#!/usr/bin/env python3

import sys
""" for the skeleton """
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
""" for the view """
from PyQt5.QtCore import Qt
# arrange widgets into a grid of rows and columns with QGridLayout
from PyQt5.QtWidgets import QGridLayout
# 
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
# arrange widgets vertically from top to bottom with QVBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
""" import partial() to connect signals with methods that accept extra args"""
from functools import partial
import pycalcModel
"""
import pycalcModel
# pycalcModel.greet()
"""

__version__ = '0.1'
__author__ = 'ABG'

ERROR_MSG = pycalcModel.ERROR_MSG

class PyCalcUi(QMainWindow):
    # PyCalc's VIEW (GUI)
    def __init__(self):
    # initialize VIEW
        super().__init__()
        self.setWindowTitle('PyCalculator')
        self.setFixedSize(335, 335)
    # set the central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)

        self.setCentralWidget(self._centralWidget)

        self._centralWidget.setLayout(self.generalLayout)
    # create the display and buttons (won't work until their methods are implemented
    # see _createDisplay() and _createButtons() )
        self._createDisplay()
        self._createButtons()
    
    # Create/implement the display
    def _createDisplay(self): 
        # Create the display widget with QLineEdit()
        self.display = QLineEdit()
        # Set display properties
        # - fixed height at 35 px
        self.display.setFixedHeight(35)
        # - text is left-aligned
        self.display.setAlignment(Qt.AlignRight)
        # - read-only (to avoid direct editing)
        self.display.setReadOnly(True)
        # add the display to the general layout with .addWidget()
        self.generalLayout.addWidget(self.display)
    
    # Create/implement the display
    def _createButtons(self):
        # create dictionary to hold the buttons
        self.buttons = {}
        # arrange the buttons on the calculator's window
        # with `QGridLayout`
        buttonsLayout = QGridLayout()
        # Button text on left | button position on grid
        buttons = { '7': (0, 0),
                    '8': (0, 1),
                    '9': (0, 2),
                    '/': (0, 3),
                    'C': (0, 4),
                    '4': (1, 0),
                    '5': (1, 1),
                    '6': (1, 2),
                    '*': (1, 3),
                    '(': (1, 4),
                    '1': (2, 0),
                    '2': (2, 1),
                    '3': (2, 2),
                    '-': (2, 3),
                    ')': (2, 4),
                    '0': (3, 0),
                    '00': (3, 1),
                    '.': (3, 2),
                    '+': (3, 3),
                    '=': (3, 4),
                }
        # create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # add buttonsLayout to general layout
        self.generalLayout.addLayout(buttonsLayout)
    # add 3 methods that will form the GUI public interface 
    # and complete the VIEW class
    # method 1 - set display text
    def setDisplayText(self, text):
        # use .setText() to set and update display text
        self.display.setText(text)
        # use .setFocus() to set the cursor's focus on the display
        self.display.setFocus()
    # method 2 - get display text
    def displayText(self):
        # this a getter method that returns the current text
        # when the user clicks =, the program will use the return value
        # of .displayText() as the math expression to be evaluated
        return self.display.text()
    # method 3 - clear display text
    def clearDisplay(self):
        # set the display text to an empty string so the user can
        # introduce a new math expression
        self.setDisplayText('')

# Create a Controller class to connect the GUI and Model
class PyCalcCtrl:
    # initalize the PyCalc Controller class
    # 1. give PyCalcCtrl an instance of PyCalcUi
    # to gain full acccess to the View's public interface
    def __init__(self, model, view):
        self._evaluate = model

        self._view = view
    # connect signals and slots
        self._connectSignals()

    # 5. take the display content, evaluate the math expression, and show the result
    # with calculateResult()
    def _calculateResult(self):
        # get display content and evaluate the expression
        result = self._evaluate(expression=self._view.displayText())
        # show the result in the display
        self._view.setDisplayText(result)

    # 2. Handle creation of math expressions and update display per user input
    def _buildExpression(self, sub_exp):
         # 6. add an if statement to clear the display if an error occurs
        if self._view.displayText() == ERROR_MSG:
            # clear the display and start over if there is an error
            self._view.clearDisplay()
        # build expression
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)
    
    # 3. Connect printable buttons to buildExpression()
    # with _connectSignals()
    def _connectSignals(self):
        # connect signals and slots
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
         # 7.add a connection to enable the = sign
        self._view.buttons['='].clicked.connect(self._calculateResult)
        # 7. add a connect to ensure the expression is calculated when user hits "ENTER"
        self._view.display.returnPressed.connect(self._calculateResult)
        # connect the clear (C) button to _view.clearDisplay() to clear display text
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)

def main():
    # 3. Define the calculator's MAIN function
    # This is the app's ENTRY POINT
    # 3. create an instance of QApplication called "pycalc"
    pycalc = QApplication(sys.argv)
    # 3. Create an instance of the PyCalcUi and show the calculator's GUI
    view = PyCalcUi()
    # 3. show the GUI with view.show()
    view.show()

    # *** create instances of Model and Controller ***    
    
    # model holds a reference to evaluateExpression() 
    model = pycalcModel.evaluateExpression
    # create an instance of PyCalcCtrl() and pass View and Model in as arguments
    PyCalcCtrl(model=model, view=view)

    # 4. Execute the calculator's main/event looop with .exec_()
    # wrap this in sys.exit
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()