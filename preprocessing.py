import re
import config

def discretize(rating):
    """
    This function takes in a rating and based on the following scheme
    it puts it into 3 bins:
    1-2-3: Needs Improvement
    4: Good
    5: Amazing
    """
    if rating<=3:
        rating='Needs Improvement'
    elif rating==4:
        rating='Good'
    elif rating==5:
        rating='Amazing'
    return rating


def remove_patterns(review, regex='\d+'):
    """
    Given a review remove patterns which are unnecessary and do not add meaning to the review.
    """
    review = re.sub(regex, ' ', str(review))
    review = re.sub(' +', ' ', str(review))
    review = review.lstrip().rstrip()

    review = review.lower()

    return review


def clean_data(dataframe, cols=['Review', 'Rating']):
    """
    Take in the dataframe remove unneded patterns by applying remove_patterns on the review column and return the dataframe.
    """
    dataframe_2 = dataframe.copy()
    
    for col in cols:
        if col == 'Review':
            dataframe_2[col] = dataframe_2[col].apply(remove_patterns, regex=config.REGEX)
        if col == 'Rating':
            dataframe_2[col] = dataframe_2[col].apply(discretize)
    
    return dataframe_2