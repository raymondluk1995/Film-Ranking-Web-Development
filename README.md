# CITS3403-Project


A simple flask app for movie polls.The application perform voting or ranking activity (view vote result), based on the inputs from users.
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

```

```

### Installing

Install python3, sqlite3, flask, wtf,sqlalchemy

1. Set up a virtual environment:
 - use pip or another package manager to install virtualenv package `pip install virtualenv`
 - start the provided virtual environment
   `source venv/bin/activate`
 - This should include flask and all the required packages
 pip install flask 
 pip install flask_script
 pip install python-dotenv
 pip install flask-wtf
 pip install flask-sqlalchemy
 pip install flask-migrate
 pip install flask-login
 pip install wtforms_sqlalchemy
  
 - [Windows instructions](http://www.sqlitetutorial.net/download-install-sqlite/)
 - In \*nix, `sudo apt-get install sqlite`
3. Build the database: `flask db init`
4. `flask run`

This should start the app running on localhost at port 5000, i.e. [http://localhost:5000/index](http://localhost:5000/index)

## Running the tests

To run the test you need to comment out this line in app.__init__.py

 #from app import routes,models



To run unit tests
`python -m tests.unittest`



## Deployment

via localhost

## Built With

vim and git

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

## Authors

* **Minrui Lu ** - *Initial work* - [raymondluk1995](https://github.com/raymondluk1995)
* **Wenjing Zheng ** - *Initial work* - [wenjing33](https://github.com/wenjing33)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Built following the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by **Miguel Grinberg**.
