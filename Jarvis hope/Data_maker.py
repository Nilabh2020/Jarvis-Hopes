import wikipedia
import json
import re
import time
import os

# Function to fetch a random Wikipedia article's content
def fetch_random_wikipedia_article():
    try:
        # Get a random article title and fetch its content
        topic = wikipedia.random()
        page = wikipedia.page(topic)
        content = page.content
        return topic, content
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error, multiple topics found: {e.options}")
        return None, None
    except wikipedia.exceptions.PageError:
        print(f"Error: Page does not exist.")
        return None, None

# Function to clean and extract the first few lines of an article
def extract_first_lines(article_content, num_lines=3):
    # Split article content into sentences
    sentences = re.split(r'(?<=[.!?]) +', article_content)
    # Take only the first `num_lines` sentences
    first_lines = ' '.join(sentences[:num_lines])
    # Clean the text from unnecessary symbols, line breaks, etc.
    clean_text = re.sub(r'\[\d+\]', '', first_lines)  # Remove reference numbers [1], [2], etc.
    clean_text = clean_text.replace('\n', ' ').strip()  # Remove new lines and excess spaces
    return clean_text

# Function to generate questions from the content
def generate_questions(article_content):
    # Extract the first 2-3 lines to form a basic question-answer set
    clean_content = extract_first_lines(article_content)

    question = f"What is the article about?"
    answer = clean_content
    return [{'question': question, 'answer': answer}]

# Function to create dataset from multiple random Wikipedia articles
def create_wikipedia_dataset():
    dataset = {}

    while True:  # Infinite loop
        print(f"Fetching a random article...")
        topic, article_content = fetch_random_wikipedia_article()

        if article_content:
            print(f"Generating questions for topic: {topic}")
            questions = generate_questions(article_content)
            dataset[topic] = questions

            # Save the dataset incrementally to avoid losing data
            save_dataset_to_json(dataset)
        else:
            print(f"Skipping invalid article...")

        # Delay between article fetches to prevent overwhelming Wikipedia's servers
        time.sleep(2)

# Function to save dataset to a JSON file (incrementally)
def save_dataset_to_json(dataset, file_name='predefined_data.json'):
    try:
        # Load existing dataset if it exists to append
        if os.path.exists(file_name):  # Using os.path to check file existence
            with open(file_name, 'r') as f:
                existing_data = json.load(f)
            existing_data.update(dataset)
        else:
            existing_data = dataset

        # Save the combined dataset
        with open(file_name, 'w') as f:
            json.dump(existing_data, f, indent=4)
        print(f"Dataset saved to {file_name}")
    except Exception as e:
        print(f"Error saving dataset: {e}")

# Main function to start the process
def main():
    create_wikipedia_dataset()

if __name__ == "__main__":
    main()
