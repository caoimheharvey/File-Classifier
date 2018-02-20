import random
from textblob.classifiers import NaiveBayesClassifier
random.seed(1)

train = [
    ('I drink Lager.', 'food'),
    ('Beijing is a city', 'travel'),
    ('Hamburger is from Germany', 'food'),
    ('Drinks can be alcoholic', 'food'),
    ('Indonesia is a country', 'travel'),
    ('Singapore is in Malaysia', 'travel'),
    ('Sangria is a beverage', 'food'),
    ('Dublin is a city', 'travel'),
    ('Berlin is historic', 'travel'),
    ('Hamburg is in Germany', 'travel'),
    ('Pizza is amazing', 'food'),
    ('Delicious food can be found everywhere', 'food'),
    ('Spain has a lot of culture', 'travel')

]

test = [
    ('The beer was good.', 'food'),
    ('Hong Kong is nice', 'travel'),
    ("The meal was great", 'food'),
    ('I have been to Barcelona', 'travel'),
]

cl = NaiveBayesClassifier(train)

# Compute accuracy
accuracy = cl.accuracy(test)
print("Accuracy: {0}".format(accuracy))

# Show 5 most informative features
cl.show_informative_features(5)


