# UK Forest-Health

![feat-1800x0-c-center copy](https://user-images.githubusercontent.com/83399849/133164186-3d6b673a-6474-45d5-87b7-9b8ad1757fd8.png)





## Overview

This project was completed as part of the Data Science Immersive course at General Assembly. The topic of UK Forest condition was selected, because of personal interest within Life Sciences.


## Goals of the project


There is an urgent need to develop a predictive understanding of the carbon and ecological dynamics of forests . Forests hold approximately two thirds of terrestrial biodiversity and half of terrestrial carbon, but we currently know little about how the biology and demography of trees lead to regional and global patterns in the biomass, structure, and species composition of forests. This problem limits our ability to predict how quickly forests might respond to climate change.

The project goal was to find out how the environmental factors affect tree health.

The purpose of the work presented here was to develop a simple model that would assess tree condition and find out whether the model can predict the dynamics of real forest communities.



## Data collection 

The forest condition report data came from the UK Government website, which included information on five tree species: Sitka Spruce, Norway Spruce, Scots Pine, Beech and Oak, located in various monitoring plots across England, Scotland and Wales. Depending on the species, it included between 29 and 33 features indicative of condition and scored for each tree. The air pollution data also came from the UK Government website and consisted of information on levels of Sulphur dioxide, Volatile organic compound, Nitrous oxide, Ammonia, Particle pollution compounds with diameters below 2.5 and 10 µm (pm25, pm10).
The annual mean temperature and annual rainfall data came from the Met Office UK website. 

![trees](https://user-images.githubusercontent.com/83399849/133161397-2ccaa59d-3ee2-4a4d-b696-51c9b740805d.png)



## Data cleaning 


The data collected was in a csv and txt format. Files in txt format have been converted to csv format using csv writer. 
The raw data consisted of almost 190,000 observations and 107 features for years 1987 - 2006. A lot of the features contained mostly missing values, therefore these were dropped. Some of the categorical features applied only to specific species , therefore, in order to retain as much data as possible new classes within each feature were imputed. The new class was referenced in the data dictionary as: ‘not applicable within this species’. 
The final dataset after cleaning includes: forest data with 63 features for almost 47,000 trees for years 1995 - 2006. 



## Feature engineering

After initial exploratory data analysis, I calculated some fields such as:
  1. Age.
  2. Local crown density mean for each tree species.
  3. Crown mean class - binary class.
  4. Longitude and Latitude using grid reference column and geopandas. 
  5. Location address using reverse coding and geopy.
  6. Extracting country from the address list.

## EDA

Exploratory Data Analysis showed the majority of the trees were healthy and not much environmental damage took place. However looking at the outliers indicated some of the trees are indeed affected and deteriorating. 



## Target variable: Crown Density class

![image](https://user-images.githubusercontent.com/83399849/154490533-183cd5e1-747f-41bc-bdb3-5cee455988a9.png)

![lcdoutliers](https://user-images.githubusercontent.com/83399849/133161818-c140ff67-673c-4a9c-a56c-f2aba52344b2.png)

![Dashboard 1](https://user-images.githubusercontent.com/83399849/135732511-0142f028-5319-431e-af98-313b1b8f70eb.png)


## Modeling 

Baseline accuracy: 0.621

SMOTE oversampling was used to deal with class imbalance (since Crown density class distibution was imbalanced).

### Classification models



A range of models were applied on the dataset, using three sets of the predictors. Most of the predictors were categorical, however there were few continuous variables. All variables have been standardised with Standard scaler before running the models Various different models were used including Logistic Regression, K Nearest Neighbours, Random Forest Classifier, Decision Tree Classifier and Extra Tree Classifier.

The best model was the Logistic Regression model (using oversampling with SMOTE), using second set of the predictors, that included the following:

diameter, height, shoot death branch, defoliation type, broadleaf dieback type, leaf browning, leaf yellowing, broadleaf dieback extend percentage, overall discolouration,damage butt stem, damage game, damage insect, damage fungal, damage abiotic, damage man, damage fire, damage other, ammonia, nitrous oxide, sulphur dioxide, volatile organic compound, particular matter 10, particualr matter 25, annual mean temp,annual rainfall, age, latitude.

The final model score was 0.69, which was above the baseline score. All the models attempted gave final scores between 0.64 and 0.73 - Decision Tree classifier yielded the worst model scores.



![image](https://user-images.githubusercontent.com/83399849/154522255-51fbe581-f057-4b25-bec2-65bbe6360c3d.png)



The best model was validated with Precision-Recall curve, receiver operating characteristic curve (ROC), confusion matrix and classification report. 



### Natural Language Processing 


Comments variable was used as a predictor in this modeling, in order to try to predict tree health. Count Vectoriser followed by Logistic Regression and Random Forest Classifier. 

The best model was Random Forest Classifier and final model score was 0.65, which was above the bassline score.


Feature importance from the NLP identified the following comments as indicative of tree deterioration:
Omd - old mechanical damage, chin - chewing insect, dead, wm - winter moth, loph - low pH.

As with the previous modeling NLP model was validated with Precision-Recall curve, receiver operating characteristic curve (ROC), confusion matrix and classification report.

<img width="522" alt="Screenshot 2021-08-11 at 01 32 05" src="https://user-images.githubusercontent.com/83399849/133163547-5bd3c2dc-6b96-4bfc-895a-ad7e5a77e192.png">






## Conclusions 

Dieback in broadleaves, shoot death branch, damage insect, particualr matter compounds, defoliation, discolouration, temperature are among the strongest indicators of local crown density reduction.
Trees with high defoliation rate and leaves/needles discolouration are most likely to be classed as deteriorating.
Local crown density reduced over the years across all of the tree species. Sitka Spruce, Beech and Oak affected the most.

## Limitations

* Air pollution data available for the UK as a whole rather than individual location.
* No forest condition records published since 2006.

## Key learning

Throughout this project I was able to learn a lot about a variety of Classification and NLP processes and how they can be applied. My greatest achievement was my determination and ability to find solutions when it at times felt impossible. Dealing with a blocker until I found a workable solution strengthened my critical thinking and problem solving skills.


## Challenges

Data cleaning after merging multiple files proved to be challenging as it created a lot of unnecessary null values and duplicates that had to be carefully cleaned. 
Installing geopy was quite prolonged and initially was not successful. However few approaches were used and installing additional Python libraries beforehand helped resolve the issue.



## Future work

* Perform the analysis based on more localised air pollution data.
* Add soil data.
* Obtain carbon emission data as well as water pollution data.
* Look at the localised animal composition.

## Libraries Used

* Pandas.
* NumPy.
* NLTK.
* Scikit-learn.
* Matplotlib.
* Seaborn.
* Geopandas.
* Geopy.
