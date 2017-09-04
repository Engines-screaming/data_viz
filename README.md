# Data Vizualization - Project 6

### Summary 

 The data used for this visualization is the Baseball dataset. The data includes a player's height, weight, handedness, home runs, and batting average. I created this data visualization to emphasize the main idea of this data set: that right handed batters have better batting averages than left or ambidextrous batters.

### Design

The initial design was to include a task bar with my name, a graph title, and a graph. The base web page was taken from a bootstrap template so that I could focus more on data visualizations and less on HTML/CSS. My idea is to plot a bubble chart of height vs weight, with the bubble size to correspond to batting average. The graph will be faceted on handedness so that you can compare the locations where size is bigger for each handedness. The handedness has the biggest circles will show that they are the better performing handedness. 

After recieving feedback, I felt that reviewer 1 and 2 had very valuable input. I think that plotting all points on the same scale make things a lot easier to compare. You can compare which different color dots are bigger a lot easier since the bigger one will create a halo around the point, showing that the corresponding handedness has a higher batting average. With all points on the same scale, having numbers show up on the x axis was not a problem. I felt that a bar chart was not appropriate for the main idea I was trying to show, since bar charts are good for showing aggregated totals such as total home runs per each handedness category. 

### Feedback

##### Reviewer 1<br>
-The scale for weight should show up under each of the handed categories

##### Reviewer 2<br>
-Would be nicer if they were all plotted on the same scale instead of being separated. This way you can directly compare points in one handedness to another.

##### Reviewer 3<br>
-Nicely done. I think that a bar chart would be better though.

### Resources

Dimple Documentation -<br>
https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.chart#series

Data set -<br>
https://docs.google.com/document/d/1w7KhqotVi5eoKE3I_AZHbsxdr-NmcWsLTIiZrpxWx4w/pub?embedded=true
