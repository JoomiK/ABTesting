### AB testing different teaching methods with Pymc3

This study looked at whether the order of presenting materials in a high school biology class made a difference in test scores. 

High school students were split into two groups; in Group 1, Mendelian genetics was taught before any in-depth discussion of the molecular biology underpinning genetics. In Group 2, the molecular biology was taught before teaching Mendelian genetics. Some teachers have hypothesized that the second method would be better for students; we looked at the evidence with this study.

Note: Every attempt was made to control for all other variables in the two groups; most importantly, they had the same teacher, textbook, and access to materials. Students were randomly placed into a group. However, there were a few things that could not be controlled for- notably, the two groups met on different times of the week.  

### Approach:  
Here I look at exam score data for the two groups- this exam specifically focused on the conceptual understanding of genetics.

I use both classical hypothesis testing and Bayesian methods to estimate how different the scores were between the two groups, and estimate the uncertainty associated with that difference.

### Documents:  
prep_data.py has functions for prepping the data.  
HypothesisTestingSimulations.py has functions for simulation-based hypothesis testing.  
AB_Testing_teaching_methods.ipynb goes through the workflow.  

---

See the blog post on this project [here](https://joomik.github.io/abtesting/).
