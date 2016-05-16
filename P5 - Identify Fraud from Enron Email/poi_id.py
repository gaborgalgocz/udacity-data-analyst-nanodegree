#!/usr/bin/python

import sys
import pickle
import sklearn
sys.path.append("../tools/")

import pandas
import numpy

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data, test_classifier
from sklearn.feature_selection import SelectKBest

def select_k_best(data_dict, k):
#Helper function to perform SelectKBest scoring    
    full_feature_list = ['poi',
                         'bonus',
                         'deferral_payments',
                         'deferred_income',
                         'director_fees',
                         'exercised_stock_options',
                         'expenses',
                         'fraction_from_poi',
                         'fraction_to_poi',
                         'from_messages',
                         'from_poi_to_this_person',
                         'from_this_person_to_poi',
                         'loan_advances',
                         'long_term_incentive',
                         'other',
                         'restricted_stock',
                         'restricted_stock_deferred',
                         'salary',
                         'shared_receipt_with_poi',
                         'to_messages',
                         'total_payments',
                         'total_stock_value']

    data = featureFormat(data_dict, full_feature_list)
    labels, features = targetFeatureSplit(data)

    k_best = SelectKBest(k=k)
    k_best.fit(features, labels)
    scores = k_best.scores_
    unsorted_pairs = zip(full_feature_list[1:], scores)
    sorted_pairs = list(reversed(sorted(unsorted_pairs, key=lambda x: x[1])))
    print sorted_pairs
    
def calculate_fraction( numerator, denominator ):
### Helper function to calculate fractions for the new features
    fraction = 0.
    import math
    if math.isnan(float(denominator)) == False and math.isnan(float(numerator)) == False:
        fraction = float(numerator) / float(denominator)
    return fraction    
    
def scoring(estimator, features_test, labels_test):
#Helper function to evaluate final algorithm    
     labels_pred = estimator.predict(features_test)
     p = sklearn.metrics.precision_score(labels_test, labels_pred, average='binary')
     r = sklearn.metrics.recall_score(labels_test, labels_pred, average='binary')
     if p > 0.3 and r > 0.3:
            return sklearn.metrics.f1_score(labels_test, labels_pred, average='binary')
     return 0
                     
    
    
    
### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi',
'bonus',
'exercised_stock_options',
'expenses',
'fraction_from_poi',
'fraction_to_poi',
'from_poi_to_this_person',
'long_term_incentive',
'other',
'restricted_stock',
'salary',
'shared_receipt_with_poi',
'total_payments'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)
    
###Data exploration 
###Exploring the important characteristics of the dataset. To make it easier, 
###I converted the dictionary to a pandas dataframe.
    
df = pandas.DataFrame.from_records(list(data_dict.values()))
df.replace(to_replace='NaN', value=numpy.nan, inplace=True)
print df.shape
print "Number of POI:", df["poi"].sum()
print "Number of null values:" 
print df.isnull().sum()

### Task 2: Remove outliers
outliers = ['TOTAL', 'THE TRAVEL AGENCY IN THE PARK']
for outlier in outliers:
    data_dict.pop(outlier, 0)


### Task 3: Create new feature(s)

### Add new features
for i in data_dict:
    from_poi = data_dict[i]["from_poi_to_this_person"]
    to_messages = data_dict[i]["to_messages"]
    fraction_from_poi = calculate_fraction( from_poi, to_messages )
    data_dict[i]["fraction_from_poi"] = fraction_from_poi

    to_poi = data_dict[i]["from_this_person_to_poi"]
    from_messages = data_dict[i]["from_messages"]
    fraction_to_poi = calculate_fraction( to_poi, from_messages )
    data_dict[i]["fraction_to_poi"] = fraction_to_poi  
    
### Store to my_dataset for easy export below.
my_dataset = data_dict    
    
###Run SelectKBest feature selection
k = 21
best_features = select_k_best(my_dataset, k)    

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)


### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
#from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB()

#GaussianNB
from sklearn.naive_bayes import GaussianNB
gnb_clf = GaussianNB()
gnb_scores = sklearn.cross_validation.cross_val_score(gnb_clf, features, labels)
print "GaussianNB scores:", gnb_scores

#RandomForest
from sklearn.ensemble import RandomForestClassifier
rf_clf = RandomForestClassifier(n_estimators=25)
rf_scores = sklearn.cross_validation.cross_val_score(rf_clf, features, labels)
print "RandomForest scores:", rf_scores

#AdaBoost
from sklearn.ensemble import AdaBoostClassifier
ab_clf = AdaBoostClassifier(n_estimators=25)
ab_scores = sklearn.cross_validation.cross_val_score(ab_clf, features, labels)
print "AdaBoost scores:", ab_scores 

#Decision Tree
from sklearn import tree
dt_clf = tree.DecisionTreeClassifier(random_state=42, min_samples_split=12,max_depth=6, splitter='best')
dt_scores = sklearn.cross_validation.cross_val_score(dt_clf, features, labels)
print "Decision Tree scores:", dt_scores 



### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html


# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn import grid_search
cv = sklearn.cross_validation.StratifiedShuffleSplit(labels, n_iter=10)


from sklearn.tree import DecisionTreeClassifier
parameters = {'n_estimators' : [5, 10, 30, 40, 50, 100,150], 'learning_rate' : [0.1, 0.5, 1, 1.5, 2, 2.5], 'algorithm' : ('SAMME', 'SAMME.R')}
ada_clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=8))
adaclf = grid_search.GridSearchCV(ada_clf, parameters, scoring = scoring, cv = cv)
adaclf.fit(features, labels)

print adaclf.best_estimator_
print adaclf.best_score_

clf = adaclf.best_estimator_
test_classifier(clf, my_dataset, features_list)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)