# csv_to_sql
Dynamically load csv file to new ms sql table

## Getting Started

### Clone to repo
```
$ git clone https://github.com/kipp-bayarea/csv_to_sql.git
```

### Install dependencies
```
$ pipenv install
```

### Setup environment variables
```
$ touch .env
```

Add the following key value pairs to the `.env` file:

```
DB_SERVER=""
DB=""
DB_SCHEMA=""
DB_USER=""
DB_PWD=""
```

### Run the code

```
$ pipenv run python main.py --filepath <path> --tablename <name>
```

Be sure to replace <path> and <name> with the filepath and table name and you want to use.