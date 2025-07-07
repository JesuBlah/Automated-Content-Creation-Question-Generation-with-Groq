from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("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"))

def generate_questions_groq(text_content, num_questions=5):
    """
    Generates multiple-choice questions based on provided text using the Groq API.

    Args:
        text_content (str): Educational text for question generation.
        num_questions (int): Number of questions to generate.

    Returns:
        str: Generated questions or an error message.
    """
    if not text_content:
        return "Error: No text provided for question generation."

    prompt = f"""
    Based on the following educational content, generate {num_questions} multiple-choice questions.
    Each question should have four answer options (A, B, C, D) and clearly indicate the correct answer.

    Content:
    ---
    {text_content}
    ---

    Questions:
    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an expert at creating quiz questions from educational material."},
                {"role": "user", "content": prompt}
            ],
            model="llama3-8b-8192",  # Or larger Groq model if needed
            temperature=0.5,  # Moderate creativity
            max_tokens=2048,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error generating questions with Groq: {e}"

# Example usage
if __name__ == "__main__":
    educational_text = """
    Photosynthesis is a process used by plants, algae, and some bacteria to convert light energy into chemical energy.
    During photosynthesis, carbon dioxide and water are converted into glucose and oxygen using sunlight and chlorophyll.
    This process is essential for life on Earth as it provides oxygen and forms the basis of most food chains.
    """

    questions = generate_questions_groq(educational_text, num_questions=3)
    print("--- Educational Content ---")
    print(educational_text)
    print("\n--- Generated Questions ---")
    print(questions)
