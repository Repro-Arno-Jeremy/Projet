# Reproducibility Arno-Jeremy

## Introduction

The goal of this project is to reproduce experiments this article https://blog.mathieuacher.com/FootballAnalysis-xG-COVIDHome/ in order to analyse if playing at home in football is an advantage especially the effects of Covid on it. Our goal during reproduction was to scrap data of five football leagues and then reproduce all of the graphs using the same metrics to compare the results. We also add recent years which is a factor of relicability to have more information on data before and after Covid pandemic. 

## Reproducibility

### How to Reproduce the Results
1. **Requirements**  
   For this project, we have used : 
    - Python 3.12.4
    - pandas
    - matplotlib
    - BeautifulSoup / requests
    - numpy
    - scipy

The data have been scrapped on https://understat.com/. BeautifulSoup and requests were used to scrap data. pandas and matplotlib were used to reorganise data and print it using graphs.

2. **Setting Up the Environment && Reproducing Results**  
   - Both Dockerfiles are setting up the environment and also reproducing results
   - Provide instructions for using the Dockerfile to create a reproducible environment:  
     ```bash
     docker build -t reproducible-project .
     docker run -v ./output:/app/output reproducible-project
     ```

   - Results of both studies (reproducibility and replicability) can then be seen in the html file of their output folder (`analysis_results.html`), 
     Opening it will show all code and output produced by the original notebook

4. **Automation (Bonus)**  
   - Explain the included GitHub Action that produces or analyzes data automatically.  
    
### Encountered Issues and Improvements

The hardest part was to find where data can be scrapped on understat. At the beginning, we didn't scrap the appropriate field to compute graphs of the paper.

For all graphs of the study, we didn't encounter any issue except for the last one.

The last one was about the Mann–Whitney U test to assess differences between seasons on the xPoints metric.
After implementing this test, we found exactly twice the results of the paper. For example, Bundesliga 2014-2015 was 0,231377 on the paper and 0.462894 with our programm. We conclude that the difference between these two experiments was an update in the spicy library. 

In addition, the wilco-xG and wilco-xG-pvalue columns have errors. All the values are the same.

### Is the Original Study Reproducible?

We succeded to reproduce all the graphs of the study except some graphic points that doesn't change the final result. As said before, metrics like wilco-xG and wilco-xG-pvalue were not provided. Then we calculate our own and it confirms the actual tendance that playing at home is still an advantage after the Covid.

Globally, the advantage of playing of home has regrown since the end of Covid. For example, in Bundesliga in 2022, results average was approximately 1.65 which is close to results before the pandemic. In addition, in Laliga in 2022, Diff_points was at 219 which is not far than the maximum diff_points of 234 in 2015.

The only failure of the study was the values of p-value in Mann–Whitney U test as explained before.

- Summarize the success or failure of reproducing the study.
- Include supporting evidence, such as comparison tables, plots, or metrics.

## Replicability

### Variability Factors
- **List of Factors**: Identify all potential sources of variability (e.g., dataset splits, random seeds, hardware).  
  Example table:
  | Variability Factor | Possible Values                                                   | Relevance                                   |
  |--------------------|-------------------------------------------------------------------|---------------------------------------------|
  | Others leagues     | [Turkey, Portugal, Greece, Netherlands, Belgium...]               | Covid may not impact these leagues          |
  | Scipy Version      | Under 1.7 or above                                                | p-value of tests may bedivided by two       |
  | Dataset Version    | After 2020                                                        | Ensures comparability across years          |
  | Others sports      | [Basketball, Baseball, Rugby...]                                  | Home advantage may not be impacted          |   

- **Constraints Across Factors**:  
  - Document any constraints or interdependencies among variability factors.  
    For example: 
    - Random Seed must align with dataset splits for consistent results.
    - Hardware constraints may limit the choice of GPU-based factors.

- **Exploring Variability Factors via CLI (Bonus)**  *
    We already compute all the graphs for 5 additionals leagues without any CLI. We also provide data for the seasons after 2020 for the original study.

### Replication Execution
1. **Instructions**  
 - Instructions for using the second Dockerfile with other study:
     - The terminal must be in Other_leagues
     ```bash
     docker build -t reproducible-other-study .
     docker run -v ./output:/app/output reproducible-other-study
     ```
- Results of both studies (reproducibility and replicability) can then be seen in the html file of their output folder (`analysis_results.html`), 
Opening it will show all code and output produced by the original notebook

2. **Presentation and Analysis of Results**  
   - Include results in text, tables, or figures.
   - Analyze and compare with the original study's findings.

### Does It Confirm the Original Study?
- Summarize the extent to which the replication supports the original study’s conclusions.
- Highlight similarities and differences, if any.

## Conclusion
- Recap findings from the reproducibility and replicability sections.
- Discuss limitations of your
