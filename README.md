# CITS3403-Project

The project is a simple flask web app for movie polls. After login, users can vote for their favourite movie in each poll for once.
The purpose of this web application is getting the movie lover community together to vote for their favourite movies, expressing their preference and letting them know how do others think of movies.
The social choice mechanism used is First Past the Post Voting. In each poll, a user can only vote for one candidate, and the candidate with the most votes ranks the first. The reason of applying this mechanism is that it can enable charts to give users an intuitionistic view of how many users are involved in a poll and how is the distribution of their favour. Moreover, this mechanism needs the least time to vote.

## Architecture
The index page is the first landing page of this web application. What can be seen first is a carousel showing that this application categorises movies in 6 kinds: Romantic Movie, Horror Movie, Fiction Movie, Documentary Movie, Comedy Movie, and Action Movie. The tag on each carousel page links to the corresponding search result in Youtube. Below the carousel, is the note for users and all polls available now. If the user has not logged in, then clicking the poll name or clicking the user icon on the top right corner will skip to the login page.

In the login page, if the user has registered, he can login with the user name and password. Otherwise, a register button is for new users. When the user login, if he inputs a wrong user name or password, he will fail and an error message will show up at the bottom of the login form. If login successful, the user will redirect back to the index page.

In the registration page, a new user need to input his username, password, and email address, and to choose the movie categories that he prefers. There are restrictions on input fields, if wrong inputs are detected, error message will show up in the registration form.

### Normal User
After a normal user logins and gets redirected back to the index page, the user can see that polls are divided into three sections: Recommended Polls, Maybe You Like, Voted Polls. Recommended Polls are the un-voted polls in the user's favourite movie categories; Maybe You Like part contains un-voted polls that are not in the user's favourite movie categories; Voted Polls part contains the polls the user has voted before.


<<<<<<< HEAD
=======
A simple flask app for movie polls.The application perform voting or ranking activity (view vote result), based on the inputs from users. Mechanism that we using is First past the post voting.
An adminstrator view, that can add and delete polls, delete responses, and add and delete users.
An user(login) view, that can view polls and current standings, and submit responses to polls.
A general view that can just view polls.

>>>>>>> a4a1e1997db1de64ad4b0cd5800e3a0215efb214
## Getting Started

Activate the python virtual environment:
`$source venv/bin/activate`

To run the app:
`$flask run`

To stop the app:
`$^C`

To exit the environment:
`$deactivate`

### Prerequisites

Requires python3, flask, venv, and sqlite


### Installing

Install python3, sqlite3, flask, wtf,sqlalchemy

1. Set up a virtual environment:
 - use pip or another package manager to install virtualenv package `pip install virtualenv`
 - start the provided virtual environment
   `source venv/bin/activate`
 - This should include flask and all the required packages
 `pip install flask`
 `pip install flask_script`
 `pip install python-dotenv`
 `pip install flask-wtf`
 `pip install flask-sqlalchemy`
 `pip install flask-migrate`
 `pip install flask-login`
 `pip install wtforms_sqlalchemy`
<<<<<<< HEAD

=======
  
>>>>>>> a4a1e1997db1de64ad4b0cd5800e3a0215efb214
2  [Windows instructions](http://www.sqlitetutorial.net/download-install-sqlite/)
  In \Linux, `sudo apt-get install sqlite`
3. Build the database: `flask db init`
4. `flask run`

This should start the app running on localhost at port 5000, i.e. [http://localhost:5000/index](http://localhost:5000/index)

## Running the tests

To run the test you need to comment out this line in app.__init__.py

 #from app import routes,models


To run unit tests
`python -m test.test1`

## Deployment

via localhost

## Built With

git

## Authors

* **Minrui Lu ** - *Initial work* - [raymondluk1995](https://github.com/raymondluk1995)
* **Wenjing Zheng ** - *Initial work* - [wenjing33](https://github.com/wenjing33)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Built following the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by **Miguel Grinberg**.
* Built following the [Pair up Flask App](https://github.com/drtnf/cits3403-pair-up) by **Tim French**
<<<<<<< HEAD
* Build following the [How to Create a Login Form with Ajax](https://www.webucator.com/how-to/how-create-login-form-with-ajax.cfm)
=======
* Build following the [How to Create a Login Form with Ajax](https://www.webucator.com/how-to/how-create-login-form-with-ajax.cfm) 
>>>>>>> a4a1e1997db1de64ad4b0cd5800e3a0215efb214
* Build following the [Form Submission Using Ajax, PHP and Javascript](https://www.formget.com/form-submission-using-ajax-php-and-javascript/)
* Build following the [Submit AJAX Forms with jQuery and Flask](https://www.youtube.com/watch?v=IZWtHsM3Y5A)
