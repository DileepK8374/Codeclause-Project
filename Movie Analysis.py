import pandas as pd
import matplotlib.pyplot as plt


movie_data = pd.read_csv('movie_dataset.csv')


ratings_mean = movie_data['Rating'].mean()
ratings_median = movie_data['Rating'].median()
ratings_std = movie_data['Rating'].std()

print(f"Mean rating: {ratings_mean:.2f}")
print(f"Median rating: {ratings_median:.2f}")
print(f"Standard deviation of ratings: {ratings_std:.2f}")


plt.hist(movie_data['Rating'], bins=10, edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Distribution of Movie Ratings')
plt.show()

from textblob import TextBlob

review = "This movie was amazing! I loved every minute of it."
blob = TextBlob(review)
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

print(f"Review: {review}")
print(f"Polarity: {polarity:.2f}")
print(f"Subjectivity: {subjectivity:.2f}")
