# FastAPI Simple API for Plotting Data

This repository contains a simple API implementation using FastAPI to plot data from a requested URL. You can use this API to fetch data from a CSV file hosted at a specified URL and generate plots dynamically through API requests.

## Technologies Used
- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+.

## Usage

1. Clone this repository: `git clone <repository_url>`
2. Navigate to the `fastapi` directory: `cd fastapi`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the FastAPI server: `uvicorn main:app --reload`
5. Open your web browser and go to `http://127.0.0.1:8000/docs` to access the Swagger UI for API documentation.
6. Use the provided endpoint to fetch data from a CSV file and generate plots.

## Example Usage
To plot data from the provided URL `https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv`, you can make a POST request to the `/plot` endpoint with the URL in the request body.

### Endpoint
- Endpoint: `/plot`
- Method: `POST`
- Request Body: `{ "url": "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv" }`

## Notes
- Make sure to replace the example URL with the URL of the CSV file you want to plot data from.


