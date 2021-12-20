# Center and Variability

## Center
1. Define **mean**, **median**, and **mode**.
mean is the arithmetic mean of all values, median is the middle value (when values are ordered from smallest to largest), mode is the most commonly occurring value, 
1. When people talk about taking an average, which **measure of center** are they usually referring to?
They mean the arithmetic mean
2. What is an **outlier**, and which measure of center does it affect the most?
The outlier would affect the average the most
3. if the **median** is greater than the **mean**, what does that tell you about the _skew_ of the distribution?
It would skew to the left because the values are more to the right
4. Give an example of a situation where finding the **mode** of a dataset would be useful.
Favorite sport out of a population
5. Two datasets have the same **mean** of 1.15. Are these two datasets the same? Why or why not?
Not neccesarily,  dataset of 1.15 as the only value is not the same as 100 values that have a mean of 1.15

## Variability
The **variability** of a dataset is also called its **spread**.

### Range
We will be examining the bill lengths of Gentoo penguins (again). Make sure you have Python code to read and analyze `penguins.csv`

1. What is the **range** of a dataset, and what is the **range** of Gentoo bill lengths?
   18.7
2. For this question, let's introduce a new datapoint: a bill length of `80.2`
   1. Does the range change, and if so, what is the new range?
   The range changes from 18.7 to 36.3
   2. How will this affect the mean, median, and mode?
   The mode wont change and the median will shift one datapoint but its value wont change signifantly, the mean would change (increase significantly)
3. For this question, let's introduce 30 new observations, all with petal length `48.1`
4. SKIP BC WE DONT HAVE THIS CSV
   1. Does the range change, and if so, what is the new range?
   the range doenst change
   2. How will this affect the mean, median, and mode?
   The mode changes to 48.1, the and the mean changes to become closer to 48.1
5. Based on your answers above, when do new data points affect the range?
   If they are greater than the max or less than the min
6. What does the range tell us about a dataset, and what _doesn't_ it tell us?
   It tells us the span of the values, but not how they are distributed in that span

### Percentiles and Quartiles
1. What is a **percentile**, and is it a single point or an interval?
   The n/100th marker in the dataset from small to largest
   50th percentile on a test was a B
   for ex. 
   it is a point, everything below that value is part of the percentile

2. What is a **quartile**?
   Seperating into 4 groups and in between the points is part of that quartile
3. Why is the median sometimes called the **2nd quartile (Q2)**?
   Because if you split the dataset into 4 quartiles, the middle one should be the half-way point
4. Examine the following table. What can you tell about the _shape_ of this distribution?
    | Q0 | Q1 | Q2 | Q3 | Q4 |
    |:--:|:--:|:--:|:--:|:--:|
    |0|4|7|9|10|
    It is skewed left because more values between Q0 and Q1 (0-4) than between Q3 and Q4 (9-10)
    
### IQR and Basic Visualizations
Shown below is a **box plot** of Gentoo bill lengths.

![Boxplot of Gentoo bill lengths](img/boxplot.png)

1. Where do the **whiskers** extend to?
   They extend to min and max (excluding whiskers)
2. What percentage of the dataset is represented by the **box**?
   50% of the data is in the box
3. What is an **interquartile range (IQR)**?
   middle 50% of the dataset from lowest to highest
4. Any observation that is `1.5*IQR` below Q1 or above Q3 is marked as a _potential_ outlier.
   1. How is this displayed in the box plot? Show the math necessary to determine that datapoint is an outlier.
   more than 1.5IQR below Q1 or 1.5IQR above Q3 defines an outlier
   1. The `1.5IQR` rule can give a false positive; that is, a datapoint that is marked as an outlier even when it isn't one. Describe an example where that happens.
   bimodal data or trimodal data would have IQR that could discount the other modes, so we could have 'outliers' that arent outliers. 
   Skewed or multimodal datasets could have these problems but 1.5IQR is still a good benchmark for determining outliers. 
Shown below is a **violin plot** for the same data.

![Violin plot of Gentoo bill lengths](img/violin.png)

1. How do the **box and whiskers** of a violin plot differ from those of a box plot?
The whiskers extend to their normal point but the box would be the area of the violin graph
2. What information does a violin plot provide that a box plot doesn't?
   It provides better information about frequency because the thicker the part the more values in that area
3. When would we want to use a violin plot over a box plot?
   It would not tell us anything about frequency and violin plots do tell us about frequency
   Test scores would be simplified into quartiles in box plot but violin plot could show us that 89% is a very common score and thus the violin would be thicker at that point. 

### Deviation
1. What is a datapoint's **deviation** in relation to the dataset mean?
   the datapoint's distance from the mean
2. What is a dataset's **standard deviation**?
   A measure of the variablity from the mean, it is a measure of center
3. What is the standard deviation of Gentoo bill lengths?
   3.081857372114287
4. What is an observation's **z-score**, and how is that related to a dataset's standard deviation?
   The z-score is the number of standard deviations by which the value of a data point is above or below the mean. Above the mean is positive z score and below mean is negative z score
5. Why might **z-score** be a better measure than deviation?
   Z score standardizes datapoints with respect to a standard deviation and mean instead of comparing raw (absolute) data to raw data. comparing their deviations wounldnt be too helpful to compare. 
   ex. comparing sports players' skills from 1940s to today, the raw scrore istn too helpful, the z score is more relevant because that tells us their relative skill level compared to the mean
   this zscore can be standardized. 