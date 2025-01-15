from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Input text
text = "The height of the building is 2 meters. Using the equation for free fall, the banana will take approximately 0.63 seconds to hit the ground, assuming no air resistance. The banana will be able to fall from the building in 0.632 seconds. The problem is a classic physics problem."

# Summarize with a max length of 75 characters
summary = summarizer(text, max_length=75, min_length=25, clean_up_tokenization_spaces=True)

# Print the summary
print(summary[0]['summary_text'])
