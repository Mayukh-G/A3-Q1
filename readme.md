## Dependencies
* dotenv `pip install dotenv`
* psycopg `pip install psycopg; pip install "psycopg[binary,pool]"`

## Running instructions
Create a `.env` file in the same directory as `Assignment3Q1App.py`. Fill the .env file with the following variables:
```js
DB_NAME = "your_database_name"
UNAME = "your_username"
PASSWORD = "your_password"
PORT = "your_database_port"
```

`Assignment3Q1App.py` contains a class called `DataBase` which contains the desired methods which can be called however you wish. The constuctor parameters of `DataBase` 
can be filled by using `config` dictionary which will contain variables set in the `.env` file. For example, to retreive password: `config["PASSWORD"]`.

Running `Assignment3Q1App.py` will run all availiable methods for `DataBase` with preset information passed as arguments.

Tested only using Python 3.12.