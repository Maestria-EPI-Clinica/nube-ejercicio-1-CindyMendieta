import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def generate_word_cloud_from_csv(csv_path, text_column):
    """
    Loads a CSV file, extracts text from a specified column, and generates a word cloud.

    Args:
        csv_path (str): The path to the CSV file.
        text_column (str): The name of the column containing the text data.
    """
    try:
        df = pd.read_csv(csv_path,sep=";")

        if text_column not in df.columns:
            print(f"Error: Column '{text_column}' not found in the CSV file.")
            return

        # Combine all text from the specified column into a single string
        text = " ".join(df[text_column].astype(str).tolist())

        # Create a set of stopwords
        stopwords = set(STOPWORDS)

        # Add Spanish articles to the stopwords
        spanish_articles = {"el", "de", "se", "para", "en", "la", "los", "las", "un", "una", "unos", "unas"}
        stopwords.update(spanish_articles)


        # Generate the word cloud
        wordcloud = WordCloud(width = 800, height = 800,
                              background_color ='white',
                              stopwords = stopwords,
                              min_font_size = 10).generate(text)

        # display the word cloud
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)

        plt.show()

    except FileNotFoundError:
        print(f"Error: CSV file not found at '{csv_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")
