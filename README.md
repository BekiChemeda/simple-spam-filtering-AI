# simple-spam-filtering-AI
This is a simple Spam Filter AI I built while practicing Naive Bayes. It classifies emails as spam or not (ham) using basic machine learning techniques. If you think it will help, feel free to use the code. I'll also be updating it from time to time to improve its functionality and performance, so stay tuned for more features!


Feel free to use the code if it helps you. It may not be the greatest project, but it's still useful for learning purposes. I will update it from time to time to improve its performance and add more features.

# Project Files
simple-spam-filtering-ai.py: The main Python file containing the code for training and testing the Naive Bayes spam filter.
dataset: A folder containing the dataset (mail_data.csv) used to train and test the model.

Requirements
bash
  pandas
  scikit-learn
  python>=3.6
Install dependencies:

pip install -r requirements.txt
How to Run
Make sure you have Python 3.6 or later installed.
Install the necessary libraries:
pip install pandas scikit-learn
Download the dataset folder and the simple-spam-filtering-ai.py file.
Run the script:
python simple-spam-filtering-ai.py
How it Works
The script reads the dataset from mail_data.csv containing email messages and their corresponding categories.
Email messages are transformed into numerical features using CountVectorizer.
A Naive Bayes classifier is trained on the dataset.
Input new email texts, and the trained model will predict whether they are spam or not.
Future Updates
I plan to regularly update this project to improve accuracy, expand the dataset, and add new features.
