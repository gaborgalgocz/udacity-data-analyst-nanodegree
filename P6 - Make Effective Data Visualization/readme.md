# Data visualization

## Summary
The project explores the widely known Titanic dataset, which contains data from all the passengers on board the Titanic. On Kaggle's site the dataset is a base of a machine learning competition, with more than 4000 entries, but in general many online resources use it to demonstrate data analysis techniques and machine learning algorithms. The file contains 891 entries across 12 variables. My task was to use data visualization techniques to tell the story of the tragedy, so the people who would look at it would gain insight on the differences between the probability of survival across many factors.

#### Notes on the dataset
Titanic had approximately 2224 passengers and crew on board on its first and final journey. The Kaggle dataset has entries only about the passengers, and it is split into train and test datasets for the purposes of running machine learning algorithms on them to predict the probability of survival. This means that the "Survived" column is only present in the train dataset, with 891 entries. This means that the visualizations that I will present contain data of only a fraction of the people on board. I have found a very insightful infographic which describes the survival rate of all the passengers and crew on Wikipedia:
https://upload.wikimedia.org/wikipedia/commons/6/69/Titanic_casualties.svg

## Design
I used Python and Pandas to import, clean and explore the dataset. In my submission I've included the iPython notebook with all the code that I used. Approximately 20 percent of the entries didn't have data on the age of the passenger, so I chose to remove those rows. I compared the distribution of ages of the full dataset and the new dataset with the removed rows and I saw no significant differences between the two, so I concluded that the missing values were appearing randomly and there was no pattern behind them (for example missing data only for children).

I was interested in three variables, age, gender and passenger class, I wanted to see how they were affecting the probability of survival. I thought the best way to visualize them is to create three bar charts with them, grouping all passengers along the three variables. 


## Feedback
### Feedback round #1
I asked for feedback at an early stage, so I can incorporate the comments quickly. ("Rapid prototyping") I knew that the labels on the first chart were not readable, but I wanted feedback on the idea. The feedback was that even with the labels fixed, there would too many bars, so that needed to be grouped.

### Feedback round #2
With the ages grouped, it looked much cleaner. The second feedback round revealed that the charts are boring, just one color, and the use of three charts to tell one story is not a good direction. The reviewer mentioned that the charts are too abstract, they don't tell a story.

### Feedback round #3
To remove abstraction from my visualization, and to increase the compactness, I tried to communicate the whole story with one single chart. I changed Survival rate to Number of passengers, to make it less abstract, more like an infographic, less like a chart with abstract information like rates on it. I used a grouped stacked bar chart. Unfortunately I couldn't find a way to color the male and female column differently, so the details were only revealed by hovering the mouse cursor over the bars. The feedback mentioned that there are too many things to compare on this chart to understand the story, the message was not clear.

### Final version
I decided to go back to Survival rate instead of Number of passengers for the y axis, and decided to use two charts. This way the grouped bars tell the story, the two colors highlight the strong difference between the survival rates of males and females across age groups and passenger classes. I think I have found the balance between compactness and clarity, and also managed to find the right visual aids (grouped bars, colors) to highlight the story that I wanted to tell.

## The story
After exploring the data using Python and Pandas, I found the two charts included in my final version the most revealing about the most influential factors that determined the survival rate of passengers: gender and class. Female passengers and passengers in higher classes had the best chances to survive. Age was an important factor only in the case of children.

Let's come up with 3 categories: 
- high chance of survival: survival rate above 0.66
- medium chance of survival: survival rate between 0.33 and 0.66
- low chance of survival: survival rate below 0.33

### Survival rate by age and sex

We can see that adult females had high chance of survival, age was not an important factor in their case. Adult males had a low chance of survival, age was again not an important factor. Age was only important factor for children, in their case gender was the factor which was not important: they all had medium chance of survival.

### Survival rate by passenger class and sex

There was one other factor that was influencing the survival rates of males and females: the passenger class. Females travelling on first and second class had high chance of survival, the "female survival rate" only decreased for females travelling on third class, where they had a medium chance.

Males had a medium chance of survival on first class and low chance of survival on second and third class.

To summarize, we could rank the chances of survival as follows:

High chance: females travelling on first or second class
Medium chance: females on third class, males on first class, children
Low chance: Males on second and third class

From the charts it is clear that the most important factor that influenced survival rates was gender, but passenger class was the second most important factor. 



