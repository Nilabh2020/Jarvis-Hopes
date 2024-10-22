import wikipedia

def get_wikipedia_answer(question):
    try:
        # Get a brief summary from Wikipedia
        summary = wikipedia.summary(question, sentences=1)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query was too broad. Did you mean: {', '.join(e.options[:3])}?"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that."
    except Exception as e:
        return f"An error occurred: {str(e)}"
