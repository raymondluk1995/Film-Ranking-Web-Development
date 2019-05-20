# CITS3403-Project

## Author
Minrui Lu 22278526
Wenjing Zheng 22126041

The project is a simple flask web application for movie polls. After login, users can vote for their favourite movie in each poll for once.

The purpose of this web application is getting the movie lover communities together to vote for their favourite movies, to express their preference and to know how do others think of movies.

The social choice mechanism used is First Past the Post Voting. In each poll, a user can only vote for one candidate, and the candidate with the most votes ranks the first. The reason of applying this mechanism is that it can enable charts to give users an intuitionistic view of how many users are involved in a poll and how is the distribution of their favour. Moreover, this mechanism needs the least time to vote.

## Architecture
The index page is the first landing page of this web application. What can be seen first is a carousel showing that this application categorises movies in 6 kinds: Romantic Movie, Horror Movie, Fiction Movie, Documentary Movie, Comedy Movie, and Action Movie. The tag on each carousel page links to the corresponding search result in Youtube. Below the carousel, is the note for users and all polls available now. If the user has not logged in, then clicking the poll name or clicking the user icon at the top right corner will skip to the login page.

In the login page, if the user has registered, he can login with the user name and password. Otherwise, a register button is for new users. When the user logins, if he inputs a wrong user name or password, he will fail and an error message will show up at the bottom of the login form. If login is successful, the user will be redirected back to the index page.

In the register page, a new user needs to input his username, password, and email address, and to choose the movie categories that he prefers. There are restrictions on input fields: if wrong inputs are detected, error message will show up in the registration form. After registering successfully, the user will be redirected back to the login page.

### Normal User
After a normal user logins and gets redirected back to the index page, the user can see polls are divided into three sections: Recommended Polls, Maybe You Like, Voted Polls. Recommended Polls are the un-voted polls in the user's favourite movie categories; Maybe You Like part contains un-voted polls that are not in the user's favourite movie categories; Voted Polls part contains the polls the user has voted before.

When a user clicks a un-voted poll tag on the index page, he will be directed to the template page which renders the corresponding poll. What can be seen are a single-choice form displaying options; a bar chart showing the current voting rank and vote numbers; a pie chart showing the vote proportions of each option. After the user commits his choice, the page gets refreshed and the user can see the latest result after his vote. At this moment, the commit button changes to a dummy button showing "Voted" and the user's previous choice is shown at the bottom of the form.

When a user wants to logout, he can click the user icon at the top right corner in the navigation bar, and a dialog box will pop out asking whether the user wants to logout. If the user clicks the Logout button, he finishes the logout process and gets redirected back to the index page.

### Admin User
After an admin user logins and gets redirected back to the index page, what can be seen added is a menu of five buttons: Create Poll, Add User, Delete Poll, Delete User, Delete Response. Unlike a normal user, the index page puts all polls in one section. This is supposed to be convenient for poll administration.

After clicking the Create Poll button, the admin user goes to the Create Poll page. In this page, an admin user can create a poll with maximum 10 options. This page is based on JavaScript and JQuery. If the user inputs something illegal, JavaScript will alert the user and not pass the values to the back end via AJAX.

After clicking the Add User button, the admin user goes to the Add User page. The page is similar to the register page, but with one more option for deciding the admin attribute of the new user. If choose yes, the new user is an administrator, otherwise, the new user is just a normal user.

When the admin user goes to the Delete Poll page, a multi-select form is provided. An admin user can delete multiple polls at once. After a poll is deleted, its associated data (options and response) is also removed.

Similar to the Delete Poll page, in Delete User page, an admin user can delete multiple users at once and associated data will be also deleted. The delete response page is the same case.

## Development
- March:

  Minrui Lu: Login HTML page, Register HTML page and Index HTML page drafts are done, along with a CSS file.

- April:
  No commitment

