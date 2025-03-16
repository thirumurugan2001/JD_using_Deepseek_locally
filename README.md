# Job Description Generator

## Overview
This project is a Flask-based web application that generates job descriptions based on user-provided data using an AI model. The AI model used is `deepseek-r1:1.5b` via Ollama. The application accepts job-related inputs, validates them, and then generates a structured job description in JSON format.

## Features
- Web interface for inputting job details
- Data validation to ensure required fields are filled
- AI-based job description generation
- JSON extraction from AI response
- Display results in an HTML template
- Error handling and logging

## Technologies Used
- Flask (Web Framework)
- Ollama (AI Model for Job Description Generation)
- HTML/CSS (Frontend Templates)
- Python (Backend Logic)
- JSON (Data Formatting)
- Regular Expressions (JSON Extraction)

## Installation & Setup

### Prerequisites
- Python 3.x
- Flask
- Ollama Installed

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/thirumurugan2001/JD_using_Deepseek_locally.git
   cd JD_using_Deepseek_locally
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open a browser and navigate to:
   ```
   http://localhost:8080
   ```

## API Endpoints

### Home Page
- **URL:** `/home` or `/`
- **Method:** GET
- **Description:** Renders the homepage (`index.html`).

### Job Description Generation
- **URL:** `/result`
- **Method:** POST, GET
- **Description:** Processes user input, validates the data, and generates a job description using the AI model.
- **Request Parameters (form data):**
  - `company`
  - `location`
  - `job-title`
  - `job-type`
  - `experience`
  - `skills`
  - `education`
- **Response:**
  - If successful: Renders `result.html` with the generated job description.
  - If an error occurs: Renders `error.html`.

## Code Explanation

### `main.py`
This file initializes the Flask application and defines the routes.
- The `/` and `/home` routes render the `index.html` template.
- The `/result` route handles job description generation by:
  1. Extracting form data.
  2. Validating data using `validateData()`.
  3. Calling `deepseek()` to generate the job description.
  4. Rendering the output or error page.

### `controller.py`
Contains helper functions for data validation and AI integration.
- `validateData(data)`: Checks if all required fields are non-empty.
- Calls `deepseek(data)` to process the job description.

### `ConnectAPI.py`
Contains AI-related functions.
- `deepseek(data)`: Uses Ollama to generate a job description based on the input fields.
- `extract_json_from_text(text)`: Extracts JSON from the AI response using regex.

## Expected AI Response Format
The AI returns job descriptions in JSON format with the following structure:
```json
{
    "Company name": "TCS",
    "Location": "Chennai,Coimbatore",
    "Experience": "5",
    "Type": "Full Time",
    "Post on": "12/12/2022",
    "Job Title": "AI Software Engineer",
    "Job Summary": "We are looking for an experienced AI Software Engineer...",
    "Key Responsibilities": [
        "Design and develop AI-powered applications...",
        "Implement and optimize RAG-based solutions..."
    ],
    "Required Skills & Qualifications": [
        "Bachelor's degree in Computer Science...",
        "Proficiency in Python, JavaScript, React..."
    ]
}
```

## Error Handling
- If JSON extraction fails, an error is logged.
- If the AI model fails, an error response with status `500` is returned.
- Missing input fields return a `400` status.

## Future Enhancements
- Add database support to store job descriptions.
- Improve frontend UI with better styling.
- Enhance validation checks with more robust error handling.

## License
This project is open-source and free to use under the MIT License.

