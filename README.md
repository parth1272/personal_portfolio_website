# personal_portfolio_website
***<h1>Overview</h1>***

This code is a Flask web application that serves a website(personal portfolio) with a contact form. The form allows users to enter their name, email, and a message, which is then sent via email to a specified email address using the SMTP protocol.

<h2>How to setup and run the site</h2>
1. Open the Pycharm and import all these file as below

![Screenshot (75)](https://github.com/parth1272/personal_portfolio_website/assets/134066202/e852392d-af62-4f0c-b69d-40c6e40f9055)

2. now run the program (Server) and go to the link which is the output of the program.

 ![Screenshot (76)](https://github.com/parth1272/personal_portfolio_website/assets/134066202/cc71c939-747c-4790-b57e-f8a9ed5208f4)


<h2>Let's break down the code:</h2>


Import Statements

1. Requests: This library is not used in the provided code, so its import statement can be removed.

2. Flask, render_template, request: These are Flask modules used for creating a web application, rendering HTML templates, and handling HTTP requests.

3. Smtplib: This module is used for sending emails using the Simple Mail Transfer Protocol (SMTP).

4. Os: This module is used for interacting with the operating system, particularly for accessing environment variables.


Environment Variables:

1. The code expects two environment variables, OWN_EMAIL and OWN_PASSWORD, to be set. These variables should contain the email address and password of the sender's Gmail account.
2. For getting the OWN_PASSWORD(veriable) i.e your password from gmail simply go the the gmail account and clicl on the profile icon and select "Manage Your Google Account".
3. Then go to the security and select 2-step verification
4. After that create app passord and coppy that password and pest it into your OWN_PASSWORD(veriable)

<h2>Flask Application Setup:</h2>

An instance of the Flask class is created with the name app.

Home Route (/):
The home route renders the "index.html" template when the root URL ("/") is accessed.
Contact Route (/contact):
This route handles both GET and POST requests.
If the request method is POST, it retrieves the data from the submitted form (name, email, and message) and calls the send_email function with this data.
After sending the email, it renders the "go.html" template.

send_email Function:
1.This function takes the user's name, email, and message as parameters.
2.It uses the smtplib module to connect to the Gmail SMTP server, starts a TLS connection, and logs in using the provided email and password.
3.It then sends an email to the specified recipient (in this case, the same email as the sender) with a subject and content that includes the user's input (name, email, and message).

<h1>Run the Application:</h1>
1.The if __name__ == "__main__": block runs the Flask application when the script is executed directly.
2.The app.run(debug=True) statement starts the development server with debugging enabled.



![image](https://github.com/parth1272/personal_portfolio_website/assets/134066202/843dc21c-8cb5-4bf7-b358-a022a3d6538f) Important Note:

Storing email credentials (especially passwords) directly in code or environment variables is not recommended for security reasons. In a production environment, consider using a more secure method, such as a configuration file or a secure vault system.
Additionally, using a user's email and password directly to send emails may not be the best practice. Instead, consider using an email service with an API key for better security.




