The question_generator.py script is a Python tool designed to generate multiple-choice questions from educational text using the Groq API. It leverages the Groq client, initialized with an API key stored in a .env file, to create quiz questions dynamically. The script includes a function, generate_questions_groq, which takes a text input and a desired number of questions (defaulting to 5) as parameters.

This function constructs a prompt instructing the Groq model (llama3-8b-8192) to generate multiple-choice questions, each with four answer options (A, B, C, D) and a clearly indicated correct answer. The prompt is built with moderate creativity (temperature=0.5) and a token limit of 2048 to ensure detailed responses. If the input text is empty, an error message is returned. Any issues during API interaction are caught and returned as error messages.

The script includes example usage, demonstrating question generation from a sample text about photosynthesis. When executed, it prints the educational content and the generated questions, making it a useful tool for educators or developers creating automated quiz systems from textual content.







1.9s
