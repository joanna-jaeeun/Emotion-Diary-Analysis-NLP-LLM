# NLP and LLM-based Analysis of Student Emotion Diaries

## Project Summary
The aim of this project is to analyze students' handwritten emotion diaries and provide personalized feedback based on the results.
Technically, the project focuses on NLP and LLM techniques, including sentiment analysis with BERT and prompt engineering to extract targeted insights.
Additionally, Neo4j and WeWeb were used to visualize outcomes, making the project more intuitive and engaging.
This project demonstrates how to derive insights from students’ writings and contributes to supporting children’s personal growth.

## Repository Contents
- **data** :
  - `Handwriting.pdf`: Example of original handwritten diary data
  - `Diary.csv` : Sample of dataframe containing 250 diary entries  
- **notebook**
  - `Analysis_of_Student_Emotion_Diaries.ipynb` : Notebook for analysis and modeling
- **assets** :


## Strategies flow
- **OCR and creating dataframe** : Using Google AI Studio, transform diaries into text datasets and create a dataframe with dataset information.
- **Personal data encryption** : To protect privacy, encrypt students' names by replacing them with nicknames.
- **Data analysis** : Using Neo4j (graph database system), analyze subtle changes in students' friendships and check their relationship status. Compare outcomes with n-gram structures in Neo4j.
- **Pseudo labeling** : For unlabeled datasets, apply the "sangrimlee/bert-base-multilingual-cased-nsmc" model with the emotion column, and correct mislabeled data.
- **Sentiment Analysis with BERT** : Perform sentiment analysis using both a pre-trained model and a fine-tuned model, then compare the results.
- **LLM** : Use GPT API with prompt engineering to extract sentiment scores and identify causes of emotions.
- **WeWeb** : Using WeWeb (no-code tool), build an emotional tracking calendar demo to visualize results.
  
## Key findings

### Shown friendship in studnets' diary with Neo4j

**Graph subjected to all diary**
- dfdfdf
![test](assets/Neo4jgraph1.png)


**Graph subjected to who write other studnets names**
- Customers in this cluster shop infrequently, as indicated by a longer **Average_Days_Between_Purchases**.
![graph2](assets/Neo4graph2.png)




### Pretrained Model vs Fine_tuned model

<div align="center">
  
| Cluster | Suggested Marketing Strategies |
|:-------:|:-------------------------------|
| **Cluster 0** | - Weekend-only promotions<br>- Casual browsing incentives (e.g., "Weekend Flash Sales")<br>- Loyalty rewards for consistent shoppers |
| **Cluster 1** | - Personalized luxury or premium product offers<br>- Special discounts after periods of inactivity<br>- Exclusive early-access events |
| **Cluster 2** | - Weekday-only discounts<br>- Bundling offers ("Buy more, save more")<br>- Reactivation campaigns to counteract decreasing trend |

</div>

## Conclusions

- User end : personalized shopping experiences based on their purchase behavior
- Business end : personalized shopping experiences based on their purchase behavior, identify high-value or at-risk customers to improve retention and engagement, Supports personalized promotions, leading to improved ROI and reduced marketing costs.
