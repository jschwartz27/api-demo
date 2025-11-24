# api-demo

After installing conda
(https://www.anaconda.com/download)
run the following command to create an environment:
```bash
conda env create -f environment.yaml
```

Next, to activate the environment run:
```bash
conda activate api-demo
```

And, if you wish to deactivate the environment:
```bash
conda deactivate
```

In order to run the FastApi solution, run the following command:
```bash
uvicorn app:app --reload
```

If swagger does not open automatically, open your browser and go to (update port if necessary):
```bash
http://127.0.0.1:8000/docs
```

If you update the environment.yaml file and want to update your environment, from within the environment run:
```bash
conda env update --file environment.yaml  --prune
```

# Tasks

## Task 1
```
GET /lucky_number/
```
Create the logic to return a random number, formatted within a string.
Through calling this endpoint, an expect a return similar to:

```
200 (status code): Your lucky number for the day is: 42
```

Consider using a number generating function from the random_numbers.RandomNumbers class, or feel free to create your own!

## Task 2
```
GET /greetings/{name}
```
by calling this endpoint with a mandatory parameter `name` an response is expected like

```
200 (status code): Hallöchen, {name}!
```

If the query parameter 'name' is omitted a status code 404 is expected

Usefull link for fastapi: 
- https://fastapi.tiangolo.com/tutorial/query-params/

## Task 3:
    
    GET /weekday_calculator/
    
by calling this endpoint with a mendatory header 'n' an response is expected like
    
    200 5 days from now is a Monday
    
if the header 'n' is omitted a `status code 422` is expected with some details on the missing header
if the header 'n' is not a valid number a `status code 422` is expected with some details on expected data type
    
consider using the backend feature 'day_calculator.get_weekday_in_n_days(n)'

usefull link for fastapi: https://fastapi.tiangolo.com/tutorial/header-params/


## Task 4:

    GET /login/
    
by calling this endpoint with the mandatory baseAuth header (username: DiveIn password: 1234) an response is expected like
    
    200 Login successful!
    
if the baseAuth header is omitted a `status code 401` is expected with some details on the missing baseAuth
if no valid username and/or password are provided a `status code 401` is expected with the hint that username/password is invalid
    
consider implementing user_loader() with check for DiveIn:1234

usefull link for fastapi: https://fastapi.tiangolo.com/advanced/security/http-basic-auth/


# Task 5 - Employees

consider using the 'db' to perform CRUD operations

## Read all

    GET /employee/

by calling this endpoint a response is expected like

```JSON
// 200
[
    {
        "id": 1,
        "name": "Alice",
        "age": 20
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 42
    },
    {
        "id": 3,
        "name": "Charles",
        "age": 50
    }
]
```
consider using the backend feature 'db.get_all()'
    

## Create

    POST /employee/

by calling this endpoint with a payload like

```JSON
{
    "name": "DiveIn",
    "age": 42
}
```

a response is expected like
```JSON
// 200
{
    "id": 4,
    "name": "DiveIn",
    "age": 42
}
```
if the endpoint is called without payload a `status code 422` is expected with some information on the needed payload
if the key 'age' is not a valid int a `status code 422` is expected with some information on the expexted data type

consider using the backend feature 'db.create(employee=employee)'


## Read

    GET /employee/{id}

by calling this endpoint with the 'id' a response is expected like

```JSON
// 200
{
    "id": 1,
    "name": "Alice",
    "age": 20
}
```
if the path parameter 'id' does not correspond to an id in the db a `status code 404` is expected with some information that no resource for the id is found    
consider using the backend feature 'db.read(id=id)'

usefull link for fastapi: https://fastapi.tiangolo.com/tutorial/path-params/

## Update

    PUT /employee/{id}

by calling this endpoint with a payload like
```JSON
{
    "id": 4,
    "name": "DiveIn",
    "age": 99
}
``` 
a response is expected like
```JSON
// 200
{
    "id": 4,
    "name": "DiveIn",
    "age": 99
}
```
if the endpoint is called without payload a `status code 422` is expected with some information on the needed payload
if the path parameter 'age' or 'id' is not a valid int a `status code 422` is expected with some information on the expected data type
if the resource for the path parameter 'id' is not found in the backend a status code 404 is expected with some information on the missing resource

consider using the backend feature 'db.update(id=id, employee=employee)'


## Delete

    DELETE /employee/{id}

by calling this endpoint with 'id' a response is expected like
```
204 No Content
```

OR
```JSON
// 200
{"message": "Employee with id: {id}, deleted"}
```
if the resource for the pathparameter 'id' is not found in the backend a `status code 404` is expected with some information on the missing resource

consider using the backend feature 'db.delete(id=id)'