# Udacity - Data Analyst nanodegree - Project submission
### P5: Machine Learning 
&nbsp;

## 1. Introduction

### Goal of the project
The goal of the project is to use machine learning methods to identify 'persons of interest' within the Enron dataset. 

### Data exploration

First, let's take a look at the dataset.

By converting the dictionary to a pandas dataframe, we can easily investigate the structure of the dataset. The dataset contains data about 146 individuals, across 21 features. Among the 146 individuals, 18 are flagged as "poi", person of interest. 

##### Features with many missing values?  
Now we will continue exploring the pandas dataframe, focusing on the important question of missing data. The features which have missing data in more than half of the cases should not be considered at the feature selection step. 


### Outlier investigation
In Lesson 7 we were investigating the outliers within the dataset and we wrote our code in outliers.py to visualize the datapoints using matplotlib. The scatterplot revealed that TOTAL was a clear outlier. The scatterplot did not reveal other clear outliers. However, by looking at the names in the dataset, it is clear that 'The travel agency in the park' needs to be removed too, since it is not a person. 


## 2. Feature selection

### Create new features	
I created two new features, 'fraction_to_poi' and 'fraction_from_poi', which are calculated as a fraction of emails to and from POI, relative to the total number of to and from emails. 

### Select features
To select the features we will use later, I ran the SelectKBest feature selection, and I sorted the scores and printed the results:


```
('exercised_stock_options', 24.815079733218194), 
('total_stock_value', 24.182898678566879), 
('bonus', 20.792252047181535), 
('salary', 18.289684043404513), 
('fraction_to_poi', 16.409712548035799), 
('deferred_income', 11.458476579280369), 
('long_term_incentive', 9.9221860131898225), 
('restricted_stock', 9.2128106219771002), 
('total_payments', 8.7727777300916792), 
('shared_receipt_with_poi', 8.589420731682381), 
('loan_advances', 7.1840556582887247), 
('expenses', 6.0941733106389453), 
('from_poi_to_this_person', 5.2434497133749582), 
('other', 4.1874775069953749), 
('fraction_from_poi', 3.1280917481567374), 
('from_this_person_to_poi', 2.3826121082276739), 
('director_fees', 2.1263278020077054), 
('to_messages', 1.6463411294420076), 
('deferral_payments', 0.22461127473600989), 
('from_messages', 0.16970094762175533), 
('restricted_stock_deferred', 0.065499652909942141)
```

I used both the result of the SelectKBest together and the result of the data exploration (to find features with many null values) to decide on the final list of features. If a feature was scored as relevant by SelectKBest, but had too many null values (for example 'deferred income' and 'loan advances') I decided to not use it. I included the top 10 features selected by SelectKBest. 

Why 10 features? I looked at the scores of the features, and I saw that some features have considerably higher scores, while others seemed to be completely irrelevant. There was no clear separation between high scores and low scores, so I decided to try using approximately half of the features, so I went with 10 to check the outcome. At a later step I wanted to improve the performance of the algorithm, so I added more features. In the final feature list I used 12 features.  


## 3. Pick and tune an algorithm

I did not use feature scaling, as none of the algorithms tried requires it. AdaBoost only requires feature scaling when using using regressions, but currently this is not the case. 

### Pick an algorithm

I used SKlearn's cross validation to pick an algorithm. I tested 4 algorithms:   
GaussianNB  
Random Forest  
AdaBoost  
Decision Tree  

I decided to go with Random Forest, since it performed the best with the cross validation. 
		

### Tune the algorithm

The machine learning algorithms have several input parameters that influence the performance of the algorithm. By trying to run the algorithm with different values for the parameters, we can optimize the performance. It is important to keep in mind that the optimal parameters for one dataset are most likely to have inferior performance on others. We also have to make sure that we are not overfitting the algorithm on the test dataset. Trying out several parameter combinations manually is time-consuming, that's why I preferred to choose GridSearchCV, which runs the algorithm with many parameter combinations that I enter as a range. It will then evaluate the outcomes and will  return the best performing parameter combination. 

I used GridSearchCV to tune the Random Forest algorithm. The best score achieved is 0.53. 

## 4. Validation and evaluation

### Validation	
Validation means to see if the algorithm generalizes well, if it performs well on new datasets. A classic mistake is to train and test on the same dataset. This leads to high accuracy on the given dataset, but will have poor results on new data. This is called overfitting. 

I used StratifiedShuffleSplit to validate my analysis, which is splitting the dataset to training and testing data and then iterates it n times (creating so-called folds). 

### Algorithm performance

Using accuracy to evaluate the performance of the algorithm is not the most useful metric, since we have so little POI. For example if all individuals were marked as non-POI, we'd still have a high accuracy. More useful are two other metrics, precision and recall. In this example, precision means the probability that - given the algorithm identifies someone as POI, - the individual is indeed POI. 

Recall in this example means the probability of identifying a person as POI, given that they are really POI.

I'd say we should aim for high recall here, this means that the algorithm will flag a high number of real POIs as such, even if some non-POIs will get flagged (which means lower precision).

I tested the performance of Random Forest on the dataset. Precision was above 0.3, but recall was just 0.18. I decided to try another algorithm. 

When I tested the algorithms with cross validation, the second best performing was AdaBoost, so I gave it a try. Precision was again above 0.3, but recall was 0.28. This was very close to the required 0.3 so I decided not to try another algorithm, but rather to try to fine tune it more. 

I decided to use more features. Originally I chose to use 10 features (and 'poi' of course). Now I checked the feature scoring done by SelectKBest and decided to add 2 more, which ranked high and didn't have many null values: 'other', and 'fraction from poi' - this latter one was one of the new features that I added. With the addition of two extra features I managed to fine tune the algorith to achieve a precision of 0.35 and a recall of 0.34 - success!

### Conclusion

I found it very useful to experience that the first attempts to pick an algorith were unsuccessful, and even the second attempt needed some fine tuning to achieve the required result. This helped me practice with real world data and I gathered very useful insight on how algorithms work in a real world setting. 

