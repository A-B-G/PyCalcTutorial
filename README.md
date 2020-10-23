
# Create a Calculator with Python and PyQt



## Create a Skeleton
1. Create a pycalc.py file and import the required modules and classes from PyQt5.QtWidgets:
- QApplication 
- QMainWindow
- QWidget

2. Create the calculator's GUI with class PyCalcUi
- This class inherits from`QMainWindow` 
Add main window properties like title and size with `setWindowTitle()` and `setFixedSize()`
- Create a `QWidget object` to act as the central widget (remember you need to set a central widget first because the GUI inherits rom `QMainWindow`. ) This object will be the parent for the rest of the GUI component

3. Create the client code:
- Define the calculator's `main function` (best practice). This function is the **entry point** to the application.
- `main`:
1. creates a `QApplication` object called `pycalc`
2. displays the GUI with `view.show()`
3. run the application's event loop with `pycalc.exec_()` and wrap the function in `sys.exit()`

4. Execute the calculator's main loop


## The View's Display and Buttons
The GUI skeleton doesn't look like a calculator--you need to complete the GUI by adding the display and buttons.<br>
Add additional imports to the pycalc.py file for:
- Qt
- QGridLayout - to arrange the buttons
- QLineEdit - for the display
- QPushButton - for the buttons
- QVBoxLayout - for the calculator's general layout

Update the initalizer for `PyCalcUi` by:
1. adding a general layout with `QVBoxLayout` - this places the display at the top and the buttons in a grid layout at the bottom
2. nest the general layout within the central widget layout
3. create/implement the display (`_createDisplay()`) widget with the `QlineEdit` object and add it to the general layout with `generalLayout.addWidget`
4. create/implement the buttons widget with the `_createButtons()`. Use a `dictionary` to hold each button's text and position on the grid. Use `QGridLayout` to arrange the buttons on the calculator's window.

### Creating the Buttons
In the _createButtons() definition:
1. First create an empty `dictionary` to hold the calculator buttons.<br>
```self.buttons = {}```<br>
2. Next create a temporary dictionary to store their labels and positions on the grid layout (called "buttonsLayout").<br>
```
buttonsLayout = QGridLayout()
buttons = { '7': (0,0),
            '8': (0,1),
            ...
            '+': (3, 3),
            '=': (3, 4)
        }
```
<br> 

3. use a `for` loop to create the buttons and add them to `self.buttons` and buttonsLayout. Every button should have a fixed size of 40 x 40 pixels.
```
for btnText, pos in buttons.items():
    self.buttons[btnText] = QPushButton(btnText)
    self.buttons[btnText].setFixedSize(40, 40)
    buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
```

## Update View's Display Information 
The calclator's GUI (View) now shows the display and buttons, but to update the information shown on th display and complete the View class for the calculator the following methods need to be added:
- setDisplayText() - to set set and update the display text
- displayText() - to get the current display text
- clearDisplay() - to clear the display text
These methods will form the GUI public interface.


## The Basic Controller
Connect the View to the Model with the Controller class. The GUI interface is done, but the calculator won't work until the Model and Controller are implemented. The Controller class will make the calculator perform actions in response to user events.<br>
The Controller class performs three main tasks:
1. Access the GUI's public interface
2. Handle the creation of math expressions
3. Connect button "clicked" **signals** with appropriate **slots**.

To create the basic Controller:
1. Define a "PyCalcCtrl" class and pass it an instance of the "PyCalcUi" View.
- This instance creates full access to the View's public interface.
2. Define a "_buildExpression()" method to handle the creation of math expressions and update the calculator's display based on user input.
3. Define a "_connectSignals()" method to connect printable buttons with the "_buildExpression()" method. 
- This allows users to create math expressions by clicking calculator buttons.
Make sure to  import `functools.partial`:<br>
```from functols import partial```<br> to connect **signals** with methods that need extra arguments.
4. Connect the "clear" button to the "_view.clearDisplay()" method to clear the display text.<br>

For the Controller to work, "main()" must be updated:
Between `view.show()` and `sys.exit(pycalc.exec_())`, create an instance of PyCalcCtrl() and pass in view as an argument:
```PyCalcCtrl(view=view)```


## The Model
The Model is the layer of code that handles the business logic, math calculations in this case. The Model here is a single function "evaluateExpression," with a `try..except` block.
- A best practice wold have the `try...except` block catch specific exceptions (not coded here). 
- Use `eval()` to evaluate a string as an expression. 
- Define a global contstant to handle errors. Note: `eval()` should only be used with trusted inputs.


## Completing the Controller 
After completing the calculator's Model, add logic to PyCalcCtrl to process the calculations and ensure the equal sign is functional.
4. Add the model to the PyCalcCtrl init function so that the class receives instances from both the Model and the View

5. Add a _calculateResult() method to evaluate expressions and display the result

6. Add an if statement to _buildExpressions() that checks if an error occured with the global ERROR_MSG 

7. Add two more connections inside _connectSignals() to connect the equal sign and "Enter" button

8. update main():
- declare a model variable, which holds a reference to evaluateExpression(), and pass it as a parameter

## Troubleshooting
Troubleshooting checklist: 
- is everything spelled correctly?
- is everything indented correctly?
- is everything imported?
- is the main function defined correctly?




