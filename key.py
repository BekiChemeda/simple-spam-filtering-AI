import time
from time import sleep

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


df = pd.read_csv('mail_data.csv')
df.fillna('', inplace=True)
df['Category'] = df['Category'].map({'spam': 0, 'ham': 1})

# print("Initial Data Sample:")
# print(df.head())

X = df['Message']
y = df['Category']

# print("\nFeatures (Messages) and Labels (Spam/Ham):")
# print(X.head())
# print(y.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print("\nNumber of training samples:", len(X_train))
# print("Number of testing samples:", len(X_test))

vectorizer = CountVectorizer(stop_words='english', lowercase=True)
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# print("\nTransformed Training Data Shape:", X_train_counts.shape)
# print("Transformed Testing Data Shape:", X_test_counts.shape)


nb_model = MultinomialNB()
nb_model.fit(X_train_counts, y_train)

train_predictions = nb_model.predict(X_train_counts)
test_predictions = nb_model.predict(X_test_counts)

train_accuracy = accuracy_score(y_train, train_predictions)
test_accuracy = accuracy_score(y_test, test_predictions)

# print(f"Testing Accuracy: {test_accuracy}\n")

print("Setting Up...")
time.sleep(3)
print("*************************")
while True:
    try:
        input_email = input("-----------------------------\nEnter text to be checked if it's spam or ham: \n ->")
        input_count =vectorizer.transform([input_email])
        prediction = nb_model.predict(input_count)
        print(f"Checking If below text spam or not \n ******************************* \n {input_email} \n -*******************************"
              )
        time.sleep(2)
        if prediction == 0:
            print(f"Above Text is spam")

        else:
            print(f"Above text is not Spam")

    except KeyboardInterrupt:
        print("I am Interrupted by Keyboard(CTRL + C) Bye Bye ")
        break