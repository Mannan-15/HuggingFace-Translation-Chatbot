# Flask Multilingual Chatbot

This project is a simple, multilingual customer support chatbot built with Python, Flask, and the Hugging Face Transformers library. It serves predefined responses based on keywords and can translate these responses into several languages in real-time.

<img width="500" height="459" alt="image" src="https://github.com/user-attachments/assets/3dbccb0c-e487-4ec6-868f-2589c24c1cd2" />


## Features

-   **Rule-Based Logic**: Provides quick and consistent answers to common questions based on simple keyword matching.
-   **Powerful Multilingual Translation**: Utilizes the `facebook/m2m100_418M` model from Hugging Face to translate responses into 8 different languages, including Japanese, French, Spanish, and more.
-   **Flask API Backend**: Built with a lightweight Flask server that exposes a `/chat` endpoint to handle user interactions.
-   **Easily Extendable**: Simple to add new canned responses or support additional languages by updating the dictionaries in the code.

## Technologies Used

-   **Python 3.x**
-   **Flask**: For the web server and API endpoint.
-   **Hugging Face Transformers**: For accessing the pre-trained translation model via the `pipeline` API.
-   **PyTorch**: As the backend framework for the Transformers model.

## Project Workflow

1.  **User Request**: A user sends a message and their preferred language (e.g., 'French') to the `/chat` endpoint via a POST request.
2.  **Keyword Matching**: The Flask application searches the user's message for keywords (e.g., "pricing", "contact") to determine the appropriate predefined response in English.
3.  **Translation (If Needed)**: If the user's specified language is not English, the selected English response is passed to the M2M100 translation model.
4.  **JSON Response**: The final response, either in the original English or translated, is sent back to the user as a JSON object.

## Setup and Installation

Follow these steps to set up the project locally.

### 1. Clone the repository:
```bash
git clone [https://github.com//Mannan-15/HuggingFace-Translation-Chatbot.git](https://github.com/Mannan-15/HuggingFace-Translation-Chatbot.git)
cd HuggingFace-Translation-Chatbot
```

### 2. Create the Frontend File:
This project requires a basic HTML file for the user interface.
-   Create a folder named `templates`.
-   Inside the `templates` folder, create a file named `mlt.html`. This file should contain a simple chat interface with JavaScript to send requests to the `/chat` endpoint.

### 3. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 4. Install the required libraries:
```bash
pip install -r requirements.txt
```
*Note: The first time you run the app, the Transformers library will download the M2M100 model, which may take some time and require a good internet connection.*

## Usage

To run the chatbot application:

1.  Execute the Flask app script from your terminal:
    ```bash
    python app.py # Or whatever you name your main script
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:5000`.
3.  Use the chat interface you created in `mlt.html` to interact with the bot. Select a language and type a message containing keywords like "product" or "pricing".
