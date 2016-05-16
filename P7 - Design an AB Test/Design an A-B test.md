# Design an A/B test
### Project submission for Udacity's Data Analyst nanodegree
#### by Gabor Galgocz

# Experiment design

## Metric choice
*List which metrics you will use as invariant metrics and evaluation metrics here.* 


### 1. Invariant metrics
*Number of cookies:*
This is basically the unique visits to the site. Since the changes happen at a later phase in the funnel, the traffic to the site is not affected by the experiment.

*Number of clicks:*
Again, the changes happen at a later phase, the number of clicks cannot be affected by the experiment. 

*Click-through-probability:*
This metric is derived from the above two metrics, it's a ratio of them, so it is also not affected by the experiment. 

### 2. Evaluation metrics
*Gross conversion:* 
The hypothesis behind the experiment is that the changes will reduce the number of students who abandon the course after the free trial. This means the evaluation is based on the difference between the number of students who start the trial and who finish it. To measure it, we need to evaluate how many students start the free trial - and this metric is exactly what we need for that. 

Our expectation is that this metric will decrease in the experiment group, because the new step asking the students will present a choice where one of the options is to access the free course materials instead of starting the trial, thus reducing the number of cookies who actually start the free trial.

*Retention:* 
To be able to compare the differences between the students who start the free trial and the ones who actually complete it and remain enrolled, the best is if we use a ratio, and this is the metric for that. The hypothesis suggests that the retention will increase, because the number of starters will possibly decrease and the number of finishers will increase. This metric is derived from gross and net conversion (it is basically a ratio of the two), so if we want to focus on just one metric to evaluate our results, this should be it. Of course as analysts we should look at all evaluation metrics, but for decision makers this is a good single metric to communicate.

Our expectation is that this metric will increase in the experiment group, because the new step will ensure that students who cannot dedicate enough time for the course will not start the free trial. This means that only more dedicated students will be taking the trial, their drop out rate will be lower, thus retention will be increased. 

*Net conversion:* 
As mentioned at the gross conversion part, we need to measure the number of students who start the free trial and the ones who complete it. This metric measure the number of completions, we need both metrics to understand the user behaviour and to calculate retention. 

Our expectation is that this metric will not decrease in the experiment group, because the only thing that would change in the experiment that less dedicated students would be leaving the funnel earlier than before. If this metric would decrease, that would mean that the experiment is causing harm and the change should definitely not be rolled out. 

### 3. Unused metrics
*Number of user-ids*
The number of user-ids is not a good invariant metric, because it is dependent on the experiment - we expect that the number of people starting the free trial will change after we make changes to the funnel. It is also not a good evaluation metric, because in itself it cannot be evaluated. We want to see how users proceed on to further stages of the funnel, so just by knowing how many people are in the funnel cannot be evaluated. Also, it can fluctuate between days and between the control and experiment groups. 

## Measuring standard deviation
*List the standard deviation of each of your evaluation metrics.*

*Gross conversion:*
0.0202

*Retention:*
0.0549

*Net conversion:*
0.0156

*For each of your evaluation metrics, indicate whether you think the analytic estimate would be comparable to the the empirical variability, or whether you expect them to be different (in which case it might be worth doing an empirical estimate if there is time). Briefly give your reasoning in each case.*
The unit of diversion and unit on analysis (which is the user-id) is the same for net and gross retention. We can expect that the analytical estimate will be comparable to the empiricial variability. The retention is a ratio of these two metrics, so we don't have to treat it as an independent metric. 

## Sizing
### Number of samples vs. power
*Indicate whether you will use the Bonferroni correction during your analysis phase, and give the number of pageviews you will need to power you experiment appropriately.* 

#### Will you use the Bonferroni correction in your analysis phase?

I did not use the Bonferroni correction. 

#### Which evaluation metrics did you select?

I chose to use net conversion and gross conversion. Retention is their ratio, it is not an independent metric, I will focus only on net and gross conversion to evaluate the experiment. 

#### How many pageviews will you need?
I used the online calculator to calculate the necessary sample size:
http://www.evanmiller.org/ab-testing/sample-size.html

I calculated the necessary sample size for both the net and gross conversion, it gave me a higher required sample size for the net conversion (27413), so I used it to establish the required number of pageviews, so I could be sure that all metrics had the required sample size for each group in the experiment. Knowing the probability of click-through on the "start of free trial" button (0.08) I could calculate the number of required page views for each group (342662.5), so the required total is the double if that:

685325


### Duration vs Exposure
*Indicate what fraction of traffic you would divert to this experiment and, given this, how many days you would need to run the experiment.*
*Give your reasoning for the fraction you chose to divert. How risky do you think this experiment would be for Udacity?*

