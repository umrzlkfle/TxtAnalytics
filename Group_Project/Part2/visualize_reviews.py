# visualize_reviews.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'processed-reviewsv2.csv'
df = pd.read_csv(file_path)

# Display basic info
print("Dataset Summary:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Visualization 1: Distribution of Review Ratings (if ratings exist)
if 'rating' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='rating', palette='viridis')
    plt.title("Distribution of Review Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("rating_distribution.png")
    plt.show()

# Visualization 2: Review Length Distribution
if 'review' in df.columns:
    df['review_length'] = df['review'].apply(len)
    plt.figure(figsize=(10, 5))
    sns.histplot(df['review_length'], bins=30, kde=True)
    plt.title("Review Length Distribution")
    plt.xlabel("Length of Review (characters)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("review_length_distribution.png")
    plt.show()

# Word Cloud (optional, if 'review' column exists)
try:
    from wordcloud import WordCloud

    if 'review' in df.columns:
        all_text = " ".join(df['review'].dropna())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title("Word Cloud of Reviews")
        plt.tight_layout()
        plt.savefig("wordcloud.png")
        plt.show()
except ImportError:
    print("wordcloud package not installed. Skipping word cloud generation.")

print("Visualizations completed.")
