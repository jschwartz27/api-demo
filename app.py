from fastapi import FastAPI
from backend.employee import Employee, EmployeeDB

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}})


@app.get("/")
async def root() -> str:
    return "Hello and welcome to your deep dive session! You can find the tasks in the README under api-interface/training. Good luck!"


@app.get("/lucky_number/")
async def lucky_number() -> str:
    """
    Task 1

    GET /lucky_number/

    Create the logic to return a random number, formatted within a string.
    Through calling this endpoint, an expect a return similar to:

    200 (status code): Your lucky number for the day is: 42


    Consider using a number generating function from the random_numbers.RandomNumbers class,
    or feel free to create your own!
    """
    return "Implement me!"


@app.get("/greetings/")
async def greetings() -> str:
    """
    Task 2:

    GET /greetings/

    By calling this endpoint with a mandatory parameter 'name' a response is expected like

    200 (status code): Welcome DiveIn

    if the query parameter 'name' is omitted a status code 404 is expected

    """
    return "Implement me!"


@app.get("/weekday_calculator/")
async def weekday_calculator():
    """
    Task 3:

    GET /weekday_calculator/

    by calling this endpoint with a mendatory header 'n' a response is expected like

    200 5 days from now is a Monday

    if the header 'n' is omitted a status code 422 is expected with some details on the missing header
    if the header 'n' is not a valid number a status code 422 is expected with some details on expected data type

    consider using the backend feature 'day_calculator.get_weekday_in_n_days(n)'

    """
    return "Implement me!"


@app.get("/login/")
async def login():
    """
    Task 4:

    GET /login/

    by calling this endpoint with the mandatory baseAuth header (username: DiveIn password: 1234) an response is expected like

    200 Login successful!

    if the baseAuth header is omitted a status code 401 is expected with some details on the missing baseAuth
    if no valid username and/or password are provided a status code 401 is expected with the hint that username/password is invalid

    consider implementing user_loader() with check for DiveIn:1234

    """
    return "Implement me!"


# ==========================================
# Employee Section
# ==========================================

db = EmployeeDB(
    populate_db=[
        Employee(name="Alice", age=20),
        Employee(name="Bob", age=42),
        Employee(name="Charles", age=50),
    ]
)


@app.get("/employee/")
async def employee():
    """
    Read all

    GET /employee/

    by calling this endpoint a response is expected like

    200 [
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

    consider using the backend feature 'db.get_all()'

    """
    return "Implement me!"


@app.post("/employee/", response_model=Employee)
async def create_employee():
    """
    Create

    POST /employee/

    by calling this endpoint with a payload like

    {
        "name": "DiveIn",
        "age": 42
    }

    a response is expected like

    200 {
            "id": 4
            "name": "DiveIn",
            "age": 42
        }

    if the endpoint is called without payload a status code 422 is expected with some information on the needed payload
    if the key 'age' is not a valid int a status code 422 is expected with some information on the expexted data type

    consider using the backend feature 'db.create(employee=employee)'

    """
    return "Implement me!"


@app.get("/employee/{id}", response_model=Employee)
async def read_employee():
    """
    Read

    GET /employee/{id}

    by calling this endpoint with the 'id' a response is expected like

    200 {
            "id": 1,
            "name": "Alice",
            "age": 20
        }

    if the path parameter 'id' does not correspond to an id in the db a status code 404 is expected with some information that no resource for the id is found

    consider using the backend feature 'db.read(id=id)'

    """
    return "Implement me!"


@app.put("/employee/{id}", response_model=Employee)
async def update_employee():
    """
    Update

    PUT /employee/{id}

    by calling this endpoint with a payload like

    {
        "id": 4
        "name": "DiveIn",
        "age": 99
    }

    a response is expected like

    200 {
            "id": 4
            "name": "DiveIn",
            "age": 99
        }

    if the endpoint is called without payload a status code 422 is expected with some information on the needed payload
    if the path parameter 'age' or 'id' is not a valid int a status code 422 is expected with some information on the expected data type
    if the resource for the path parameter 'id' is not found in the backend a status code 404 is expected with some information on the missing resource

    consider using the backend feature 'db.update(id=id, employee=employee)'

    """
    return "Implement me!"


@app.delete("/employee/{id}", response_model=Employee)
async def delete_employeelogin():
    """
    Delete

    DELETE /employee/{id}

    by calling this endpoint with 'id' a response is expected like

    200 {
            "id": 4
            "name": "DiveIn",
            "age": 99
        }

    if the resource for the pathparameter 'id' is not found in the backend a status code 404 is expected with some information on the missing resource

    consider using the backend feature 'db.delete(id=id)'

    """
    return "Implement me!"