After making sure that the changes required for the test are thouroughly tested, bug free, so there is no risk of negatively affecting the user experience, I would use the full audience for this test (50%-50%). Of course the user experience metrics will need to be monitored throughout the test (bounce rate, the number of signups, etc.). Knowing the daily traffic (40000), the experiment would require 17.13 days to complete (let's round that to 18).



#### Number of pageviews
685325

#### Fraction of traffic exposed
1

#### Length of experiment
18

# Experiment analysis
## Sanity checks
*For each of your invariant metrics, give the 95% confidence interval for the value you expect to observe, the actual observed value, and whether the metric passes your sanity check.*

Based on the provided data, we know the total number of pageviews (that is, the number of cookies), the clicks on "start free trial" and we can calculate the click-through probability based on the above two metrics. Based on these, we can calculate the confidence interval and check if the metrics are equivalent within the confidence interval for the two groups.

#### Number of cookies

Control group = 345543
Experiment group = 344660
Standard deviation = sqrt(0.5 * 0.5 / (345543 + 344660)) = 0.0006018
Margin of error = 1.96 * 0.0006018 = 0.0011796
Lower bound = 0.5 - 0.0011797 = 0.4988
Upper bound = 0.5 + 0.0011797 = 0.5012
Observed value = 345543 / (345543 + 344660) = 0.5006

The observed value is within the range of the confidence interval, it passes the sanity check.


#### Number of clicks on "Start free trial"

Control group = 28378
Experiment group = 28325
Standard deviation = sqrt(0.5 * 0.5 / (28378 + 28325)) = 0.0021
Margin of error = 1.96 * 0.0021 = 0.0041
Lower bound = 0.5 - 0.0041 = 0.4959
Upper bound = 0.5 + 0.0041 = 0.5041
Observed value = 28378 / (28378 + 28325) = 0.5005

The observed value is within the range of the confidence interval, it passes the sanity check.

#### Click-through probability on "Start free trial"

Control = 0.0821258
Standard deviation = sqrt(0.0821258 * (1-0.0821258) / 344660) = 0.000468
Sargin of error = 1.96 * 0.000468 = 0.00092
Lower bound = 0.0821258 - 0.00092 = 0.0812
Upper bound = 0.0821258 + 0.00092 = 0.0830
Observed = 0.0821824 

The observed value is within the range of the confidence interval, it passes the sanity check.


## Result analysis
### Effect size test
*For each of your evaluation metrics, give a 95% confidence interval around the difference between the experiment and control groups. Indicate whether each metric is statistically and practically significant.*

*Gross conversion:*
Lower bound: -0.0291
Upper bound: -0.0120

It is both statistically and practically significant, because the range does not include 0 or the minimum boundary of practical significance.

*Net conversion:*
Lower bound: -0.0116
Upper bound: 0.0019

It is neither statistically or practically significant, since the range includes zero and the upper bound is below the threshold of practical significance. Let's also note that the lower bound is lower than the negative of the practical significance boundary.


### Sign tests
*For each of your evaluation metrics, do a sign test using the day-by-day data, and report the p-value of the sign test and whether the result is statistically significant.* 

*Gross conversion*
Alpha-level: 0.025
p-value: 0.0026

The result confirms that the finding is statistically significant.


*Net conversion*
p-value: 0.6776

This is higher than the alpha-level, so this confirms that the finding is not statistically significant.


### Summary
In this experiment, we have two evaluation metrics, net and gross conversion. Our expectation is that gross conversion will decrease while net conversion will not be significantly change. We need both metrics to match our expectations, so this is not a case where using the Bonferroni correction would be justified (which is designed to be used in experiments where *any* of the evaluation metrics could be justifying a success in the experiment).

Based on the results, it seems like making the change to the funnel would decrease gross conversion (the number of students starting the free trial) but would not significantly increase the net conversion (the number of students completing the free trial and thus becoming paid student). There is also a chance that the net conversion will decrease, so this experiment should not be launched.

## Recommendation
My recommendation is not launch this experiment. We have two evaluation metrics, and in order to consider the experiment a success, we need both metrics to meet our expectations. 

The gross conversion met our expectations, it decreased, and it was both statistically and practically significant. 

On the other hand, we saw that the net conversion did not meet our expectations. It did not reach statistical significance, and it also did not reach the practical significance boundary - actually its confidence interval included the negative of it. This means that rolling out the experiment could possibly decrease the net conversion, that is, the number of students continuing to enroll in the course. This experiment was not successful, the changes should not be rolled out.


# Follow-up experiment 
*Give a high-level description of the follow up experiment you would run, what your hypothesis would be, what metrics you would want to measure, what your unit of diversion would be, and your reasoning for these choices.*
I think the main problem with this experiment is that it actively diverts people from starting the free trial, so I would definitely avoid similar options. While I agree with the idea that notifying the students that the successful completion needs a serious dedication of time, this could be done in other ways too.

I would definitely move the experimental phase to a later step in the funnel, so I would not change the start phase. 

I think most people drop out of courses because they face a challenge at an early phase, and they don't get any reward. Their background knowledge might be lacking or they might need some help. I would try an experiment where during the trial period, maybe after the first week the experiment group would be asked for their feedback (in an email or in a small pop-up survey message) and if they are stuck with something and need help to get "unstuck". I think this would also highlight the benefits of personal coaching and the attention and help students might get from Udacity.

So the experiment would work as follows:
- after the first week of the free trial, an email would be sent to the members of the experiment group, asking for their feedback and mentioning that they can get personalized help from coaches if they are stuck. There would be a link where they could read more about coaching and ask for assistance. 

Evaluation metric would be retention. Retention is based on user-ids, so it's more stable than net conversion. I expect it to increase compared to the control group. The number of cookies, number of clicks, click-through probability and gross conversion will not be used, since they are related to earlier steps in the funnel. The user-id would be used as invariant metric, since it describes the number of enrolled students, who are the subjects of the experiment. The unit of diversion would be the same too, user-id. 

The hypothesis is that even without asking for assistance, the email explaining the idea of coaching, as a way to get "unstuck" would send a very positive message and would help with keeping more students in the course. It would also help students understand why should they pay for a course if there are so many free resources available online. To be more specific, I would expect that the net conversion and retention would both increase in the group which receives the email. I would need both of them to increase, if only one would increase that would be a warning that something is not set up correctly in the experiment. 



 



