import nltk
from nltk.tokenize import sent_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Download NLTK data for sentence tokenization
nltk.download('punkt')

def summarize_text(text, num_sentences=3):
    """
    Summarizes the given text using the LSA (Latent Semantic Analysis) algorithm.
    
    :param text: The input article or book text.
    :param num_sentences: Number of sentences to return in the summary.
    :return: Summarized text.
    """
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

# Get user input
print("Enter/Paste your text and press Enter twice when done:")
user_text = []
while True:
    try:
        line = input()
        if line == "":
            break
        user_text.append(line)
    except EOFError:
        break

user_text = " ".join(user_text)

# Generate and display the summary
if user_text.strip():
    summary = summarize_text(user_text, num_sentences=3)
    print("\n=== Summary ===\n")
    print(summary)
else:
    print("No text entered. Please provide some content.")
