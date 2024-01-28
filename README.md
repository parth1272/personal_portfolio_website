# personal_portfolio_website

This code is a simple Flask web application that serves a basic website with a contact form. The form allows users to enter their name, email, and a message, which is then sent via email to a specified email address using the SMTP protocol.

Let's break down the code:

Import Statements:

requests: This library is not used in the provided code, so its import statement can be removed.
Flask, render_template, request: These are Flask modules used for creating a web application, rendering HTML templates, and handling HTTP requests.
smtplib: This module is used for sending emails using the Simple Mail Transfer Protocol (SMTP).
os: This module is used for interacting with the operating system, particularly for accessing environment variables.
Environment Variables:

The code expects two environment variables, OWN_EMAIL and OWN_PASSWORD, to be set. These variables should contain the email address and password of the sender's Gmail account.
Flask Application Setup:

An instance of the Flask class is created with the name app.
Home Route (/):

The home route renders the "index.html" template when the root URL ("/") is accessed.
Contact Route (/contact):

This route handles both GET and POST requests.
If the request method is POST, it retrieves the data from the submitted form (name, email, and message) and calls the send_email function with this data.
After sending the email, it renders the "go.html" template.
send_email Function:

This function takes the user's name, email, and message as parameters.
It uses the smtplib module to connect to the Gmail SMTP server, starts a TLS connection, and logs in using the provided email and password.
It then sends an email to the specified recipient (in this case, the same email as the sender) with a subject and content that includes the user's input (name, email, and message).
Run the Application:

The if __name__ == "__main__": block runs the Flask application when the script is executed directly.
The app.run(debug=True) statement starts the development server with debugging enabled.
Important Note:

Storing email credentials (especially passwords) directly in code or environment variables is not recommended for security reasons. In a production environment, consider using a more secure method, such as a configuration file or a secure vault system.
Additionally, using a user's email and password directly to send emails may not be the best practice. Instead, consider using an email service with an API key for better security.