- May:  

  Wenjing Zheng: Create Poll HTML page draft, testing modules, ReadMe file

  Minrui Lu: Flask Backend, Create Poll page, Delete Poll page, Add User Page, Delete User page, Delete Response page, Responsive CSS, shared_part.js JavaScript file, ReadMe file, Chart.js application, dummy data insertion

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
Python3 environment

### Dependencies
alembic, Flask, Flask-Login, Flask-Migrate, Flask-Script, Flask-SQLAlchemy, Flask-WTF, itsdangerous, Jinja2, Mako, MarkupSafe, python-dateutil, python-dotenv, python-editor, SQLAlchemy, Werkzeug, WTForms, WTForms-SQLAlchemy

### Installing

1. Set up a virtual environment:
 - `$python3 -m venv venv`
 - Or use pip or another package manager to install virtualenv package `$pip install virtualenv`
 - start the provided virtual environment
   `$source venv/bin/activate`

2. Execute the following code to install environment: `$pip install -r requirements.txt`
3. Build the database: `$flask db init`
4. `$flask run`

This should start the app running on localhost at port 5000, i.e. [http://localhost:5000/index](http://localhost:5000/index)

## Running the tests

To run the test you need to comment out this line in app.__init__.py

 #from app import routes,models


To run unit tests
`$python -m test.test1`

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
* External libraries introduced: [fontawesome](https://fontawesome.com/),[Google Fonts](https://fonts.google.com/),[JQuery](https://jquery.com/), [Chart.js](https://www.chartjs.org/),[bootstrap](https://getbootstrap.com/)
* Build following the [HTML5 Tutorial](https://www.w3schools.com/html/), [CSS Tutorial](https://www.w3schools.com/css/default.asp),[JavaScript Tutorial](https://www.w3schools.com/js/default.asp)
* Build following the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), [Flasky](https://github.com/miguelgrinberg/flasky) by **Miguel Grinberg**.
* Build following the [Pair up Flask App](https://github.com/drtnf/cits3403-pair-up) by **Tim French**
* Build following the [Submit AJAX Forms with jQuery and Flask](https://www.youtube.com/watch?v=IZWtHsM3Y5A)
* Picture sources: [Logo](https://www.vectorstock.com/royalty-free-vector/movie-film-play-people-abstract-logo-vector-4097798), [background_original](https://medium.com/edmodoblog/more-than-coding-what-students-really-learn-from-computer-science-3d6870387fbc),[One Day](http://intrigue.ie/books-every-woman-read-one-day/),[IT](http://www.slaphappylarry.com/stephen-kings-it-storytelling-techniques/it-2017-movie-poster/),[Interstellar](https://wallpapershome.com/movies/sci-fi/interstellar-movie-matthew-mcconaughey-space-suit-snow-381.html),[Score](https://www.score-movie.com/), [Mr Bean's Holiday](https://images.app.goo.gl/D9mv1dzvzCDVWTDp8), [Fast and Furious 8](https://free4kwallpaper.com/fast-and-furious-8-movie-4k-wallpaper/)
* Slideshow Reference: [How TO - Slideshow](https://www.w3schools.com/howto/howto_js_slideshow.asp)
* Bootstrap Form Reference: [Forms](https://getbootstrap.com/docs/4.0/components/forms/)
* Checkbox WTForms Reference: [Checkbox WTForms Example (in Flask) ](https://gist.github.com/einSelbst/1797d4457814f31accfed825da202b31)
* Chart.js Reference: [10 Chart.js example charts to get you started](https://tobiasahlin.com/blog/chartjs-charts-to-get-you-started/), [Show values on top of bars in chart.js](https://stackoverflow.com/questions/42556835/show-values-on-top-of-bars-in-chart-js/42562284),[ChartJS: datalabels: show percentage value in Pie piece](https://stackoverflow.com/questions/52044013/chartjs-datalabels-show-percentage-value-in-pie-piece)
