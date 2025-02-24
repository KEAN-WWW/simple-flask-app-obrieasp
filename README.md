[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/d66Ph9QZ)
# simple-flask-app
To finish this assignment, you will need to know how to make simple Flask application with template html.

1. create your application script under `app` folder to make a Flask application. You should name your application script as `app.py` and your flask instance as `app` in code. You can check the announcement for the setup guide. 
2. create default route page to demonstrate text content `Hello CPS3500!`
3. create a new route page to `new_page` and show the text content `This is a New Page!`
4. create a folder named `templates` under folder `app`
5. create a template HTML file under `templates`. Any name and any content is fine for now
6. create a new route page to use `render_template` method from Flask to display that HTML template file. In addition, make it route to `user` and followed with a variable. We need to use this route page to accept any parameter.
7. edit the HTML template file with Jinja syntax to create a branch condition to detect if a username is `jack`. If it is, print its name to all capitalized form in a message `Hello, [THE CAPTIALIZED NAME]!`. If not, display message `Hi, Anonymous!`.
8. push it back for the grade.


   **_Hint_**: You will need to use Jinja variable and `if-else` statement and `upper()` method. Please check the announcement to browse the `Jinja if, else` section for the guide. And you are free to use any HTML template online or in that guide to finish it.


Don't forget to use `pytest --pylint` to see if local tests are passed before you do the push.
