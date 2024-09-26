
# Simple Spam Filtering AI

## Overview
This is a Simple Spam Filtering AI project built using the Naive Bayes classifier. It classifies emails as either spam or ham (not spam) based on the email content. The project uses a dataset of email messages and implements text processing techniques to train a model that can identify spam emails.

Feel free to use the code if it helps you. It may not be the greatest project, but it's still useful for learning purposes. I will update it from time to time to improve its performance and add more features.

## Project Files
1. **simple-spam-filtering-ai.py**: The main Python file containing the code for training and testing the Naive Bayes spam filter.
2. **dataset**: A file containing the dataset (`mail_data.csv`) used to train and test the model.

## Requirements
```
pandas
scikit-learn
python>=3.6
```

## Steps to Run

1. **Ensure Python is Installed**: 
   - Make sure you have Python 3.6 or later installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: 
   - Open your terminal or command prompt and run the following command to clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-spam-filtering-ai.git
   ```
   - Replace `yourusername` with your actual GitHub username if necessary.

3. **Navigate to the Project Directory**: 
   - Change to the directory where the project was cloned:
   ```bash
   cd simple-spam-filtering-ai
   ```

4. **Install the Required Libraries**: 
   - Install the necessary libraries using pip. If you have a `requirements.txt` file, run:
   ```bash
   pip install -r requirements.txt
   ```
   - If there is no `requirements.txt` file, you can manually install the libraries:
   ```bash
   pip install pandas scikit-learn
   ```

5. **Run the Script**: 
   - Execute the main Python script to start the spam filter:
   ```bash
   python simple-spam-filtering-ai.py
   ```

6. **Input Emails for Classification**: 
   - After running the script, you can input email text to check if it is spam or ham. The program will continuously prompt you for input until you exit by pressing **Ctrl + C**.

## How it Works
1. The script reads the dataset from `mail_data.csv`, containing email messages and their corresponding categories.
2. Email messages are transformed into numerical features using CountVectorizer.
3. A Naive Bayes classifier is trained on the dataset.
4. Input new email texts, and the trained model will predict whether they are spam or not.

## Future Updates
I plan to regularly update this project to improve accuracy, expand the dataset, and add new features.
