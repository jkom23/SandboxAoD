# Name:
Jack Komaroff

Please respond to the following questions. _Show your work_ if applicable, and be as _explicit_ as possible in your answers.

1. In the following snippet of code, label the name of the variable and the name of the class. Use this example to explain what an object is in the context of memory.
    ```py
    p1 = Point(2,3)
    ```

The class is the "Point" class and the the variable (object of that class) is "p1". We are creating an object of this class, called p1, and it has certain values baked into it that we have set with the Point constructor method. Namely, it has, logically, (I am assuming because I don't have the full code) an x value of 2 and a y value of 3. In terms of computer memory, there is a unique memory address for this object. It will be some strange combination of letters and numbers (ex. 0x01L5FBB92C) that the computer can understand as where that actual object of the point class (p1) is stored on my local PC.

2. A researcher is conducting a survey on favorite sports and encodes each sport with a number. For example, 1=Archery, 2=Boxing, 3=Curling, and so on. They average these numbers to get 2.3 and conclude that on average, people's favorite sport is boxing on ice. Why is this incorrect?

We are not looking for the average value, we want the mode. This will tell us which number (and thus a corresponding sport) is the most commonly occurring in our group of subjects, and thus this mode value will be the favorite sport. Also, this data is not ordinal, but the researches are making it ordinal by averaging the values, which is fundamentally incorrect. 

3. A researcher is conducting a study on vegetarian diets. They stand in front of a build-your-own-salad restaurant and survey people who enter. Identify the population, and explain why this is not a great sample.

The population depends on the research experiment and how broad of a claim that the researchers want to make. From the description given, it appears that the researchers want to make a broad claim about all vegetarians (presumably in the US or NYC). The people who are in front of this salad bar restaurant are not a great sample because these are people who have diets that consist of (at least partially of) salads, and not tofu or beans, pasta, pizza, etc. Therefore, we are not looking at a true representation of all vegetarians and our sample (chosen non probabilistically) is far too narrow to make a substantial claim about the entire vegetarian community. This is a prime example of coverage bias, as our sample is not a proper representation of our larger population (all vegetarians, who don't necessarily have a salad based diet). 

4. A researcher wants to study the population of all New York City residents. What is a feasible sample frame, and what biases might this sample frame be prone to?

This depends on the conclusion that we want to make. If I wanted to make a conclusion (as the problem says) about all NYC residents, I would want a large n. Perhaps, I can go to different facebook message groups, put up signs on community/school boards, place flyers on trees, that all advertise a study that I would pay people to attend. This method is feasible, but has some major biases as people with lower incomes would have a far greater tendency to participate in this study due to its financial reward. Also, with facebook message boards, we would get far more adults than kids (perhaps the school flyers could help balance this, but nonetheless there is bias). There are many coverage biases and other biases that could drastically alter the accuracy of this study. To conclude, a study of this large conclusion would need a team of researchers would lots of resources to accurately cover all groups of people in the sample frame and minimize and coverage bias. 

5. A scientist conducted an observational study on mental health and calculated that the correlation between recreational drug use and depression is 0.83. Why can't they conclude that recreational drug use causes depression?

By the very nature of observational studies, we can't make claims about causality, only correlation. We are not (and this would raise many ethical/moral questions) providing drugs to people and seeing if they develop depression. So, since the researches are not changing the independent variable (the use of drugs) and seeing how the dependent variable (depression) changes, we can't show that drugs CAUSE depression (we can only show correlation between drugs and depression). Also, we would want a very rigorous study design with a large RCT to make such a strong claim. 

The confounding factor in this spurious correlation is poverty, this is the reason for this observation. With a confounding variable like poverty or subpar living environments, especially at a young age, we see depression develop AND recreational drug use. The drug use is due to a lack of strong role models, social pressures, etc. Therefore, these two results are present but one does not cause the other, poverty is simply the confounder in this correlation. 