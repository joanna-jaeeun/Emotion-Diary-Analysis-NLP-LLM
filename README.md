# Sentiment Analaysis with Emotion Diary

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
  - `Sentiment_Analysis.ipynb` : Notebook for analysis and modeling
- **assets** :


## Strategies flow
- **ORC and creating dataframe** : Using Google AI Studio, transform diaries into text datasets and create a dataframe with dataset information.
- **Personal data encryption** : To protect privacy, encrypt students' names by replacing them with nicknames.
- **Data analysis** : Using Neo4j (graph database system), analyze subtle changes in students' friendships and check their relationship status. Compare outcomes with n-gram structures in Neo4j.
- **Pseudo labeling** : For unlabeled datasets, apply the "sangrimlee/bert-base-multilingual-cased-nsmc" model with the emotion column, and correct mislabeled data.
- **Sentiment Analysis with BERT** : Perform sentiment analysis using both a pre-trained model and a fine-tuned model, then compare the results.
- **LLM** : Use GPT API with prompt engineering to extract sentiment scores and identify causes of emotions.
- **WeWeb** : Using WeWeb (no-code tool), build an emotional tracking calendar demo to visualize results.
  
## Key findings
### Customer Profiles Derived from Radar Chart Analysis

![test](assets/Radarchart.png)
**Cluster 0: Casual Weekend Shoppers**
- Customers in this cluster usually shop less frequently and spend less money compared to other clusters.
- They generally have a smaller number of transactions and purchase fewer products.
- They prefer shopping during weekends, possibly engaging in casual or window shopping.
- Their spending habits are quite stable over time, showing little fluctuation in their monthly spending.
  
**Cluster 1: Occasional Big Spenders**
- Customers in this cluster shop infrequently, as indicated by a longer **Average_Days_Between_Purchases**.
- Their spending has been increasing, suggesting a growing interest or investment in their purchases.
- They tend to have high monthly spending with a large standard deviation, indicating variability in spending within the group.
- Their **Average_Transaction_Value** is high compared to other clusters.

**Cluster 2: Frequent Big Spenders**
- Customers in this cluster shop frequently, with a high total purchase volume and number of transactions.
- Although they shop often, they tend to spend less per transaction, buying a variety of products.
- They prefer shopping on weekdays.
- Their spending trend is decreasing, which might signal a future change in their shopping habits.

### Marketing strategies

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
