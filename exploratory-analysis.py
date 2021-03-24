import pandas as pd
import numpy as np
from preprocessing import clean_data
import config
import matplotlib.pyplot as plt

reviews = pd.read_csv(config.PATH_DATA)


ratings_distribution = reviews[['Rating']].value_counts()

#plot of distribution of ratings
labels = ratings_distribution.index.get_level_values(0).values
distribution = ratings_distribution.values

x = np.arange(len(labels))
width = 0.35


fig, ax = plt.subplots(figsize=(12,6))
rect = ax.bar(x-width/2, distribution, width, label='Ratings Count', color='#008891')

# Add text for labels, title and custom x-axis tick labels
ax.set_ylabel('Count')
ax.set_xlabel('Ratings')
ax.set_title('Rating Distribution')
ax.set_xticks(x-0.18)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rect)
fig.savefig('plots/Ratings-Distribution.png', facecolor='w')
fig.tight_layout()
plt.show()
##############################################################################
reviews = clean_data(reviews)
discrete_ratings_distribution = reviews[['Rating']].value_counts()

#plot of distribution of ratings
labels = discrete_ratings_distribution.index.get_level_values(0).values
distribution = discrete_ratings_distribution.values

x = np.arange(len(labels))
width = 0.35


fig, ax = plt.subplots(figsize=(12,6))
rect = ax.bar(x-width/2, distribution, width, label='Ratings Count', color='#008891')

# Add text for labels, title and custom x-axis tick labels
ax.set_ylabel('Count')
ax.set_xlabel('Binned Ratings')
ax.set_title('Discrete Rating Distribution')
ax.set_xticks(x-0.18)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rect)
fig.savefig('plots/Binned-Ratings-Distribution.png', facecolor='w')
fig.tight_layout()
plt.show()