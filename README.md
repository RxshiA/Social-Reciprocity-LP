# Adaptive Learning API

This project is an Adaptive Learning API built with FastAPI. The API provides endpoints for submitting feedback, saving and retrieving child progress, and generating stories and multiple-choice questions (MCQs) based on the child's learning level.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/RxshiA/Social-Reciprocity-LP.git
    cd Social-Reciprocity-LP
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add the following environment variables:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    MONGO_URI=your_mongo_uri
    ```

## Running the Application

1. Start the FastAPI server:
    ```sh
    uvicorn app.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Running Tests

1. To run the tests, use the following command:
    ```sh
    pytest
    ```

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/main.yml`. It runs the tests and uploads coverage reports to Codecov.

## API Endpoints

### `/api/submit_feedback/` (POST)

Submit feedback for a child and get a new story and MCQs based on the child's learning level.

### `/api/save_progress/` (POST)

Save the progress of a child.

### `/api/get_progress/{child_id}` (GET)

Retrieve the progress of a child by their ID.

## License

This project is licensed under the MIT License.