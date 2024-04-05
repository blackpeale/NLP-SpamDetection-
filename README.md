# NLP Message Classifier: A Spam Detection Application

This project aims to develop a spam detection application using Natural Language Processing (NLP) techniques and Support Vector Classification (SVC). The application is designed to accurately classify messages as either spam or non-spam (ham), thereby enhancing inbox security and improving the overall digital experience of users.

## Project Overview

Spam messages have become a significant nuisance and security threat in today's digital age. To combat this issue, this project utilizes NLP techniques combined with SVC to develop an efficient message classifier. The classifier is trained on a dataset containing labeled examples of spam and ham messages.

## Dataset

The dataset used for this project consists of two columns: 'category' and 'message'. The 'category' column indicates whether a message is spam or ham, while the 'message' column contains the text of the messages. This dataset serves as the foundation for training and evaluating the classifier model.

## Model Training

The steps taken to achieve an optimal solution of predicting message profitability at a 99% accuracy include:

1. **Data Preprocessing**: The raw text data is preprocessed to remove noise and standardize the text format. This includes tasks such as tokenization, lowercasing, and removing stop words.

2. **Feature Extraction**: Relevant features are extracted from the text data to represent messages numerically. This typically involves techniques like TF-IDF vectorization to convert text into a format suitable for machine learning algorithms.

3. **Model Selection**: Support Vector Classification (SVC) is chosen as the primary model due to its effectiveness in handling high-dimensional data and its ability to handle non-linear decision boundaries.

4. **Model Training**: The SVC model is trained on the preprocessed dataset, optimizing parameters to achieve the highest accuracy possible.

## Model Deployment

The trained SVC model is deployed using Streamlit, a Python library for building interactive web applications. The deployment is hosted on Streamlit Share and can be accessed at [Spam Detection App](https://spamtextnlp-project.streamlit.app/). Users can input messages into the application, and the model will classify them as spam or ham in real-time.

## Conclusion

By leveraging NLP techniques and SVC, this project delivers a robust spam detection solution with high accuracy. The deployed application provides users with a valuable tool for enhancing inbox security and improving their digital experience. Future enhancements may include incorporating additional features and exploring advanced machine learning algorithms to further improve accuracy and performance.
