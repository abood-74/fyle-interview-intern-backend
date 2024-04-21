# Fyle Backend Challenge

## Installation

1- Clone the repository and proceed with steps mentioned below
```sh
git clone https://github.com/abood-74/fyle-interview-intern-backend.git
```


### Getting Started
#### 1- Run the following commands to create the image and run the container.
```
cd fyle-interview-intern-backend.git
docker-compose build
docker-compose up
```
#### 2- Run the following command to list all running Docker containers.
```
docker ps
```
#### 3- Locate the name of the target container in the NAMES column.
#### 4- Start a bash shell by running the following command with the target container name.
```
docker exec -it <container_name> bash
```



### Reset DB 

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```

### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```
