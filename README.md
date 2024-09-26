
# Simple Spam Filtering AI

## Overview
This is a Simple Spam Filtering AI project built using the Naive Bayes classifier. It classifies emails as either spam or ham (not spam) based on the email content. The project uses a dataset of email messages and implements text processing techniques to train a model that can identify spam emails.

Feel free to use the code if it helps you. It may not be the greatest project, but it's still useful for learning purposes. I will update it from time to time to improve its performance and add more features.

## Project Files
1. **simple-spam-filtering-ai.py**: The main Python file containing the code for training and testing the Naive Bayes spam filter.
2. **dataset**: A folder containing the dataset (`mail_data.csv`) used to train and test the model.

## Requirements
```
pandas
scikit-learn
python>=3.6
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run
1. Make sure you have Python 3.6 or later installed.
2. Install the necessary libraries:
   ```bash
   pip install pandas scikit-learn
   ```
3. Download the dataset folder and the simple-spam-filtering-ai.py file.
4. Run the script:
   ```bash
   python simple-spam-filtering-ai.py
   ```

## How it Works
1. The script reads the dataset from `mail_data.csv` containing email messages and their corresponding categories.
2. Email messages are transformed into numerical features using CountVectorizer.
3. A Naive Bayes classifier is trained on the dataset.
4. Input new email texts, and the trained model will predict whether they are spam or not.

## Future Updates
I plan to regularly update this project to improve accuracy, expand the dataset, and add new features.
