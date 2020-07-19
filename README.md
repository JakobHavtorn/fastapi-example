# fastapi-example
Example of FastAPI usage

## Installation

`pip install .`

## Running

`uvicorn example.main:app --reload`

The command uvicorn example.main:app refers to:

- `main`: the file `main.py` (the Python "module").
- `app`: the object created inside of `main.py` with the line `app = FastAPI()`.
- `--reload`: make the server restart after code changes. Only do this for development.

## Using

Get an item: http://127.0.0.1:8000/items/5?q=a-test-query

## Documentation

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc
