## Installing the Dependencies
### Requirements
- Python 3.5 >=
- Windows Machine
- `pip install -r requirements.txt`
- Please ensure that the Microsft Build Tools ( microsoft visual c++ 14.0) is already installed[ prior to installing the modules]

## How to run the Project
- `uvicorn main:app --reload`

On Uvicorn server, run the `main` file and inside that file the application is named as `app`, and `--reload` capture the latest changes

## How to get the API Documentation
- http://localhost:8000/docs#/
This opens the Swagger link of the available APIs and the requested body and response 
- http://localhost:8000/redoc Just the API Documentation