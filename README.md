# Ask Your CSV using LangChain

This repository contains a Streamlit app that allows users to upload a CSV file and ask questions related to the data in the file. The app utilizes the Langchain framework and the OpenAI language model to provide informative responses based on the uploaded CSV data.

## Getting Started

To get started with the Ask Your CSV app, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/ask-your-csv.git
   ```

2. Install the required dependencies. It is recommended to use a virtual environment:

   ```
   cd ask-your-csv
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate  # For Windows
   pip install -r requirements.txt
   ```

3. Run the app:

   ```
   streamlit run app.py
   ```

4. Open your web browser and navigate to `http://localhost:8501` to access the app.

## Usage

1. Upload a CSV file by clicking on the "Upload your csv" button and selecting a CSV file from your local machine.

2. Once the file is uploaded, you can enter your question in the text input field labeled "Ask a question."

3. Press Enter or click outside the input field to submit your question.

4. The app will process your question using the Langchain framework and the OpenAI language model. The generated response will be displayed on the app interface.

5. You can ask additional questions by entering them in the input field and submitting them. The app will provide responses based on the data in the uploaded CSV file.

## Frameworks and Libraries Used

- Streamlit: The app is built using the Streamlit framework, which allows for easy creation of interactive web applications in Python.

- Langchain: Langchain is a Python library that provides a framework for working with language models and processing natural language. It is used in this app to create an agent that can interact with the CSV file and generate responses to user questions.

- OpenAI: OpenAI is a language model used by the Langchain framework. In this app, the OpenAI language model is utilized to process user questions and provide informative responses based on the uploaded CSV data.

- dotenv: The dotenv library is used to load environment variables from a .env file. It is used in this app to load any required environment variables.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them.

4. Push your changes to your fork.

5. Submit a pull request with a description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

- This app was created using the Langchain framework, which provides a powerful and flexible way to work with language models and process natural language tasks.

- The OpenAI language model was utilized to generate informative responses based on the uploaded CSV data.

- Streamlit made it easy to create the user interface for this app and quickly iterate on the development process.
