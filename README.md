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
