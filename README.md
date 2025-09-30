# NLP and LLM-based Analysis of Student Emotion Diaries

## Project Summary
The aim of this project is to analyze students' handwritten emotion diaries and provide personalized feedback based on the results.
Technically, the project focuses on NLP and LLM techniques, including sentiment analysis with BERT and prompt engineering to extract targeted insights.
Additionally, Neo4j and WeWeb were used to visualize outcomes, making the project more intuitive and engaging.
This project demonstrates how to derive insights from students’ writings and contributes to supporting children’s personal growth.

## Repository Contents
- **data** :
  - `Handwriting.pdf`: Handwritten diary data form
  - `Diary.csv` : Sample of dataframe containing around 250 diary entries  
- **notebook**
  - `Analysis_of_Student_Emotion_Diaries.ipynb` : Notebook for analysis and modeling
- **deployment**:
   - `emotion_calendar.py`: Generates the emotion calendar
   - `emotion_graph.py`: Generates the emotion graph

  
## Strategies flow
- **OCR and creating dataframe** : Using Google AI Studio, transform diaries into text datasets and create a dataframe with dataset information.
- **Personal data encryption** : To protect privacy, encrypt students' names by replacing them with nicknames.
- **Data analysis** : Using Neo4j (graph database system), analyze subtle changes in students' friendships and check their relationship status. Compare outcomes with n-gram structures in Neo4j.
- **Pseudo labeling** : For unlabeled datasets, apply the "sangrimlee/bert-base-multilingual-cased-nsmc" model with the emotion column, and correct mislabeled data.
- **Sentiment Analysis with BERT** : Perform sentiment analysis using both a pre-trained model and a fine-tuned model ("beomi/KcELECTRA-base"), then compare the results.
  | Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row1 Val1| Row1 Val2| Row1 Val3|
| Row2 Val1| Row2 Val2| Row2 Val3|
- **LLM** : Use GPT API with prompt engineering to extract sentiment scores and identify causes of emotions.
- **Streamlit** : Using Streamlit, build an emotional tracking calendar and graph demo to visualize results.
