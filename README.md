### AB testing different teaching methods with Pymc3

This was from a study that looked at whether the order of presenting materials in a high school biology class made a difference in test scores. 

High school students were split into two groups; in Group 1, Mendelian genetics was taught before any in-depth discussion of the molecular biology underpinning genetics. In Group 2, the molecular biology was taught before teaching Mendelian genetics. Some teachers have hypothesized that the second method would be better for students; we looked at the evidence with this study.

Here I look at exam score data for the two groups- this exam specifically focused on the conceptual understanding of genetics.

I use Bayesian methods to estimate how different the scores were between the two groups, and estimate the uncertainty associated with that difference.

See the blog post on this project [here](https://joomik.github.io/abtesting/).
