# Data Vizualization - Project 6

### Summary 

 The data used for this visualization is the Baseball dataset. The data includes a player's height, weight, handedness, home runs, and batting average. I created this data visualization to emphasize the main idea of this data set: that left handed batters have a higher median of home runs hit compared to ambidextrous and left handed batters.

### Design

The initial design was to include a task bar with my name, a graph title, and a graph. The base web page was taken from a bootstrap template so that I could focus more on data visualizations and less on HTML/CSS. My initial idea was to plot a bubble chart of height vs weight, with the bubble size to correspond to batting average. The graph will be faceted on handedness so that you can compare the locations where size is bigger for each handedness. The handedness has the biggest circles will show that they are the better performing handedness. 

After recieving feedback, I felt that reviewers 1 through 3 focused on aesthetics to make my bubble visualization better. Reviewer 4 mentioned that the visualization does not focus on a specific clear finding, and that it was more of an exploratory than explainatory visualization. I decided that I wanted to show how left handed batters have higher median home runs hit than ambidextrous or right handed batters. To really focus on this finding, I realized that a bar chart showing the median home runs hit for each handedness would be the clearest visualization.

To find the median home runs for each handedness, I used the pandas library in python. The python file in the scripts folder will take the baseball data, group it by handedness, and find the median values for each column in the data set. I used the dimplejs library to plot out the handedness and median home runs on a bar graph.

### Feedback

##### Reviewer 1<br>
-The scale for weight should show up under each of the handed categories

##### Reviewer 2<br>
-Would be nicer if they were all plotted on the same scale instead of being separated. This way you can directly compare points in one handedness to another.

##### Reviewer 3<br>
-Nicely done. I think that a bar chart would be better though.

##### Reviewer 4<br>
-(With bubble chart design) I am marking this as not meeting specification since in this project we require that the visualization centers on a specific, clear finding in the data. 

### Resources

Dimple Documentation -<br>
https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.chart#series

Data set -<br>
https://docs.google.com/document/d/1w7KhqotVi5eoKE3I_AZHbsxdr-NmcWsLTIiZrpxWx4w/pub?embedded=true

Explainatory vs Exploratory Analysis -<br>
http://www.storytellingwithdata.com/blog/2014/04/exploratory-vs-explanatory-analysis