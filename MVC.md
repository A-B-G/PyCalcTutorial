# Model-View-Controller (MVC) Design Pattern
The MVC pattern has three layers of code.
1. Model - handles the app's business logic
- This contains the core functionality and data.
2. View - implements the app's GUI and receives user actions and events
- This hosts all the application widgets the end-user interacts with
3. Controller - connects the model and the view so that the application works
- The controller receives user events (requests), triggering the model. The model delivers the requested result (data), which the controller forwards to the view.